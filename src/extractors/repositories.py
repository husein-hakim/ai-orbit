# src/extractors/repositories.py
import urllib.request
import json
from src.normalizer import normalize

SEED_REPOSITORIES = [
    {
        "name": "langchain-ai/langchain",
        "description": "LangChain is a widely adopted open-source orchestration framework for developing context-aware applications powered by large language models. It provides composable primitives for prompt chaining, agentic tool invocation, and multi-source document retrieval.",
        "url": "https://github.com/langchain-ai/langchain",
        "github_stars": 98000,
        "primary_language": "Python",
        "last_updated": "2026-09",
        "topics": ["llm", "agents", "rag", "orchestration"],
        "license": "MIT",
        "forks": 16000
    },
    {
        "name": "run-llama/llama_index",
        "description": "LlamaIndex is an enterprise data framework designed to ingest, structure, and access private or domain-specific data for LLM applications. It offers sophisticated document parsing, hierarchical indexing algorithms, and automated query engines for production RAG systems.",
        "url": "https://github.com/run-llama/llama_index",
        "github_stars": 38000,
        "primary_language": "Python",
        "last_updated": "2026-09",
        "topics": ["rag", "data-framework", "vector-search", "knowledge-base"],
        "license": "MIT",
        "forks": 4800
    },
    {
        "name": "vllm-project/vllm",
        "description": "vLLM is a high-throughput and memory-efficient serving engine for large language models based on PagedAttention memory management. It drastically reduces GPU memory fragmentation, delivering up to 24x higher serving throughput compared to standard Hugging Face implementations.",
        "url": "https://github.com/vllm-project/vllm",
        "github_stars": 36000,
        "primary_language": "Python",
        "last_updated": "2026-09",
        "topics": ["llm-serving", "paged-attention", "inference", "gpu-optimization"],
        "license": "Apache-2.0",
        "forks": 5200
    },
    {
        "name": "huggingface/transformers",
        "description": "Transformers provides thousands of pretrained models to perform tasks on texts, vision, and audio for developers and researchers worldwide. It constitutes the core backbone of the modern machine learning ecosystem, supporting PyTorch, TensorFlow, and JAX backends.",
        "url": "https://github.com/huggingface/transformers",
        "github_stars": 135000,
        "primary_language": "Python",
        "last_updated": "2026-09",
        "topics": ["deep-learning", "pytorch", "transformers", "nlp"],
        "license": "Apache-2.0",
        "forks": 26000
    },
    {
        "name": "ollama/ollama",
        "description": "Ollama is an open-source local runtime that enables users to get up and running with large language models locally on macOS, Linux, and Windows. It packages model weights, configurations, and GPU acceleration into Modelfiles for simple command-line execution and local API serving.",
        "url": "https://github.com/ollama/ollama",
        "github_stars": 105000,
        "primary_language": "Go",
        "last_updated": "2026-09",
        "topics": ["local-llm", "llama", "go", "desktop-ai"],
        "license": "MIT",
        "forks": 8900
    },
    {
        "name": "microsoft/autogen",
        "description": "AutoGen is a programming framework by Microsoft Research that enables developers to build multi-agent conversational systems. It facilitates autonomous collaboration between customizable, conversable agents that combine LLMs, human inputs, and external code execution tools.",
        "url": "https://github.com/microsoft/autogen",
        "github_stars": 36000,
        "primary_language": "Python",
        "last_updated": "2026-09",
        "topics": ["multi-agent", "autonomous-agents", "llm-agents", "collaboration"],
        "license": "CC-BY-4.0",
        "forks": 5400
    },
    {
        "name": "geekan/MetaGPT",
        "description": "MetaGPT is a multi-agent framework that assigns standardized operating procedures (SOPs) and roles like Product Manager, Architect, and Engineer to LLM agents. Given a single line requirement, it autonomously produces user stories, competitive analysis, system design diagrams, and complete code repositories.",
        "url": "https://github.com/geekan/MetaGPT",
        "github_stars": 46000,
        "primary_language": "Python",
        "last_updated": "2026-09",
        "topics": ["software-engineering", "multi-agent", "sop", "autonomous-coding"],
        "license": "MIT",
        "forks": 5300
    },
    {
        "name": "browser-use/browser-use",
        "description": "Browser Use is an open-source library that enables AI agents to interact with web browsers using natural language instructions. It handles complex multi-step navigation, form completion, and content extraction by inspecting the accessibility tree and visual page elements.",
        "url": "https://github.com/browser-use/browser-use",
        "github_stars": 24000,
        "primary_language": "Python",
        "last_updated": "2026-09",
        "topics": ["browser-automation", "agentic-web", "playwright", "web-agent"],
        "license": "MIT",
        "forks": 2400
    },
    {
        "name": "modelcontextprotocol/servers",
        "description": "The Model Context Protocol servers repository contains official reference MCP server implementations curated by Anthropic. It provides standard connectors for local filesystems, Git repositories, SQLite databases, Brave search, and memory graphs.",
        "url": "https://github.com/modelcontextprotocol/servers",
        "github_stars": 21000,
        "primary_language": "TypeScript",
        "last_updated": "2026-09",
        "topics": ["mcp", "anthropic", "context-protocol", "tools"],
        "license": "MIT",
        "forks": 2200
    },
    {
        "name": "chroma-core/chroma",
        "description": "Chroma is an open-source AI-native embedding database designed from the ground up for developer ergonomics. It provides built-in embedding computation, semantic filtering, multi-modal search, and seamless integration with LangChain and LlamaIndex.",
        "url": "https://github.com/chroma-core/chroma",
        "github_stars": 16000,
        "primary_language": "Python",
        "last_updated": "2026-09",
        "topics": ["vector-database", "embeddings", "semantic-search", "rag"],
        "license": "Apache-2.0",
        "forks": 1400
    },
    {
        "name": "qdrant/qdrant",
        "description": "Qdrant is an open-source vector similarity search engine and database written in Rust. It offers production-grade nearest-neighbor search with payload-based filtering, quantization algorithms, and distributed clustering support for mission-critical enterprise workloads.",
        "url": "https://github.com/qdrant/qdrant",
        "github_stars": 22000,
        "primary_language": "Rust",
        "last_updated": "2026-09",
        "topics": ["vector-search", "rust", "hnsw", "nearest-neighbor"],
        "license": "Apache-2.0",
        "forks": 1600
    },
    {
        "name": "weaviate/weaviate",
        "description": "Weaviate is an open-source, AI-native vector database that allows developers to store data objects and vector embeddings alongside structured scalar properties. It supports hybrid vector-lexical search, multi-modal embeddings, and automated schema generation.",
        "url": "https://github.com/weaviate/weaviate",
        "github_stars": 12000,
        "primary_language": "Go",
        "last_updated": "2026-09",
        "topics": ["vector-database", "hybrid-search", "machine-learning", "graphql"],
        "license": "BSD-3-Clause",
        "forks": 950
    }
]

