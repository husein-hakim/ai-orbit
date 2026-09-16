# src/extractors/collections.py
from src.normalizer import normalize

COLLECTIONS = [
    {
        "name": "awesome-chatgpt-prompts",
        "url": "https://github.com/f/awesome-chatgpt-prompts",
        "collection_type": "GitHub Awesome List & Prompt Collection",
        "item_count": 250,
        "maintained_by": "Fatih Kadir Akın & Global Open Source Community",
        "github_url": "https://github.com/f/awesome-chatgpt-prompts",
        "github_stars": 115000,
        "description": "awesome-chatgpt-prompts is one of the most widely starred open-source collections of prompts enabling ChatGPT to adopt specific personas and technical roles. It includes tested system prompts that configure AI models to act as Linux terminals, financial advisors, code reviewers, and debaters."
    },
    {
        "name": "awesome-llm",
        "url": "https://github.com/Hannibal046/Awesome-LLM",
        "collection_type": "Curated Academic Literature & Research List",
        "item_count": 650,
        "maintained_by": "Kehai Chen & Academic Contributors",
        "github_url": "https://github.com/Hannibal046/Awesome-LLM",
        "github_stars": 19500,
        "description": "Awesome-LLM is a curated chronological compilation of landmark research papers, pre-training methodologies, instruction-tuning frameworks, and evaluation benchmarks in large language models. Maintained for academic researchers, it organizes deep learning breakthroughs across model architectures and alignment techniques."
    },
    {
        "name": "awesome-mcp-servers",
        "url": "https://github.com/punkpeye/awesome-mcp-servers",
        "collection_type": "Protocol Tool Index & Community Directory",
        "item_count": 1200,
        "maintained_by": "punkpeye & MCP Developer Community",
        "github_url": "https://github.com/punkpeye/awesome-mcp-servers",
        "github_stars": 26000,
        "description": "awesome-mcp-servers is the premier community-driven registry indexing Model Context Protocol (MCP) servers, clients, and developer SDKs. It categorizes verified integrations across cloud infrastructure, databases, developer tooling, browser automation, and productivity applications."
    },
    {
        "name": "LMSYS Chatbot Arena",
        "url": "https://chat.lmsys.org",
        "collection_type": "Crowdsourced Benchmark & ELO Leaderboard",
        "item_count": 140,
        "maintained_by": "Large Model Systems Organization (LMSYS)",
        "github_url": "https://github.com/lm-sys/FastChat",
        "github_stars": 36000,
        "description": "LMSYS Chatbot Arena is a crowdsourced open research benchmark platform for evaluating large language models based on human blind pairwise preference comparisons. Leveraging Bradley-Terry statistical modeling, it calculates dynamic ELO ratings widely recognized as the gold standard for comparing frontier models."
    },
    {
        "name": "Papers With Code",
        "url": "https://paperswithcode.com",
        "collection_type": "Machine Learning Research & Benchmark Index",
        "item_count": 95000,
        "maintained_by": "Meta AI & Community Contributors",
        "github_url": "https://github.com/paperswithcode/paperswithcode-data",
        "github_stars": 14000,
        "description": "Papers With Code is a free, open resource that links machine learning research papers with their corresponding official code implementations, evaluation datasets, and state-of-the-art leaderboards. It provides transparent reproducibility metrics across computer vision, natural language processing, and robotics."
    },
    {
        "name": "OpenLLM Leaderboard",
        "url": "https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard",
        "collection_type": "Automated Benchmark & Model Evaluation Hub",
        "item_count": 8500,
        "maintained_by": "Hugging Face Research Team",
        "github_url": "https://github.com/EleutherAI/lm-evaluation-harness",
        "github_stars": 8200,
        "description": "The Open LLM Leaderboard by Hugging Face tracks, ranks, and evaluates newly released open-access language models on an automated suite of rigorous reasoning benchmarks including MMLU-Pro, GSM8k, and MATH. It serves as an impartial verification gate for academic and enterprise open-weights models."
    },
    {
        "name": "The Pile",
        "url": "https://pile.eleuther.ai",
        "collection_type": "Open-Source AI Pre-Training Dataset",
        "item_count": 22,
        "maintained_by": "EleutherAI Non-Profit Research Group",
        "github_url": "https://github.com/EleutherAI/the-pile",
        "github_stars": 4200,
        "description": "The Pile is an 825 GiB diverse, open-source language modeling pre-training dataset constructed from 22 smaller high-quality datasets spanning PubMed Central, arXiv, GitHub, and FreeLaw filings. Engineered by EleutherAI, it has served as the empirical foundation for training multiple open foundation models."
    },
    {
        "name": "PromptBase",
        "url": "https://promptbase.com",
        "collection_type": "Commercial Prompt Marketplace & Repository",
        "item_count": 120000,
        "maintained_by": "PromptBase Inc",
        "github_url": "",
        "github_stars": None,
        "description": "PromptBase is a curated marketplace where prompt engineers and digital creators buy and sell high-performing prompts for Midjourney, ChatGPT, DALL-E, and Stable Diffusion. It tests prompts for reliability, style consistency, and photorealistic rendering quality before approving them for commercial listing."
    },
    {
        "name": "FlowGPT",
        "url": "https://flowgpt.com",
        "collection_type": "Interactive Prompt Sharing Community & App Store",
        "item_count": 450000,
        "maintained_by": "FlowGPT Inc",
        "github_url": "",
        "github_stars": None,
        "description": "FlowGPT is a global community platform and prompt ecosystem where users discover, test, and share interactive AI agent characters, coding templates, and productivity prompts. It provides in-browser execution sandboxes allowing visitors to experiment with community creations across multiple foundation models."
    },
    {
        "name": "Hugging Face Datasets Hub",
        "url": "https://huggingface.co/datasets",
        "collection_type": "Global Machine Learning Dataset Archive",
        "item_count": 220000,
        "maintained_by": "Hugging Face & Global Community",
        "github_url": "https://github.com/huggingface/datasets",
        "github_stars": 20000,
        "description": "Hugging Face Datasets is the world's premier open community repository of datasets for natural language processing, computer vision, tabular modeling, and speech analysis. With built-in streaming, memory mapping, and one-line Python loading, it democratizes access to petabytes of training and evaluation corpora."
    }
]

def extract() -> list[dict]:
    """Extract prominent curated AI collections, benchmark leaderboards, and prompt libraries."""
    entities = []
    for c in COLLECTIONS:
        entity = normalize(
            raw={
                "name": c["name"],
                "description": c["description"],
                "url": c["url"],
                "categories": ["collection", "curation", c["collection_type"].lower()],
                "collection_type": c["collection_type"],
                "item_count": c["item_count"],
                "maintained_by": c["maintained_by"],
                "github_url": c["github_url"],
                "github_stars": c["github_stars"],
            },
            entity_type="collection",
            source_name="Curated AI Directories & Registries",
            source_url=c["url"],
        )
        entities.append(entity)
    return entities
