#!/usr/bin/env python3
"""sonde.py — relève la machine et les services déjà en place, sans rien modifier.

Sert au cadrage d'un projet : le skill n'a pas à demander ce qu'il peut lire.
Bibliothèque standard seulement. Aucune écriture, aucun réseau hors de localhost.

    python3 sonde.py            # résumé court en français, puis le JSON
    python3 sonde.py --json     # JSON seul
"""

from __future__ import annotations

import json
import os
import platform
import shutil
import socket
import subprocess
import sys

# Port local -> service que ce port trahit. Une réponse sur le port suffit.
PORTS = {
    11434: "Ollama",
    8000: "serveur HTTP (vLLM ou FastAPI)",
    8080: "serveur HTTP",
    5432: "PostgreSQL",
    3306: "MySQL / MariaDB",
    6379: "Redis",
    6333: "Qdrant",
    8123: "ClickHouse",
    9000: "MinIO",
    5000: "MLflow",
    9200: "Elasticsearch / OpenSearch",
    7687: "Neo4j",
    27017: "MongoDB",
    3000: "Grafana ou appli web",
    9090: "Prometheus",
}

# Outils cherchés dans le PATH.
OUTILS = ["git", "uv", "python3", "pip", "docker", "podman", "node", "npm", "ollama",
          "vllm", "psql", "redis-cli", "make", "just", "gh"]


def lance(cmd: list[str], delai: int = 4) -> str:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=delai)
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def est_wsl() -> bool:
    try:
        return "microsoft" in platform.release().lower() or "wsl" in platform.release().lower()
    except Exception:
        return False


def memoire_go() -> float | None:
    try:
        if sys.platform.startswith("linux"):
            with open("/proc/meminfo", encoding="utf-8") as f:
                for ligne in f:
                    if ligne.startswith("MemTotal"):
                        return round(int(ligne.split()[1]) / 1024 / 1024, 1)
        if sys.platform == "darwin":
            return round(int(lance(["sysctl", "-n", "hw.memsize"])) / 1024 ** 3, 1)
        if sys.platform.startswith("win"):
            sortie = lance(["powershell", "-NoProfile", "-Command",
                            "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory"])
            return round(int(sortie) / 1024 ** 3, 1)
    except (ValueError, OSError):
        pass
    return None


def gpu() -> list[dict]:
    """GPU NVIDIA par nvidia-smi ; AMD par rocm-smi ; Apple par le modèle de puce."""
    trouves: list[dict] = []
    if shutil.which("nvidia-smi"):
        sortie = lance(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"])
        for ligne in sortie.splitlines():
            nom, _, mem = ligne.partition(",")
            trouves.append({"marque": "NVIDIA", "nom": nom.strip(), "memoire": mem.strip()})
    elif shutil.which("rocm-smi"):
        trouves.append({"marque": "AMD", "nom": "voir rocm-smi", "memoire": ""})
    elif sys.platform == "darwin" and platform.machine() == "arm64":
        trouves.append({"marque": "Apple", "nom": lance(["sysctl", "-n", "machdep.cpu.brand_string"]),
                        "memoire": "mémoire unifiée"})
    elif sys.platform.startswith("win"):
        sortie = lance(["powershell", "-NoProfile", "-Command",
                        "(Get-CimInstance Win32_VideoController).Name"])
        for nom in sortie.splitlines():
            if nom.strip():
                trouves.append({"marque": "?", "nom": nom.strip(), "memoire": ""})
    return trouves


def ports_ouverts() -> list[dict]:
    ouverts = []
    for port, nom in PORTS.items():
        s = socket.socket()
        s.settimeout(0.15)
        try:
            if s.connect_ex(("127.0.0.1", port)) == 0:
                ouverts.append({"port": port, "service": nom})
        except OSError:
            pass
        finally:
            s.close()
    return ouverts


def conteneurs() -> list[str]:
    moteur = "docker" if shutil.which("docker") else ("podman" if shutil.which("podman") else "")
    if not moteur:
        return []
    sortie = lance([moteur, "ps", "--format", "{{.Names}} ({{.Image}})"])
    return [ligne for ligne in sortie.splitlines() if ligne]


def sonde() -> dict:
    disque = shutil.disk_usage(os.getcwd())
    return {
        "systeme": platform.system() + (" (WSL)" if est_wsl() else ""),
        "version": platform.release(),
        "architecture": platform.machine(),
        "processeurs": os.cpu_count(),
        "memoire_go": memoire_go(),
        "disque_libre_go": round(disque.free / 1024 ** 3),
        "gpu": gpu(),
        "outils": {o: bool(shutil.which(o)) for o in OUTILS},
        "ports_ouverts": ports_ouverts(),
        "conteneurs": conteneurs(),
        "dossier_courant": os.getcwd(),
    }


def resume(d: dict) -> str:
    lignes = [f"Système : {d['systeme']} {d['architecture']}",
              f"Processeurs : {d['processeurs']} · Mémoire : {d['memoire_go']} Go · Disque libre : {d['disque_libre_go']} Go"]
    if d["gpu"]:
        lignes.append("GPU : " + " ; ".join(f"{g['marque']} {g['nom']} {g['memoire']}".strip() for g in d["gpu"]))
    else:
        lignes.append("GPU : aucun détecté (CPU seulement)")
    presents = [o for o, ok in d["outils"].items() if ok]
    lignes.append("Outils présents : " + (", ".join(presents) or "aucun"))
    if d["ports_ouverts"]:
        lignes.append("Services qui répondent : " + ", ".join(f"{p['service']} (:{p['port']})" for p in d["ports_ouverts"]))
    else:
        lignes.append("Services qui répondent : aucun")
    if d["conteneurs"]:
        lignes.append("Conteneurs : " + ", ".join(d["conteneurs"]))
    return "\n".join(lignes)


def main() -> int:
    d = sonde()
    if "--json" not in sys.argv:
        print(resume(d))
        print()
    print(json.dumps(d, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