SEARCH_QUERIES = [
    "llm agents",
    "rag retrieval augmented generation",
    "vector database embeddings",
]

def extract() -> list[dict]:
    """Fetch prominent open-source AI repositories from GitHub API and curated seeds."""
    entities = []
    seen = set()

    # Add curated seeds first
    for seed in SEED_REPOSITORIES:
        name = seed["name"]
        seen.add(name.lower())
        entity = normalize(
            raw={
                **seed,
                "categories": ["repository", "open-source", seed["primary_language"].lower()]
            },
            entity_type="repository",
            source_name="GitHub Official Repositories",
            source_url=seed["url"],
        )
        entities.append(entity)

    # Fetch live repositories from GitHub Search API
    headers = {
        "User-Agent": "AIOrbit-Pipeline/1.0",
        "Accept": "application/vnd.github.v3+json",
    }
    for q in SEARCH_QUERIES:
        if len(entities) >= 25:
            break
        try:
            url = f"https://api.github.com/search/repositories?q={q.replace(' ', '+')}&sort=stars&order=desc&per_page=6"
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            
            for item in data.get("items", []):
                full_name = item.get("full_name", "")
                if not full_name or full_name.lower() in seen:
                    continue
                seen.add(full_name.lower())
                
                desc = item.get("description") or f"{full_name} is an open-source AI project on GitHub."
                if not desc.endswith(('.', '!', '?')):
                    desc += '.'
                desc += f" It has acquired over {item.get('stargazers_count', 0):,} stars and serves as a vital resource in the AI developer ecosystem."

                entity = normalize(
                    raw={
                        "name": full_name,
                        "description": desc,
                        "url": item.get("html_url", f"https://github.com/{full_name}"),
                        "categories": ["repository", "open-source", str(item.get("language", "software")).lower()],
                        "github_stars": item.get("stargazers_count", 0),
                        "primary_language": item.get("language") or "Python",
                        "last_updated": item.get("pushed_at", "2026-09")[:7],
                        "topics": item.get("topics", [])[:5],
                        "license": (item.get("license") or {}).get("spdx_id", "Open-Source"),
                        "forks": item.get("forks_count", 0),
                    },
                    entity_type="repository",
                    source_name="GitHub Search API",
                    source_url=f"https://github.com/search?q={q}",
                )
                entities.append(entity)
                if len(entities) >= 25:
                    break
        except Exception as e:
            print(f"[repositories] GitHub API warning for query '{q}': {e} — using seeds")

    return entities
