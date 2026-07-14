# gen-stubs-batch.ps1 - Genere en lot des stubs Services compacts
# pour combler les wikilinks fantomes restants apres le batch principal.
#
# Usage : powershell -ExecutionPolicy Bypass -File AI/scripts/gen-stubs-batch.ps1
#
# Chaque stub a : frontmatter complet + Pourquoi + Quand l'utiliser
# + Quand NE PAS l'utiliser + Pieges + Liens. Format compact (~25-35 lignes).

$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $root
$today = Get-Date -Format "yyyy-MM-dd"

function Write-Stub {
    param(
        [string]$Dir,
        [string]$Name,
        [string]$Categorie,
        [string[]]$SubCat = @(),
        [string[]]$Alias = @(),
        [string[]]$Tags,
        [string]$Why,
        [string[]]$WhenUse,
        [string[]]$WhenNot = @(),
        [string[]]$Pitfalls = @(),
        [string[]]$Links = @(),
        [string]$Url = "",
        [string[]]$Alternatives = @(),
        [string]$Licence = "",
        [string]$Langage = ""
    )
    $path = Join-Path $root "$Dir/$Name.md"
    if (Test-Path $path) { Write-Host "skip (existe) : $Dir/$Name.md"; return }

    $aliasStr = if ($Alias.Count -gt 0) { "[" + ($Alias -join ', ') + "]" } else { "[]" }
    $subCatStr = if ($SubCat.Count -gt 0) { "[" + ($SubCat -join ', ') + "]" } else { "[]" }
    $tagsStr = "[" + ($Tags -join ', ') + "]"
    $altStr = if ($Alternatives.Count -gt 0) { "[" + (($Alternatives | ForEach-Object { "`"$_`"" }) -join ', ') + "]" } else { "[]" }

    $sb = [System.Text.StringBuilder]::new()
    [void]$sb.AppendLine("---")
    [void]$sb.AppendLine("galaxie: dev")
    [void]$sb.AppendLine("nom: $Name")
    [void]$sb.AppendLine("alias: $aliasStr")
    [void]$sb.AppendLine("categorie: $Categorie")
    [void]$sb.AppendLine("sous_categories: $subCatStr")
    [void]$sb.AppendLine("licence: $Licence")
    [void]$sb.AppendLine("licence_type: open-source")
    [void]$sb.AppendLine("hosted: self")
    [void]$sb.AppendLine("maturite: production")
    [void]$sb.AppendLine("langage: $Langage")
    [void]$sb.AppendLine("clients_officiels: [python]")
    [void]$sb.AppendLine("plateforme: [linux, macos, windows]")
    [void]$sb.AppendLine("score: ")
    [void]$sb.AppendLine("mes_projets: []")
    [void]$sb.AppendLine("alternatives: $altStr")
    [void]$sb.AppendLine("remplace: []")
    [void]$sb.AppendLine("remplace_par: []")
    [void]$sb.AppendLine("created: $today")
    [void]$sb.AppendLine("modified: $today")
    [void]$sb.AppendLine("status: discovered")
    [void]$sb.AppendLine("tags: $tagsStr")
    [void]$sb.AppendLine("url_officiel: $Url")
    [void]$sb.AppendLine("url_docs: $Url")
    [void]$sb.AppendLine("url_repo: ")
    [void]$sb.AppendLine("---")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("# $Name")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("## Pourquoi")
    [void]$sb.AppendLine($Why)
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("## Quand l'utiliser")
    foreach ($w in $WhenUse) { [void]$sb.AppendLine("- $w") }
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("## Quand NE PAS l'utiliser")
    if ($WhenNot.Count -eq 0) {
        [void]$sb.AppendLine("- (a enrichir au fil des projets)")
    } else {
        foreach ($w in $WhenNot) { [void]$sb.AppendLine("- $w") }
    }
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("## Pieges connus")
    if ($Pitfalls.Count -eq 0) {
        [void]$sb.AppendLine("- (a enrichir via REX)")
    } else {
        foreach ($p in $Pitfalls) { [void]$sb.AppendLine("- $p") }
    }
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("## Liens")
    foreach ($l in $Links) { [void]$sb.AppendLine("- $l") }
    if ($Url -ne "") { [void]$sb.AppendLine("- Site : $Url") }

    [System.IO.File]::WriteAllText($path, $sb.ToString(), [System.Text.UTF8Encoding]::new($false))
    Write-Host "cree : $Dir/$Name.md"
}

# ?????????????????????????????????????????????????????????????????
# Data formats / lakehouse / orchestrators
# ?????????????????????????????????????????????????????????????????

Write-Stub -Dir "Services/Data" -Name "Apache Iceberg" `
    -Categorie "data/lakehouse" -SubCat @("lakehouse","table-format","acid") `
    -Alias @("iceberg") -Tags @("service","data","lakehouse","iceberg") `
    -Why "Format de table open pour data lakehouse. Apporte ACID + time travel + schema evolution + partition evolution sur des fichiers Parquet stockes en object storage (S3, GCS). Standard avec Delta Lake et Hudi." `
    -WhenUse @("Data warehouse modernes Spark / Trino / Flink","Multi-engine (lire avec un, ecrire avec l'autre)","ACID sur S3 sans serveur DB","Time travel et schema evolution") `
    -WhenNot @("Volume < 1TB -> simple Parquet partitionne suffit","Single-engine pure analytique -> DuckDB / ClickHouse direct","Pas de catalog dispo (besoin Glue, Nessie, REST catalog)") `
    -Pitfalls @("Compaction : petits fichiers grossissent -> planifier","Catalog mgmt critique (AWS Glue, Hive Metastore, Nessie, REST)","Snapshots accumulent -> expire policy") `
    -Links @("[[Parquet]] - format sous-jacent","[[Spark]] - engine principal","Delta Lake (alt) : https://delta.io/","Apache Hudi (alt) : https://hudi.apache.org/") `
    -Url "https://iceberg.apache.org/" -Licence "Apache-2.0" -Langage "Java"

Write-Stub -Dir "Services/Data" -Name "Avro" `
    -Categorie "data/format" -SubCat @("serialization","schema","streaming","kafka") `
    -Alias @("avro","apache-avro") -Tags @("service","data","format","streaming") `
    -Why "Format de serialisation row-based avec schema JSON integre. Standard de fait dans l'ecosysteme Kafka / Confluent Schema Registry. Compact, schema-evolution natif." `
    -WhenUse @("Streaming Kafka / Pulsar","Schema Registry (compatibilite forward/backward)","Echange systeme-a-systeme type","RPC type Apache Thrift") `
    -WhenNot @("Analytique columnar -> [[Parquet]] / ORC","Echange humain -> JSON","Sans schema stable -> Protobuf / JSON") `
    -Pitfalls @("Schema mgmt critique : breaking changes cassent les consumers","Outils SQL peu performants vs Parquet","Lib Python pas la plus polish (fastavro mieux que avro standard)") `
    -Links @("[[Parquet]] - columnar alternative","fastavro (Python) : https://github.com/fastavro/fastavro","Confluent Schema Registry") `
    -Url "https://avro.apache.org/" -Licence "Apache-2.0" -Langage "Java"

Write-Stub -Dir "Services/Data" -Name "Temporal" `
    -Categorie "data/workflow" -SubCat @("durable","workflow","saga","retry","event-sourcing") `
    -Alias @("temporal","temporal-io") -Tags @("service","workflow","durable","saga") `
    -Why "Plateforme de workflows durables. Tu ecris du code Python/Go/Java/TS comme un programme normal, Temporal s'occupe de la persistence d'etat, des retries, des timeouts, du recovery apres crash. Different des orchestrateurs data : concu pour microservices, sagas, processus metier longs (jours/mois)." `
    -WhenUse @("Microservices avec workflows longs (paiements, onboarding)","Sagas / compensation patterns","Retries intelligents (exponential backoff, idempotence)","Recovery apres crash / redemarrage","Approval workflows / human-in-the-loop") `
    -WhenNot @("Pipeline ETL pur data -> [[Prefect]] / [[Dagster]] / [[Airflow]]","Cron simple -> cron-job tout court","Pas de besoin durable -> asyncio + queue") `
    -Pitfalls @("Determinism mandate : pas de random/time dans workflows, side effects via Activities","Apprentissage SDK initial","Temporal Cloud cher, self-host = ops cluster","Versionning workflows : breaking changes complexes") `
    -Links @("[[Comparatif - Orchestrateurs data]]","Inngest, Trigger.dev - alternatives modernes","Restate (event-sourcing)","Hatchet (Postgres-based)") `
    -Url "https://temporal.io/" -Licence "MIT" -Langage "Go"

Write-Stub -Dir "Services/Data" -Name "Argo Workflows" `
    -Categorie "data/orchestrator" -SubCat @("kubernetes","workflow","cncf") `
    -Alias @("argo","argo-workflows") -Tags @("service","data","kubernetes","workflow") `
    -Why "Orchestrateur de workflows **Kubernetes-native** (CNCF). Definit workflows en CRD YAML, chaque step est un pod. Standard si tu es deja tout en K8s." `
    -WhenUse @("Stack Kubernetes existante","Workflows scientifiques / bioinformatique","CI/CD complexe sur K8s","Combo avec Argo CD / Events / Rollouts") `
    -WhenNot @("Pas de K8s -> [[Prefect]] / [[Dagster]] / [[Airflow]]","Python natif prefere -> orchestrateurs Python","Workflows < 100 tasks -> cron simple") `
    -Pitfalls @("YAML verbeux pour workflows complexes","DAG dynamique necessite WorkflowTemplate + recursion (pas trivial)","UI moins riche que les orchestrators Python","Resource limits par pod critiques") `
    -Links @("[[Comparatif - Orchestrateurs data]]","Argo CD (sister project, GitOps)","Tekton (alt CI/CD K8s)") `
    -Url "https://argo-workflows.readthedocs.io/" -Licence "Apache-2.0" -Langage "Go"

Write-Stub -Dir "Services/Data" -Name "Kestra" `
    -Categorie "data/orchestrator" -SubCat @("yaml","multi-language","orchestrator") `
    -Alias @("kestra") -Tags @("service","data","orchestrator","yaml") `
    -Why "Orchestrateur declaratif YAML, multi-langage (Python/JS/Shell/SQL/etc dans le meme workflow). UI moderne (web), event-driven, plugins riches. Alternative montee pour les equipes data non-Python." `
    -WhenUse @("Equipe polyglotte (pas que Python)","Workflows declaratifs versionnes Git","UI web pour business users","Event-driven (file detected, message Kafka, etc.)") `
    -WhenNot @("Stack Python pur -> [[Prefect]] / [[Dagster]]","Asset-centric ML -> [[Dagster]]","Complexite ETL > YAML -> Python natif mieux") `
    -Pitfalls @("YAML grossit vite sur workflows complexes","Ecosysteme plus jeune (vs Airflow 10+ ans)","Plugins variables en qualite") `
    -Links @("[[Comparatif - Orchestrateurs data]]","Mage (alt notebook-style)","Prefect / Dagster - alt Python") `
    -Url "https://kestra.io/" -Licence "Apache-2.0" -Langage "Java"

Write-Stub -Dir "Services/Data" -Name "Mage" `
    -Categorie "data/orchestrator" -SubCat @("notebook","data","orchestrator","python") `
    -Alias @("mage","mage-ai") -Tags @("service","data","orchestrator","notebook") `
    -Why "Orchestrateur Python avec UI notebook-style. Blocks = scripts Python qui se chainent en pipeline. Cible les data engineers / analystes qui aiment l'interactivite notebook." `
    -WhenUse @("Equipe avec background notebooks (Jupyter)","Pipelines moyens 10-100 blocks","Combo data ingestion + transform + export","Stack Python") `
    -WhenNot @("Production grosse echelle -> [[Airflow]] / [[Prefect]] / [[Dagster]]","Workflows complexes branches -> orchestrateurs avec graphes","Multi-langage -> [[Kestra]]") `
    -Pitfalls @("Notebook-style peut encourager mauvaise structuration","Ecosysteme modeste","Pas standard industrie (vs Airflow)") `
    -Links @("[[Comparatif - Orchestrateurs data]]","[[Prefect]] / [[Dagster]]") `
    -Url "https://www.mage.ai/" -Licence "Apache-2.0" -Langage "Python"

Write-Host "`nData done."
Write-Host "---"

# ?????????????????????????????????????????????????????????????????
# Document processing
# ?????????????????????????????????????????????????????????????????

Write-Stub -Dir "Services/Data" -Name "Marker" `
    -Categorie "data/document" -SubCat @("pdf","ocr","ml-extraction","table-extraction") `
    -Alias @("marker","marker-pdf") -Tags @("service","data","pdf","extraction") `
    -Why "Convertisseur PDF -> Markdown haute fidelite, base sur ML (modeles transformer). Excellent sur PDFs academiques (tables, equations), souvent meilleur que pdfplumber/PyMuPDF + Unstructured. Plus rapide que LlamaParse cloud sur certains cas." `
    -WhenUse @("PDFs scientifiques / techniques (tables, formules)","Pipeline RAG sur docs complexes","Local processing (privacy)","Conversion batch") `
    -WhenNot @("PDFs simples avec texte selectable -> pypdf / PyMuPDF suffit","Volumes massifs sans GPU -> LlamaParse cloud","Layout tres exotique -> Unstructured + post-processing") `
    -Pitfalls @("Modeles ML : besoin GPU pour throughput","Quality variable selon type de PDF","Lib jeune, breaking changes possibles") `
    -Links @("[[Docling]] - alt IBM","LlamaParse (cloud) : https://github.com/run-llama/llama_parse","PyMuPDF / pdfplumber - extraction simple") `
    -Url "https://github.com/VikParuchuri/marker" -Licence "GPL-3.0" -Langage "Python"

Write-Stub -Dir "Services/Data" -Name "Unstructured" `
    -Categorie "data/document" -SubCat @("pdf","docx","html","extraction","rag") `
    -Alias @("unstructured","unstructured-io") -Tags @("service","data","document","rag") `
    -Why "Library Python pour extraction de contenu structure depuis 25+ formats : PDF, DOCX, PPTX, HTML, emails, images. Standard pour ingestion RAG : sort des 'Elements' types (Title, NarrativeText, Table, etc.) facilement chunkables." `
    -WhenUse @("Pipeline RAG sur formats varies (mix PDF + DOCX + HTML)","Extraction structuree (titres, tables detectees separement)","Chunking element-aware","Cloud API (managed) pour scale") `
    -WhenNot @("PDF only -> [[Docling]] / Marker / PyMuPDF","Stack LlamaIndex -> LlamaParse integre","Simple : juste du texte -> tika / textract") `
    -Pitfalls @("Performance variable selon format / strategy (fast vs hi_res)","Hi-res necessite GPU + modeles","API cloud payante au volume","Deps lourdes (poppler, tesseract, etc.)") `
    -Links @("[[Docling]] - alt IBM","LlamaParse - cloud LLM-friendly","Marker - PDF scientifique") `
    -Url "https://unstructured.io/" -Licence "Apache-2.0" -Langage "Python"

Write-Stub -Dir "Services/Data" -Name "LlamaParse" `
    -Categorie "data/document" -SubCat @("pdf","cloud","rag","llm-extraction") `
    -Alias @("llamaparse","llama-parse") -Tags @("service","data","pdf","rag","cloud") `
    -Why "API cloud LlamaIndex pour parsing PDF/DOCX -> Markdown haute qualite, optimise RAG. Utilise des modeles LLM en interne pour structure / tables. Standard si tu utilises [[LlamaIndex]]." `
    -WhenUse @("PDFs complexes avec tables -> quality > local libs","Stack [[LlamaIndex]] integre","Pas envie de gerer modeles ML local","Batch volume modere") `
    -WhenNot @("Privacy / on-prem obligatoire -> Marker / [[Docling]] / Unstructured","Cout critique -> libs locales","Volume enorme -> cher au volume") `
    -Pitfalls @("Cloud only -> upload data sensitive","Pricing au volume (par page)","Rate limits","Latence cloud (~10-30s par PDF)") `
    -Links @("[[LlamaIndex]] - integration native","Marker - alt local","[[Docling]] - alt IBM") `
    -Url "https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/" -Licence "Proprietaire" -Langage ""

Write-Stub -Dir "Services/Data" -Name "pdfplumber" `
    -Categorie "data/document" -SubCat @("pdf","extraction","tables","python") `
    -Alias @("pdfplumber") -Tags @("service","data","pdf","python") `
    -Why "Lib Python d'extraction PDF : texte, **tables**, geometrie des elements. Tres bonne pour PDFs avec **tables** structurees. Plus simple que PyMuPDF pour ce use case." `
    -WhenUse @("Extraction de tables structurees de PDFs","Scripts d'extraction one-shot","Pas besoin de quality ML","Coordinate-aware extraction (bbox)") `
    -WhenNot @("Layout tres complexe -> Marker / Unstructured","Vitesse pure -> PyMuPDF (10x plus rapide)","Documents scannes (images) -> OCR + tools dedies") `
    -Pitfalls @("Plus lent que PyMuPDF","Tables avec cellules fusionnees : parfois rate","Pas de chunking/elements pour RAG natif") `
    -Links @("PyMuPDF - alt rapide","[[Unstructured]] - alt RAG-friendly","Camelot / Tabula - alt extraction tables") `
    -Url "https://github.com/jsvine/pdfplumber" -Licence "MIT" -Langage "Python"

Write-Stub -Dir "Services/Data" -Name "PyMuPDF" `
    -Categorie "data/document" -SubCat @("pdf","extraction","fast","python") `
    -Alias @("pymupdf","fitz") -Tags @("service","data","pdf","python") `
    -Why "Binding Python du moteur MuPDF (C). **Tres rapide** (10x+ pdfplumber), supporte PDF + EPUB + XPS. Standard pour extraction de masse." `
    -WhenUse @("Volume eleve (10k+ PDFs)","Extraction texte + images + metadonnees","Rendering pages -> images","Search + highlight dans PDFs") `
    -WhenNot @("Layout tables complexes -> pdfplumber / Camelot","RAG element-aware -> [[Unstructured]]","Quality ML transformer -> Marker") `
    -Pitfalls @("Licence AGPL pour version open (commercial license payante)","API moins Pythonic que pdfplumber","Pas de chunking/elements RAG out-of-box") `
    -Links @("pdfplumber - alt tables","[[Unstructured]] - alt RAG","[[Docling]]") `
    -Url "https://pymupdf.readthedocs.io/" -Licence "AGPL-3.0 / commercial" -Langage "Python/C"

Write-Host "`nDocs done."

# ?????????????????????????????????????????????????????????????????
# LLM serving / providers
# ?????????????????????????????????????????????????????????????????

Write-Stub -Dir "Services/LLM" -Name "Azure OpenAI" `
    -Categorie "llm/api" -SubCat @("api","llm","azure","openai-compat","enterprise") `
    -Alias @("azure-openai","aoai") -Tags @("service","llm","api","azure","enterprise") `
    -Why "OpenAI heberge sur Azure. Meme API, mais : deploiement par region (EU, etc.), compliance entreprise (SOC2, HIPAA, ISO), VNet isolation, contractualisation enterprise. Standard chez les grandes boites qui ont deja Azure." `
    -WhenUse @("Compliance / data residency EU","Stack Azure deja existante","SLA / support enterprise needed","Quotas dedies (Provisioned Throughput Units)") `
    -WhenNot @("Latest models day-zero -> OpenAI direct (lag Azure ~semaines)","Pricing pur -> souvent OpenAI direct moins cher","Multi-cloud / portabilite -> [[LiteLLM]] routes") `
    -Pitfalls @("API endpoints differents (`deployment_name` au lieu de `model`)","Versions modeles decalees vs OpenAI","Quotas regionaux limitatifs","Setup IAM complexe") `
    -Links @("[[OpenAI API]] - version directe","Bedrock - equivalent AWS","Vertex AI - equivalent GCP") `
    -Url "https://azure.microsoft.com/en-us/products/ai-services/openai-service" -Licence "Proprietaire" -Langage ""

Write-Stub -Dir "Services/LLM" -Name "Semantic Kernel" `
    -Categorie "llm/framework" -SubCat @("agent","framework","microsoft","dotnet","python") `
    -Alias @("semantic-kernel","sk") -Tags @("service","llm","framework","microsoft") `
    -Why "Framework d'orchestration LLM Microsoft. Plugins + planners + memory. Standard chez les boites .NET / Azure (existe aussi Python/Java). Comparable LangChain mais plus opinionated entreprise." `
    -WhenUse @("Stack .NET / Microsoft","Combo Azure OpenAI + Cosmos DB + Microsoft 365","Plugins natifs Microsoft Graph","Architecture entreprise opinionated") `
    -WhenNot @("Stack Python pure -> [[LangChain]] / [[LlamaIndex]] / [[DSPy]]","Pas d'ecosysteme Microsoft -> autres frameworks ont plus d'integrations","Production prouvee -> encore moins de retours que LangChain") `
    -Pitfalls @("Doc Python en retard sur .NET","Concepts (Kernel, Plugins) a apprendre","Lock-in Microsoft modere") `
    -Links @("[[LangChain]] / [[LlamaIndex]] - alt","[[AutoGen]] - autre Microsoft (multi-agent)") `
    -Url "https://learn.microsoft.com/en-us/semantic-kernel/" -Licence "MIT" -Langage "C# / Python / Java"

Write-Stub -Dir "Services/LLM" -Name "MLX" `
    -Categorie "llm/inference" -SubCat @("apple-silicon","local","metal","unified-memory") `
    -Alias @("mlx","mlx-lm") -Tags @("service","llm","apple","local") `
    -Why "Framework ML Apple optimise **Apple Silicon** (M-series). Memoire unifiee -> GPU peut adresser RAM totale (vs CUDA limitee VRAM). Standard pour LLM local sur Mac (mlx-lm), souvent **plus rapide que llama.cpp** sur M1/M2/M3/M4." `
    -WhenUse @("LLM local sur Mac Apple Silicon","Modeles 70B+ qui depassent VRAM CUDA mais tiennent en RAM unifiee","Fine-tuning local Mac","Inference rapide M-series") `
    -WhenNot @("Pas de Mac -> [[llama.cpp]] / [[Ollama]]","CUDA dispo -> [[PyTorch]] + [[vLLM]] meilleurs","Production server-side -> cloud APIs ou serveurs Linux") `
    -Pitfalls @("Mac only","Ecosysteme encore jeune (vs PyTorch)","Modeles a convertir au format MLX","Quantization moins mature") `
    -Links @("mlx-lm : https://github.com/ml-explore/mlx-lm","mlx-community (modeles) : https://huggingface.co/mlx-community","[[llama.cpp]] / [[Ollama]] - alt cross-platform","[[PyTorch]] - alt CUDA") `
    -Url "https://github.com/ml-explore/mlx" -Licence "MIT" -Langage "Python/C++"

Write-Stub -Dir "Services/LLM" -Name "SGLang" `
    -Categorie "llm/inference" -SubCat @("inference","serving","radix-attention") `
    -Alias @("sglang") -Tags @("service","llm","inference","serving") `
    -Why "Serveur LLM avec **RadixAttention** : prefix caching arbre radix, tres efficace pour requests partageant des prefixes (chatbot, RAG). Performance souvent superieure a [[vLLM]] sur ces cas. Frontend DSL Python pour structurer les prompts." `
    -WhenUse @("Apps avec shared prefixes massifs (chatbot multi-user, RAG)","Structured output via grammar","Multi-LoRA serving","Benchmarks throughput agressifs") `
    -WhenNot @("Stack vLLM mature -> migration couteuse","Modeles non supportes (toujours pas tout)","Petite echelle / dev -> [[Ollama]] suffit") `
    -Pitfalls @("Setup plus complexe que vLLM","Moins de modeles supportes","Doc moins mature","Frontend DSL a apprendre si on utilise") `
    -Links @("[[vLLM]] - alt mature","[[TGI]] - alt HuggingFace","TensorRT-LLM - alt NVIDIA") `
    -Url "https://github.com/sgl-project/sglang" -Licence "Apache-2.0" -Langage "Python"

Write-Stub -Dir "Services/LLM" -Name "TGI" `
    -Categorie "llm/inference" -SubCat @("inference","serving","huggingface","text-generation-inference") `
    -Alias @("tgi","text-generation-inference") -Tags @("service","llm","inference","huggingface") `
    -Why "Serveur d'inference LLM par Hugging Face. Container Docker production-ready, integration native HF Hub, support GGUF + GPTQ + AWQ + EETQ, continuous batching, prompt caching. Alternative production a vLLM, plus HF-natif." `
    -WhenUse @("Stack HuggingFace existante","Quantization AWQ / GPTQ / EETQ","Modeles HF Hub directement (zero config)","Combo Inference Endpoints HF managed") `
    -WhenNot @("Performance pure throughput -> [[vLLM]] souvent meilleur","Modeles custom non-HF -> autre","Apple Silicon -> [[MLX]] / llama.cpp") `
    -Pitfalls @("Licence change historique (HFOIL non-OSI 2023, retour Apache 2.0 fin 2023)","Moins de features bleeding-edge vs vLLM","Configs Docker env vars verbeuses") `
    -Links @("[[vLLM]] - alt principal","SGLang - alt RadixAttention","HuggingFace Inference Endpoints (managed)") `
    -Url "https://github.com/huggingface/text-generation-inference" -Licence "Apache-2.0" -Langage "Rust/Python"

Write-Stub -Dir "Services/LLM" -Name "TensorRT-LLM" `
    -Categorie "llm/inference" -SubCat @("inference","nvidia","tensorrt","optimization") `
    -Alias @("tensorrt-llm","trt-llm") -Tags @("service","llm","inference","nvidia") `
    -Why "Backend NVIDIA pour LLM serving optimise **H100/H200/B200**. Compile les modeles avec TensorRT -> meilleure latence et throughput sur GPU NVIDIA recents. Standard pour serving LLM sur infra NVIDIA enterprise (Triton Server + TensorRT-LLM)." `
    -WhenUse @("Infra NVIDIA H100/H200/B200","Latence critique (TTFT)","Quantization FP8/INT4 optimisee TensorRT","Combo [[NVIDIA Triton]] Inference Server") `
    -WhenNot @("Pas de NVIDIA recent -> [[vLLM]] / [[SGLang]]","Multi-vendor portable -> vLLM","Setup rapide -> vLLM 10x plus simple") `
    -Pitfalls @("Setup tres complexe (compile engines)","Lock-in NVIDIA hardware","Versions materielles + CUDA + TensorRT-LLM a matcher","Models supportes < vLLM") `
    -Links @("[[vLLM]] / [[SGLang]] - alt","[[NVIDIA Triton]] - combo recommande") `
    -Url "https://github.com/NVIDIA/TensorRT-LLM" -Licence "Apache-2.0" -Langage "Python/C++"

Write-Stub -Dir "Services/LLM" -Name "LM Studio" `
    -Categorie "llm/local" -SubCat @("local","gui","desktop","gguf") `
    -Alias @("lmstudio") -Tags @("service","llm","local","gui") `
    -Why "App desktop (Mac/Win/Linux) pour telecharger + run des LLMs locaux. GUI tres polish, serveur OpenAI-compatible local sur port 1234, supporte GGUF (llama.cpp) + MLX. Pour utilisateurs non-CLI." `
    -WhenUse @("Premiere install LLM local (UX accessible)","Tester des modeles GGUF sans setup","Hosting API locale OpenAI-compat pour dev","Mac MLX engine integre") `
    -WhenNot @("Production serveur -> [[vLLM]] / [[TGI]] / [[Ollama]]","Scripts CLI -> [[Ollama]] / [[llama.cpp]] direct","Multi-user concurrent -> mieux Ollama") `
    -Pitfalls @("App pas open-source (closed source, gratuit usage perso)","Pas de scripting natif (UI-first)","Update modeles via UI moins reproductible","Pas designed for headless server") `
    -Links @("[[Ollama]] - alt CLI/serveur","[[llama.cpp]] - backend low-level","[[MLX]] - Mac engine") `
    -Url "https://lmstudio.ai/" -Licence "Proprietaire (gratuit perso)" -Langage ""

Write-Stub -Dir "Services/LLM" -Name "text-generation-webui" `
    -Categorie "llm/local" -SubCat @("local","webui","gui","gradio") `
    -Alias @("text-generation-webui","oobabooga") -Tags @("service","llm","local","webui") `
    -Why "WebUI Gradio pour run LLMs locaux. Surnomme 'Oobabooga' (du nom du createur). Supporte plein de backends (transformers, llama.cpp, exllamav2, GGUF). Pour exploration interactive de modeles." `
    -WhenUse @("Exploration / RP / story telling local","Tester 10 modeles differents avec une seule UI","Backend swap dynamique (transformers <-> llama.cpp)","LoRA loading hot-swap") `
    -WhenNot @("Production -> [[vLLM]] / [[TGI]]","UX polish -> [[LM Studio]] (plus moderne)","CLI scripting -> [[Ollama]]","Multi-user concurrent -> autre stack") `
    -Pitfalls @("UI Gradio old-school","Dependencies lourdes (PyTorch + plusieurs backends)","Updates GitHub frequents -> breakages","Pas thread-safe vraiment") `
    -Links @("[[LM Studio]] - alt UI moderne","[[Ollama]] - alt CLI/serveur") `
    -Url "https://github.com/oobabooga/text-generation-webui" -Licence "AGPL-3.0" -Langage "Python"

Write-Host "`nLLM serving done."

# ?????????????????????????????????????????????????????????????????
# ML : tracking, HP search, feature store, serving
# ?????????????????????????????????????????????????????????????????

Write-Stub -Dir "Services/ML" -Name "Weights & Biases" `
    -Categorie "ml/tracking" -SubCat @("tracking","experiments","ml-ops","sweeps","artifacts") `
    -Alias @("wandb","w-and-b","weights-and-biases") -Tags @("service","ml","tracking","experiments") `
    -Why "Plateforme #1 de tracking d'experiences ML (cloud-first). Tres polish UX, sweeps (HP search), artifacts versioning, reports collaboratifs, Weave (observability LLM recente). Standard chez OpenAI, Anthropic, Stability, etc." `
    -WhenUse @("Tracking experiences ML / DL serieux","Sweeps (HP search avec Bayesian / grid)","Artifacts (versioning datasets + modeles)","Equipe collaborative (reports partages)","LLM observability (Weave)") `
    -WhenNot @("Self-host obligatoire -> [[MLflow]] (W&B Server = enterprise cher)","Budget zero -> MLflow open","Stack leger sans cloud -> [[Aim]] (open + light)") `
    -Pitfalls @("Cloud only par defaut (W&B Server = deal Enterprise)","Pricing volume peut surprendre","Lock-in modere (export possible mais friction)","Logging hooks peuvent slow down training (set freq)") `
    -Links @("[[MLflow]] - alt open self-host","[[Comet]] / [[Neptune]] / [[ClearML]] - alt cloud","Weave (W&B LLM) : https://weave.dev/") `
    -Url "https://wandb.ai/" -Licence "Proprietaire" -Langage ""

Write-Stub -Dir "Services/ML" -Name "Aim" `
    -Categorie "ml/tracking" -SubCat @("tracking","experiments","open-source","local") `
    -Alias @("aim") -Tags @("service","ml","tracking","open-source") `
    -Why "Tracker d'experiences ML **open-source** leger, full local. UI rapide, comparaison de runs intuitive. Standard de fait pour qui veut un W&B-like 100% open et self-host trivial." `
    -WhenUse @("ML perso / petit groupe sans cloud","Open-source obligatoire","Visualisations interactives rapides","Local-first (pas de upload data)") `
    -WhenNot @("Equipe grande, besoin SSO / RBAC -> [[MLflow]] / [[Weights & Biases]] Enterprise","Sweeps managed natifs -> [[Ray Tune]] / [[Optuna]] / W&B","Combo Models registry integre -> [[MLflow]]") `
    -Pitfalls @("Pas vraiment de cloud managed (full self-host)","Ecosysteme integrations moins riche","Pas de RBAC entreprise","Storage local peut grossir") `
    -Links @("[[MLflow]] / [[Weights & Biases]] / [[ClearML]] / [[Comet]] / [[Neptune]] - alt") `
    -Url "https://aimstack.io/" -Licence "Apache-2.0" -Langage "Python"

Write-Stub -Dir "Services/ML" -Name "ClearML" `
    -Categorie "ml/tracking" -SubCat @("tracking","ml-ops","experiments","orchestration") `
    -Alias @("clearml","allegro-clearml") -Tags @("service","ml","tracking","ml-ops") `
    -Why "Plateforme MLOps end-to-end : tracking + orchestration + serving + agents (workers). Open-source self-host genereux ou ClearML Cloud managed. Plus complet que MLflow, plus opinionated." `
    -WhenUse @("Stack MLOps complet self-host","Orchestration ML + tracking dans meme outil","Agents (workers distribues) pour training","Hyperparameter optimization integre") `
    -WhenNot @("Juste tracking -> [[MLflow]] / [[Aim]] plus leger","Orchestration data -> [[Prefect]] / [[Dagster]]","Stack LangChain LLM -> outils LLM dedies") `
    -Pitfalls @("Setup serveur lourd (MongoDB + Elasticsearch + Redis + service)","Concepts a apprendre (tasks, pipelines, agents)","Moins de retours communaute vs W&B / MLflow") `
    -Links @("[[MLflow]] / [[Weights & Biases]] / [[Aim]] / [[Comet]] / [[Neptune]]") `
    -Url "https://clear.ml/" -Licence "Apache-2.0" -Langage "Python"

Write-Stub -Dir "Services/ML" -Name "Comet" `
    -Categorie "ml/tracking" -SubCat @("tracking","experiments","cloud","opik") `
    -Alias @("comet","comet-ml") -Tags @("service","ml","tracking","cloud") `
    -Why "Tracker d'experiences cloud (avec self-host enterprise). Alternative directe a W&B. Recemment Opik = leur produit LLM observability (open-source)." `
    -WhenUse @("ML experience tracking cloud","Opik pour LLM observability (open MIT)","Stack favoris si gratuite ou pricing avantageux","Production registry / model card") `
    -WhenNot @("Open-source obligatoire (Comet ML lui-meme n'est pas open, seul Opik l'est) -> [[MLflow]] / [[Aim]]","Stack 100% W&B existant -> migration couteuse") `
    -Pitfalls @("Moins de momentum vs W&B (2024)","SSO et features avancees payantes","Doc inegale") `
    -Links @("Opik (LLM observ open) : https://github.com/comet-ml/opik","[[Weights & Biases]] / [[MLflow]] - alt") `
    -Url "https://www.comet.com/" -Licence "Proprietaire (Opik = Apache-2.0)" -Langage ""

Write-Stub -Dir "Services/ML" -Name "Neptune" `
    -Categorie "ml/tracking" -SubCat @("tracking","experiments","cloud","metadata-store") `
    -Alias @("neptune","neptune-ai") -Tags @("service","ml","tracking","cloud") `
    -Why "Tracker d'experiences cloud avec accent sur **metadata store** structure. Bon pour equipes qui veulent UI / collaboration sans setup. Plus 'data scientist friendly' que W&B selon certains avis." `
    -WhenUse @("Equipe DS qui veut UI claire sans setup","Metadata structurees (hierarchical) - pas juste metriques","Stack pas trop volumineuse (tier gratuit OK)","Reports collaboratifs") `
    -WhenNot @("Open-source obligatoire -> [[MLflow]] / [[Aim]]","Stack tres grande / orgs -> W&B / ClearML plus mature","Self-host non payant -> autres") `
    -Pitfalls @("Cloud only (self-host = Enterprise)","Pricing volume","Moins d'integrations que W&B/MLflow") `
    -Links @("[[Weights & Biases]] / [[MLflow]] / [[Aim]] / [[Comet]] / [[ClearML]]") `
    -Url "https://neptune.ai/" -Licence "Proprietaire" -Langage ""

Write-Stub -Dir "Services/ML" -Name "Hyperopt" `
    -Categorie "ml/hp-tuning" -SubCat @("hyperparameter","bayesian","tpe","search") `
    -Alias @("hyperopt") -Tags @("service","ml","hyperparameter","tuning") `
    -Why "Bibliotheque historique d'hyperparameter optimization Python. Algorithme phare : **TPE** (Tree-structured Parzen Estimator). Aujourd'hui largement supplantee par [[Optuna]] (UX bien meilleure) mais reste referencee." `
    -WhenUse @("Code legacy qui l'utilise deja","Algo TPE specifique (Optuna l'a aussi)","Combo MLflow tracking historique") `
    -WhenNot @("Nouveau projet -> [[Optuna]] (UX, pruning, dashboard meilleurs)","Distributed massif -> [[Ray Tune]]","Sweeps W&B / Comet -> leur propres outils") `
    -Pitfalls @("Maintenance modeste (vs Optuna tres actif)","API moins Pythonic","Pruning / early stopping pas natif") `
    -Links @("[[Optuna]] - alt moderne recommande","[[Ray Tune]] - alt distributed") `
    -Url "http://hyperopt.github.io/hyperopt/" -Licence "BSD-3-Clause" -Langage "Python"

Write-Stub -Dir "Services/ML" -Name "Feast" `
    -Categorie "ml/feature-store" -SubCat @("feature-store","ml-ops","online-store","offline-store") `
    -Alias @("feast","feast-feature-store") -Tags @("service","ml","feature-store") `
    -Why "Feature store open-source #1. Separe features offline (training, BigQuery/Snowflake) et online (serving, Redis/DynamoDB). Standard pour orgs ML matures qui veulent du **feature reuse** et de la **consistency train/serve**." `
    -WhenUse @("Plusieurs modeles partagent les memes features","Pipeline train/serve avec besoin consistency","Point-in-time correctness (eviter data leakage temporel)","Multiple data scientists qui reutilisent features") `
    -WhenNot @("1 modele / 1 use case -> over-engineering","Petite echelle -> pandas + Postgres suffit","Stack tres custom -> build maison") `
    -Pitfalls @("Setup lourd (online + offline stores + registry)","Concept feature view + entity a apprendre","Tecton (managed) cher","Doc parfois en retard sur le code") `
    -Links @("Tecton (managed Feast++) : https://www.tecton.ai/","Hopsworks - alt") `
    -Url "https://feast.dev/" -Licence "Apache-2.0" -Langage "Python"

Write-Stub -Dir "Services/ML" -Name "ArviZ" `
    -Categorie "ml/bayesian" -SubCat @("bayesian","visualization","diagnostics","pymc") `
    -Alias @("arviz") -Tags @("service","ml","bayesian","visualization") `
    -Why "Library Python pour **viz + diagnostics** de modeles bayesiens. Compatible PyMC, NumPyro, Stan, Pyro. Standard pour : trace plots, R-hat, ESS, posterior predictive checks. Indispensable avec [[PyMC]]." `
    -WhenUse @("Diagnostiquer convergence MCMC (R-hat, ESS, trace)","Posterior predictive checks","Comparaison modeles (LOO, WAIC)","Plots posterior (densites, forest plots)") `
    -WhenNot @("Pas de modele bayesien -> matplotlib/seaborn direct","Visualisation single-shot -> seaborn") `
    -Pitfalls @("Data formats : InferenceData object specifique","Performance sur tres gros traces","Plots customizable mais doc a creuser") `
    -Links @("[[PyMC]] - combo classique","[[MCMC]] (concept)","Stan / NumPyro / Pyro - compatibles aussi") `
    -Url "https://www.arviz.org/" -Licence "Apache-2.0" -Langage "Python"

Write-Stub -Dir "Services/ML" -Name "Seldon Core" `
    -Categorie "ml/serving" -SubCat @("serving","kubernetes","cncf","mlops") `
    -Alias @("seldon","seldon-core") -Tags @("service","ml","serving","kubernetes") `
    -Why "Plateforme de model serving Kubernetes-native (CNCF). Multi-framework (sklearn, XGBoost, PyTorch, TF, ONNX). Inference graphs (chainer modeles + transformers + routing). Plus avance que KServe sur les inference graphs." `
    -WhenUse @("Stack Kubernetes existante","Inference graphs complexes (A/B test, shadow, ensemble)","Multi-framework hosting","SeldonDeployment CRD + monitoring integre") `
    -WhenNot @("Pas de K8s -> [[BentoML]] / [[Ray Serve]] / cloud managed","Single model simple -> torchserve / [[NVIDIA Triton]] / cloud","LLM serving -> [[vLLM]] / [[TGI]] / [[SGLang]]") `
    -Pitfalls @("Setup K8s + Istio (selon version) lourd","Apprentissage CRDs Seldon","Licence Seldon Core v2 (2024) = BSL non-OSI (verifier)") `
    -Links @("KServe - alt CNCF lighter","[[BentoML]] / [[Ray Serve]] - alt non-K8s","[[NVIDIA Triton]]") `
    -Url "https://www.seldon.io/" -Licence "BSL" -Langage "Python/Go"

Write-Stub -Dir "Services/ML" -Name "KServe" `
    -Categorie "ml/serving" -SubCat @("serving","kubernetes","cncf","kubeflow") `
    -Alias @("kserve","kfserving") -Tags @("service","ml","serving","kubernetes") `
    -Why "Standard CNCF de model serving Kubernetes-native (anciennement KFServing). InferenceService CRD, auto-scaling KNative, multi-framework. Plus simple que Seldon Core, ne couvre pas les inference graphs avances." `
    -WhenUse @("Stack Kubeflow / Kubernetes","Auto-scale to zero (KNative)","Multi-framework (sklearn, XGBoost, PyTorch, TF, ONNX)","Standard ouvert non-vendor") `
    -WhenNot @("Pas de K8s -> [[BentoML]] / [[Ray Serve]] / cloud","Inference graphs complexes -> [[Seldon Core]]","LLM serving -> [[vLLM]] / [[TGI]]") `
    -Pitfalls @("Setup K8s + KNative + Istio lourd","Doc moins riche que Seldon","Cold start (scale to zero) latence") `
    -Links @("[[Seldon Core]] - alt plus complet","[[Kubeflow]] - combo classique","[[BentoML]] - alt non-K8s") `
    -Url "https://kserve.github.io/website/" -Licence "Apache-2.0" -Langage "Python/Go"

Write-Stub -Dir "Services/ML" -Name "TensorFlow Serving" `
    -Categorie "ml/serving" -SubCat @("serving","tensorflow","grpc","savedmodel") `
    -Alias @("tf-serving","tfserving") -Tags @("service","ml","serving","tensorflow") `
    -Why "Serveur d'inference officiel TensorFlow. Mature, optimise pour SavedModel, gRPC + REST. Versioning de modeles natif. Standard si tu sers du TF en prod." `
    -WhenUse @("Modeles TF / Keras 3 en prod","gRPC pour latence basse","Versioning multi-modele","Hot reload SavedModel sans downtime") `
    -WhenNot @("Modeles PyTorch -> [[TorchServe]] / vLLM / Triton","Multi-framework -> [[NVIDIA Triton]] / [[BentoML]]","LLM transformers -> vLLM / TGI") `
    -Pitfalls @("TF-only","Setup Docker / batching configs","Logging gRPC moins amical que REST","Pas de KServe inference graphs") `
    -Links @("[[NVIDIA Triton]] - alt multi-framework","[[TorchServe]] - alt PyTorch") `
    -Url "https://www.tensorflow.org/tfx/guide/serving" -Licence "Apache-2.0" -Langage "C++"

Write-Stub -Dir "Services/ML" -Name "TorchServe" `
    -Categorie "ml/serving" -SubCat @("serving","pytorch","mar","model-archive") `
    -Alias @("torchserve") -Tags @("service","ml","serving","pytorch") `
    -Why "Serveur d'inference officiel PyTorch (Meta + AWS). Standard pour servir des modeles PyTorch en prod. Plus simple que vLLM/Triton mais moins optimise pour LLM transformer." `
    -WhenUse @("PyTorch models en prod (CV, ASR, recsys, NLP non-LLM)","Multi-modele hosting","Combo SageMaker (image officielle)","Metrics Prometheus natifs") `
    -WhenNot @("LLM transformers -> [[vLLM]] / [[TGI]] / [[SGLang]] (specialises)","Multi-framework -> [[NVIDIA Triton]] / [[BentoML]]","TensorFlow -> [[TensorFlow Serving]]") `
    -Pitfalls @("MAR (Model Archive) format a comprendre","Maintenance modeste depuis 2023","Pas optimise pour throughput LLM (batching primitif)") `
    -Links @("[[NVIDIA Triton]] - alt multi","[[BentoML]] - alt Python-friendly","[[vLLM]] - alt LLM-specialise") `
    -Url "https://pytorch.org/serve/" -Licence "Apache-2.0" -Langage "Python/Java"

Write-Host "`nML done."

# ?????????????????????????????????????????????????????????????????
# Tooling: viz, distributed, config, stats, package
# ?????????????????????????????????????????????????????????????????

Write-Stub -Dir "Services/Tooling" -Name "Modin" `
    -Categorie "tooling/dataframe" -SubCat @("pandas","distributed","drop-in") `
    -Alias @("modin","modin-project") -Tags @("service","python","dataframe","distributed") `
    -Why "**Drop-in replacement pandas** : `import modin.pandas as pd` -> tes scripts utilisent automatiquement Ray ou Dask en backend. Magique en theorie, en pratique [[Polars]] est souvent meilleur choix pour la perf single-node." `
    -WhenUse @("Code pandas legacy massif -> swap 1 ligne d'import","Ray cluster deja existant","Tu veux tester sans refactor") `
    -WhenNot @("Greenfield projet -> [[Polars]] (10x plus rapide, syntax meilleure)","Tu peux refactor -> Polars vaut le coup","Petites donnees -> pandas suffit") `
    -Pitfalls @("Pas 100% pandas compatible (certains ops non couverts)","Performance variable selon ops","Overhead distributed si donnees petites") `
    -Links @("[[Polars]] - alt recommandee","[[Dask]] - alt explicite","[[pandas]]") `
    -Url "https://modin.readthedocs.io/" -Licence "Apache-2.0" -Langage "Python"

Write-Stub -Dir "Services/Tooling" -Name "CuPy" `
    -Categorie "tooling/numpy" -SubCat @("numpy","gpu","cuda","drop-in") `
    -Alias @("cupy") -Tags @("service","python","numpy","gpu") `
    -Why "**Drop-in replacement numpy** sur GPU NVIDIA. `import cupy as cp` -> arrays sur GPU avec API numpy. Pour calcul scientifique GPU sans passer a PyTorch/JAX." `
    -WhenUse @("Calcul scientifique numpy massif sur GPU","Code numpy existant -> port GPU rapide","Combo numba / RAPIDS","Pas besoin autograd ([[PyTorch]] alors)") `
    -WhenNot @("Pas de NVIDIA -> numpy direct","Besoin autograd -> [[PyTorch]] / [[JAX]]","Apple Silicon -> [[MLX]]") `
    -Pitfalls @("CUDA versions matching","Memory management explicit (`free_all_blocks`)","Pas 100% numpy compatible (certaines fonctions niche manquent)") `
    -Links @("RAPIDS (cuDF, cuML) : https://rapids.ai/","[[PyTorch]] - alt avec autograd","[[JAX]] - alt fonctionnel") `
    -Url "https://cupy.dev/" -Licence "MIT" -Langage "Python/CUDA"

Write-Stub -Dir "Services/Tooling" -Name "python-dotenv" `
    -Categorie "tooling/config" -SubCat @("config","env-vars","secrets","dotenv") `
    -Alias @("python-dotenv","dotenv") -Tags @("service","python","config","env-vars") `
    -Why "Charge variables depuis un fichier `.env` vers `os.environ`. Standard de fait pour dev Python (combine avec [[Pydantic]] Settings ou [[FastAPI]] config)." `
    -WhenUse @("Dev local (DATABASE_URL, API_KEY dans .env)","Secrets en local (.env dans .gitignore)","12-factor app config") `
    -WhenNot @("Production cloud -> vrai secret manager (AWS Secrets Manager, Vault, etc.)","Config riche / typee -> [[Pydantic]] Settings (qui peut lire .env aussi)","Multi-env complex -> hydra / dynaconf") `
    -Pitfalls @("Quotes vs no quotes dans .env (differentes libs interpretent differemment)","Multi-line values delicats","Pas typed (tout string)","Commit accidentel de .env (toujours dans .gitignore)") `
    -Links @("[[Pydantic]] Settings (combo recommande)","hydra (Facebook) - alt riche","dynaconf - alt multi-env") `
    -Url "https://github.com/theskumar/python-dotenv" -Licence "BSD-3-Clause" -Langage "Python"

Write-Stub -Dir "Services/Tooling" -Name "hydra" `
    -Categorie "tooling/config" -SubCat @("config","yaml","facebook","ml-experiments","composition") `
    -Alias @("hydra","hydra-core") -Tags @("service","python","config","ml") `
    -Why "Framework de config Facebook (Meta) pour ML experimental. Composition de configs YAML, override CLI, multi-runs (grid sweep). Tres utilise en recherche DL." `
    -WhenUse @("Experiences ML avec nombreuses configs (modeles + datasets + optimizers)","Multi-runs sweeps (CLI override `model=resnet50 lr=0.01,0.001`)","Reproductibilite config (Hydra save config snapshot)","Stack Fairseq / Detectron2 / etc.") `
    -WhenNot @("App production / web -> [[Pydantic]] Settings","Config simple -> python-dotenv","Pas besoin de composition -> over-engineering") `
    -Pitfalls @("Magic / decorators @hydra.main -> debug peut surprendre","CWD changes par defaut (option `hydra.job.chdir=false`)","OmegaConf concepts (interpolation, structured configs)","Lock-in modere") `
    -Links @("OmegaConf (foundation Hydra) : https://omegaconf.readthedocs.io/","[[Pydantic]] Settings - alt typed","dynaconf - alt multi-env") `
    -Url "https://hydra.cc/" -Licence "MIT" -Langage "Python"

Write-Stub -Dir "Services/Tooling" -Name "dynaconf" `
    -Categorie "tooling/config" -SubCat @("config","multi-env","secrets","python") `
    -Alias @("dynaconf") -Tags @("service","python","config","multi-env") `
    -Why "Lib de config Python multi-env (dev/staging/prod). Supports TOML/YAML/JSON/INI/.env + Vault / Redis / Postgres backends. Validation + lazy loading + cli + Flask/Django plugins." `
    -WhenUse @("Multi-env serieux (.env + secrets distants)","Vault / Redis comme backend secrets","Flask / Django app avec config rich","CLI overrides + env vars combines") `
    -WhenNot @("ML experiments -> hydra","Simple -> python-dotenv + Pydantic Settings","FastAPI moderne -> [[Pydantic]] Settings natif") `
    -Pitfalls @("API plus complexe que python-dotenv","Magic attributes (`settings.FOO` typing)","Doc parfois lacunaire sur edge cases","Moins de momentum 2024+") `
    -Links @("[[Pydantic]] Settings - alt typed moderne","python-dotenv - alt simple","hydra - alt ML") `
    -Url "https://www.dynaconf.com/" -Licence "MIT" -Langage "Python"

Write-Stub -Dir "Services/Tooling" -Name "pingouin" `
    -Categorie "tooling/stats" -SubCat @("stats","statistical-tests","python") `
    -Alias @("pingouin") -Tags @("service","python","stats") `
    -Why "Library Python de **tests statistiques** : t-tests, ANOVA, correlations, Bayes factors, mixed models. Wrapper elegant sur scipy.stats + statsmodels, sorties pandas-friendly avec effect sizes inclus." `
    -WhenUse @("Analyse stats reproductible (sciences sociales, medical)","Effect sizes necessaires (Cohen d, Hedges g)","Tests Bayesian de comparaison","Tests sur DataFrames pandas direct") `
    -WhenNot @("Pure modeling -> [[statsmodels]] (plus complet GLM, time series)","ML -> [[scikit-learn]]","R workflow -> pingouin moins riche que R packages") `
    -Pitfalls @("Moins de tests que statsmodels","Bayes factors limites","Maintenance modeste (1 dev principal)") `
    -Links @("[[statsmodels]] - alt riche","scipy.stats - bas niveau","[[Hypothesis testing]] (concept)") `
    -Url "https://pingouin-stats.org/" -Licence "GPL-3.0" -Langage "Python"

Write-Stub -Dir "Services/Tooling" -Name "scipy.stats" `
    -Categorie "tooling/stats" -SubCat @("stats","scipy","statistical-tests","distributions") `
    -Alias @("scipy-stats","scipy.stats") -Tags @("service","python","stats","scipy") `
    -Why "Module statistique de [SciPy](https://scipy.org/) : distributions (Normal, Beta, Gamma, etc.), tests classiques (t-test, ANOVA, Chi?, KS, Mann-Whitney), correlations, descriptive stats. **Standard bas niveau** pour stats en Python. Bricks de pingouin et statsmodels." `
    -WhenUse @("Tests statistiques de base (t-test, Chi?)","Sampling depuis distributions","Stats descriptives","Brique de calcul scientifique") `
    -WhenNot @("Modeling complexe (GLM, time series) -> [[statsmodels]]","Analyse reproductible avec effect sizes -> pingouin","Bayesian -> [[PyMC]] / ArviZ") `
    -Pitfalls @("API inconsistante (anciennes vs nouvelles fonctions)","Pas d'effect sizes natifs","Documentation academique parfois opaque") `
    -Links @("pingouin - wrapper haut niveau","[[statsmodels]] - modeling complet","[[Hypothesis testing]] / [[t-test and ANOVA]] / [[Chi-squared tests]] (concepts)") `
    -Url "https://docs.scipy.org/doc/scipy/reference/stats.html" -Licence "BSD-3-Clause" -Langage "Python"

Write-Stub -Dir "Services/Tooling" -Name "pip" `
    -Categorie "tooling/package-manager" -SubCat @("python","package-manager","installer") `
    -Alias @("pip") -Tags @("service","python","packaging") `
    -Why "Gestionnaire de paquets officiel Python. Universellement disponible, mais **lent et limite** par rapport aux alternatives modernes ([[uv]]). Reste le standard bas niveau (utilise par tous les autres outils en interne)." `
    -WhenUse @("Outil universel disponible partout","Install rapide one-off (`pip install foo`)","Compat scripts existants","Si pas le choix") `
    -WhenNot @("Projets serieux 2026 -> [[uv]] (10-100x plus rapide, gere venv + lockfile + Python install)","Multi-env workflow -> uv / pipx / poetry") `
    -Pitfalls @("Pas de lockfile natif (besoin pip-tools / pip freeze)","Resolution lente sur dependencies complexes","Pas de Python version management","Verbosite (creer venv + activate + pip install separe)") `
    -Links @("[[uv]] - successeur recommande","pipx - install isole CLI tools","pip-tools (pip-compile + pip-sync)") `
    -Url "https://pip.pypa.io/" -Licence "MIT" -Langage "Python"

Write-Stub -Dir "Services/Tooling" -Name "bokeh" `
    -Categorie "tooling/viz" -SubCat @("visualization","interactive","web","python") `
    -Alias @("bokeh") -Tags @("service","python","viz","interactive") `
    -Why "Library de visualisation interactive Python pour le web. Plots JS-backed (bokehjs), embedable HTML, server pour dashboards. Concurrent direct de [[plotly]], moins polish mais full-stack ouvert." `
    -WhenUse @("Dashboards interactifs custom","Plots web embedable","Visualisations tres grandes (10M+ points, datashader)","Combo Panel pour apps") `
    -WhenNot @("Notebooks / static -> matplotlib / seaborn","Polish ready-made -> [[plotly]]","Apps prod -> Streamlit / Gradio") `
    -Pitfalls @("API plus verbose que plotly","Doc moins claire","Communaute plus petite","Server (panel) complexe a setup") `
    -Links @("[[plotly]] / [[matplotlib]] - alt","Panel (apps) - sister project","datashader - combo big data viz") `
    -Url "https://bokeh.org/" -Licence "BSD-3-Clause" -Langage "Python"

Write-Stub -Dir "Services/Tooling" -Name "altair" `
    -Categorie "tooling/viz" -SubCat @("visualization","grammar-of-graphics","vega-lite","python") `
    -Alias @("altair","altair-viz") -Tags @("service","python","viz","grammar") `
    -Why "Library de viz Python **declarative** basee sur Vega-Lite (grammaire des graphiques). Code concis (`chart.encode(x='date', y='value')`). Excellent pour exploration et analyses propres avec syntax claire." `
    -WhenUse @("Analyse exploratoire avec code propre / lisible","Stats / data science : composition de visualisations","Combo Streamlit (Altair charts natifs)","Apprentissage grammaire des graphiques") `
    -WhenNot @("Plots complexes custom -> [[plotly]] / [[matplotlib]]","Animation / temps reel -> bokeh / plotly","Tres gros volumes (>5k points) -> datashader / vega-lite plain") `
    -Pitfalls @("Limite ~5000 rows par defaut (configurable)","JSON Vega-Lite spec parfois opaque pour debug","Moins de plugins / extensions") `
    -Links @("Vega-Lite (foundation) : https://vega.github.io/vega-lite/","[[plotly]] / [[bokeh]] / [[matplotlib]]","ggplot2 (R) - equivalent grammar") `
    -Url "https://altair-viz.github.io/" -Licence "BSD-3-Clause" -Langage "Python"

Write-Stub -Dir "Services/Tooling" -Name "seaborn" `
    -Categorie "tooling/viz" -SubCat @("visualization","matplotlib","statistical","python") `
    -Alias @("seaborn") -Tags @("service","python","viz","stats") `
    -Why "Wrapper haut niveau sur [[matplotlib]] pour **viz statistiques**. Defaults beaux, syntax pandas-friendly, plots distribution / regression / correlation en 1 ligne. Standard pour analyse exploratoire DS." `
    -WhenUse @("Exploration de donnees stats (boxplot, violin, heatmap, pairplot)","Quick stats viz dans notebook","Defaults beaux sans tuning matplotlib","Combos pandas natif") `
    -WhenNot @("Interactivite -> [[plotly]] / [[bokeh]] / altair","Apps web -> frameworks ad-hoc","Custom heavy -> matplotlib direct") `
    -Pitfalls @("Reecrit en v0.12+ : `seaborn.objects` (interface declarative) vs functional historique","Performance sur gros datasets","Configuration globale matplotlib parfois en conflit") `
    -Links @("[[matplotlib]] - foundation","altair / [[plotly]] - alt interactive") `
    -Url "https://seaborn.pydata.org/" -Licence "BSD-3-Clause" -Langage "Python"

Write-Host "`nTooling done."

# ?????????????????????????????????????????????????????????????????
# UI / Web app
# ?????????????????????????????????????????????????????????????????

Write-Stub -Dir "Services/UI" -Name "Dash" `
    -Categorie "ui/dashboard" -SubCat @("dashboard","plotly","web-app","python") `
    -Alias @("dash","plotly-dash") -Tags @("service","ui","dashboard","python") `
    -Why "Framework dashboard Python par Plotly. Apps web full Python (callbacks reactifs), no JS. Cible analytics dashboards entreprise. Plus structure que Streamlit, plus puissant pour apps complexes." `
    -WhenUse @("Dashboards analytics complexes (multi-page, layouts custom)","Combo [[plotly]] (integration native)","Apps metier internes Python-only","Plotly Enterprise existant") `
    -WhenNot @("App rapide < 100 lignes -> [[Streamlit]] / [[Gradio]]","UI mobile-first -> autres","Open-source full -> Streamlit / Gradio communaute plus active") `
    -Pitfalls @("Callback pattern a apprendre (Inputs/Outputs)","State management plus dur que Streamlit","Dash Enterprise payant pour features avancees (Snapshot Engine, App Manager)") `
    -Links @("[[Streamlit]] / [[Gradio]] - alt","[[plotly]] - combo natif") `
    -Url "https://dash.plotly.com/" -Licence "MIT" -Langage "Python"

Write-Stub -Dir "Services/UI" -Name "Shiny for Python" `
    -Categorie "ui/dashboard" -SubCat @("dashboard","reactive","posit","python","web-app") `
    -Alias @("shiny","shiny-python","py-shiny") -Tags @("service","ui","dashboard","python") `
    -Why "Port Python de Shiny R (Posit / RStudio). Modele reactif : recompute UI quand inputs changent. Plus structure que [[Streamlit]] (callbacks explicites), proche de [[Dash]] philosophiquement." `
    -WhenUse @("Background R / Shiny -> migration vers Python familiere","Apps reactives complexes (graphs dynamiques)","Stack Posit (Posit Connect / Cloud)","Modele reactif explicite prefere") `
    -WhenNot @("Quick prototype -> [[Streamlit]] / [[Gradio]]","Pas familier Shiny -> courbe d'apprentissage","Communaute plus active -> Streamlit / Gradio") `
    -Pitfalls @("Plus jeune que Shiny R","Doc parfois R-centric","Posit Connect (managed deploy) payant") `
    -Links @("[[Streamlit]] / [[Gradio]] / [[Dash]] - alt") `
    -Url "https://shiny.posit.co/py/" -Licence "MIT" -Langage "Python"

Write-Host "`nUI done."

# ?????????????????????????????????????????????????????????????????
# VectorDB (ANN libraries)
# ?????????????????????????????????????????????????????????????????

Write-Stub -Dir "Services/VectorDB" -Name "Annoy" `
    -Categorie "vectordb/ann" -SubCat @("ann","approximate","spotify","trees") `
    -Alias @("annoy") -Tags @("service","vectordb","ann","python") `
    -Why "Library ANN (Approximate Nearest Neighbors) par Spotify, basee sur des arbres aleatoires (RP-trees). Standard historique avant HNSW. Read-only apres build, tres rapide en lecture, immutable." `
    -WhenUse @("Index read-only (build une fois, query apres)","Memory-mapped (lecture sans charger en RAM)","Stable historique chez Spotify (recsys)","Simple a integrer") `
    -WhenNot @("Updates frequentes -> HNSW / [[Qdrant]] / [[Weaviate]]","Filtering structure -> vraies vector DBs","High recall sur low latency -> HNSW mieux","Production moderne -> [[Faiss]] / [[hnswlib]]") `
    -Pitfalls @("Pas d'add apres build (re-build complet)","Performance moins bonne que HNSW","Pas de filtering","Maintenance modeste") `
    -Links @("[[Faiss]] - alt principal","hnswlib - alt HNSW pur","[[Qdrant]] / [[Weaviate]] - full vector DB") `
    -Url "https://github.com/spotify/annoy" -Licence "Apache-2.0" -Langage "C++/Python"

Write-Stub -Dir "Services/VectorDB" -Name "hnswlib" `
    -Categorie "vectordb/ann" -SubCat @("ann","hnsw","approximate","library") `
    -Alias @("hnswlib") -Tags @("service","vectordb","ann","hnsw") `
    -Why "Implementation de reference de l'algo HNSW (Hierarchical Navigable Small World). C++ + bindings Python. Tres rapide, mature, sous-jacent a beaucoup de vector DBs ([[Qdrant]], [[Weaviate]], pgvector v0.5+)." `
    -WhenUse @("Tu veux HNSW pur dans ton process Python","Embedded ANN (pas de serveur)","Combo numpy -> recherche rapide","Update + query (HNSW supporte add incremental)") `
    -WhenNot @("Filtering / metadata -> [[Qdrant]] / [[Weaviate]] / pgvector","Multi-tenant -> vraies vector DBs","Distributed scale-out -> Milvus") `
    -Pitfalls @("Memory full RAM (pas de disk-based)","Params M / ef a tuner","Pas de filtering structure","Sauvegarde / load index manuel") `
    -Links @("[[Faiss]] / [[Qdrant]] / [[Weaviate]] - alt","pgvector v0.5+ utilise HNSW","Paper HNSW : https://arxiv.org/abs/1603.09320") `
    -Url "https://github.com/nmslib/hnswlib" -Licence "Apache-2.0" -Langage "C++/Python"

Write-Stub -Dir "Services/VectorDB" -Name "ScaNN" `
    -Categorie "vectordb/ann" -SubCat @("ann","google","approximate","quantization") `
    -Alias @("scann") -Tags @("service","vectordb","ann","google") `
    -Why "ANN library Google avec **vector quantization** (asymmetric quantization). Tres bonne perf a recall equivalent vs HNSW. Bas niveau, moins de wrappers haut niveau. Utilise en interne par Vertex AI Matching Engine." `
    -WhenUse @("Recall critique sur very large indices (100M+)","Vertex AI Matching Engine (Google cloud)","Research / benchmarks ANN avance") `
    -WhenNot @("Setup rapide -> [[Faiss]] / hnswlib / [[Qdrant]]","Cross-platform (ScaNN Linux + GPU primairement)","Production ops simple -> Vector DB managed") `
    -Pitfalls @("API moins amicale que Faiss / hnswlib","Build / install parfois douloureux","Doc clairsemee") `
    -Links @("[[Faiss]] / hnswlib - alt mainstream","Vertex AI Matching Engine - managed Google","Paper ScaNN : https://arxiv.org/abs/1908.10396") `
    -Url "https://github.com/google-research/google-research/tree/master/scann" -Licence "Apache-2.0" -Langage "C++/Python"

Write-Host "`nVectorDB done."

# ?????????????????????????????????????????????????????????????????
# Observability (Grafana, Loki)
# ?????????????????????????????????????????????????????????????????

# Create Observability dir if needed
$obsDir = Join-Path $root "Services/Observability"
if (-not (Test-Path $obsDir)) { New-Item -ItemType Directory -Path $obsDir | Out-Null }

Write-Stub -Dir "Services/Observability" -Name "Grafana" `
    -Categorie "observability/dashboard" -SubCat @("monitoring","metrics","dashboard","visualization") `
    -Alias @("grafana") -Tags @("service","observability","monitoring","metrics") `
    -Why "Plateforme de **dashboards observability** open-source. Multi-datasource (Prometheus, Loki, InfluxDB, Postgres, CloudWatch, etc.). Standard pour monitoring infra + applis. Grafana Labs vend aussi cloud / enterprise." `
    -WhenUse @("Dashboards multi-sources","Visualiser Prometheus metrics","Combo Loki (logs) + Tempo (tracing) = stack LGTM Grafana","Alertes (Grafana Alerting unifie)") `
    -WhenNot @("Dashboards LLM-specific -> [[Langfuse]] / [[Helicone]] dedies","Setup simple sans Prometheus -> cloud-native (Datadog, etc.)","Logs structured -> Kibana (Elastic stack)") `
    -Pitfalls @("Versions OSS vs Enterprise (Grafana 11+ : licence AGPLv3)","Dashboards complexes : JSON export/import","Plugins inegaux qualite","Setup auth (LDAP / OIDC) verbeux") `
    -Links @("Prometheus (datasource principal) : https://prometheus.io/","[[Loki]] - combo logs Grafana Labs","Tempo - tracing","Datadog (alt commercial)") `
    -Url "https://grafana.com/" -Licence "AGPL-3.0 (OSS)" -Langage "Go"

Write-Stub -Dir "Services/Observability" -Name "Loki" `
    -Categorie "observability/logs" -SubCat @("logs","grafana-labs","aggregation") `
    -Alias @("loki","grafana-loki") -Tags @("service","observability","logs") `
    -Why "Systeme d'aggregation de logs par Grafana Labs. Indexe **labels** (pas le contenu), donc plus economique que Elasticsearch. Standard de la stack LGTM (Loki + Grafana + Tempo + Mimir)." `
    -WhenUse @("Stack Grafana existante","Volumes logs gros (economie disque vs ES)","Combo Kubernetes + Promtail/Alloy","Tail logs en live via Grafana") `
    -WhenNot @("Full-text search rapide -> Elasticsearch / OpenSearch","Logs simples -> Cloud-native (CloudWatch Logs, GCP Cloud Logging)","Audit / compliance riche -> solutions dediees") `
    -Pitfalls @("Pas de full-text search rapide (LogQL filtre seulement)","Cardinality labels critique (trop = lent)","Setup retention / compaction a comprendre","Alloy (anciennement Promtail) a integrer") `
    -Links @("[[Grafana]] - combo natif","Elasticsearch / OpenSearch - alt full-text") `
    -Url "https://grafana.com/oss/loki/" -Licence "AGPL-3.0" -Langage "Go"

Write-Host "`nObservability done."
Write-Host ""
Write-Host "===================================="
Write-Host "Generation terminee."
Write-Host "===================================="
