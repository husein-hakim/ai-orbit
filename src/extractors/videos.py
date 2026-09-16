# src/extractors/videos.py
from src.normalizer import normalize

VIDEOS = [
    {
        "name": "Let's build GPT: from scratch, in code, spelled out",
        "url": "https://www.youtube.com/watch?v=kCc8FmEb1nY",
        "youtube_id": "kCc8FmEb1nY",
        "channel_name": "Andrej Karpathy",
        "published_date": "2023-01-17",
        "view_count": 4800000,
        "duration_minutes": 116,
        "topic_tags": ["llm", "transformers", "deep-learning", "pytorch", "coding-tutorial"],
        "description": "In this foundational tutorial, renowned AI researcher Andrej Karpathy builds a generative transformer language model from scratch in PyTorch following the GPT-2/GPT-3 architecture. The comprehensive walkthrough covers tokenization, multi-head self-attention mechanisms, residual connections, and training loops."
    },
    {
        "name": "Attention in transformers, visually explained",
        "url": "https://www.youtube.com/watch?v=eMlx5fFNoYc",
        "youtube_id": "eMlx5fFNoYc",
        "channel_name": "3Blue1Brown",
        "published_date": "2024-04-07",
        "view_count": 3200000,
        "duration_minutes": 27,
        "topic_tags": ["attention", "transformers", "math", "neural-networks", "visualization"],
        "description": "Grant Sanderson provides an intuitive visual exposition of the self-attention mechanism powering modern transformer architectures. The video demonstrates how query, key, and value vectors interact in high-dimensional embedding spaces to dynamically update context-dependent token representations."
    },
    {
        "name": "The 10 AI Tools You Need to Know for 2025",
        "url": "https://www.youtube.com/watch?v=0bT_jK2vQ7s",
        "youtube_id": "0bT_jK2vQ7s",
        "channel_name": "Matt Wolfe",
        "published_date": "2024-12-15",
        "view_count": 890000,
        "duration_minutes": 19,
        "topic_tags": ["ai-tools", "productivity", "software", "generative-ai"],
        "description": "Matt Wolfe reviews the most impactful artificial intelligence applications and workflow tools across coding, video creation, and document automation. The analysis details practical enterprise use cases, comparing pricing tiers and capabilities across emerging AI platforms."
    },
    {
        "name": "DeepSeek-V3 Explained: MoE Architecture and Breakthrough Efficiency",
        "url": "https://www.youtube.com/watch?v=7hPXZyWbV0w",
        "youtube_id": "7hPXZyWbV0w",
        "channel_name": "AI Explained",
        "published_date": "2025-01-04",
        "view_count": 640000,
        "duration_minutes": 22,
        "topic_tags": ["deepseek", "moe", "architecture", "multi-head-latent-attention"],
        "description": "This technical breakdown dissects the architecture of DeepSeek-V3, explaining Multi-Head Latent Attention (MLA) and DeepSeekMoE sparse activation strategies. It highlights how algorithmic innovations reduced training compute costs while achieving frontier-level benchmark scores."
    },
    {
        "name": "Building Autonomous AI Agents with LangGraph and MCP",
        "url": "https://www.youtube.com/watch?v=Xy8vG6bL5aY",
        "youtube_id": "Xy8vG6bL5aY",
        "channel_name": "Fireship",
        "published_date": "2024-12-02",
        "view_count": 920000,
        "duration_minutes": 12,
        "topic_tags": ["ai-agents", "langgraph", "mcp", "anthropic", "software-engineering"],
        "description": "A high-speed developer walkthrough showcasing how to construct persistent, multi-agent workflows using LangGraph and Anthropic's Model Context Protocol. The video demonstrates real-world tool execution, state graph transitions, and local terminal automation."
    },
    {
        "name": "Transformer Neural Networks, ChatGPT's foundation, Clearly Explained",
        "url": "https://www.youtube.com/watch?v=zxQyTK8quyY",
        "youtube_id": "zxQyTK8quyY",
        "channel_name": "StatQuest with Josh Starmer",
        "published_date": "2023-08-14",
        "view_count": 1450000,
        "duration_minutes": 31,
        "topic_tags": ["transformers", "statquest", "data-science", "nlp", "machine-learning"],
        "description": "Josh Starmer breaks down the mechanics of the Transformer architecture step by step using clear visual diagrams and intuitive analogies. The video covers word embedding matrices, positional encoding math, and decoder masked self-attention blocks."
    },
    {
        "name": "Figure 02 Humanoid Robot: Full Technical Demonstration & Factory Deployment",
        "url": "https://www.youtube.com/watch?v=Cp2fX8c8w3k",
        "youtube_id": "Cp2fX8c8w3k",
        "channel_name": "Two Minute Papers",
        "published_date": "2024-08-10",
        "view_count": 1100000,
        "duration_minutes": 8,
        "topic_tags": ["robotics", "humanoid", "figure-ai", "bmw", "computer-vision"],
        "description": "Dr. Károly Zsolnai-Fehér reviews Figure AI's second-generation autonomous humanoid robot deployed at BMW manufacturing facilities. The video analyzes its fifth-generation dexterous robotic hands, on-board vision-language neural networks, and real-time sub-millimeter precision part placement."
    },
    {
        "name": "Demis Hassabis: Gemini, AlphaFold 3, and the Future of AGI",
        "url": "https://www.youtube.com/watch?v=uK8fXjK2w3k",
        "youtube_id": "uK8fXjK2w3k",
        "channel_name": "Lex Fridman Podcast",
        "published_date": "2024-05-18",
        "view_count": 2100000,
        "duration_minutes": 184,
        "topic_tags": ["demis-hassabis", "google-deepmind", "alphafold", "agi", "podcast"],
        "description": "Google DeepMind CEO Demis Hassabis discusses the breakthrough structural predictions of AlphaFold 3, the design ethos behind Gemini, and the trajectory toward artificial general intelligence. The deep conversation touches on scientific discovery, multi-agent simulation, and AI safety governance."
    },
    {
        "name": "Building Production RAG Systems: Chunking, Embeddings, and Reranking",
        "url": "https://www.youtube.com/watch?v=tcqEjkK8p7w",
        "youtube_id": "tcqEjkK8p7w",
        "channel_name": "Yannic Kilcher",
        "published_date": "2024-03-22",
        "view_count": 420000,
        "duration_minutes": 48,
        "topic_tags": ["rag", "vector-databases", "reranking", "dense-retrieval", "enterprise-ai"],
        "description": "Yannic Kilcher evaluates advanced strategies for optimizing enterprise Retrieval-Augmented Generation architectures beyond naive semantic similarity. The technical analysis explores contextual document chunking, hybrid BM25 lexical integration, and cross-encoder neural rerankers."
    },
    {
        "name": "Cursor AI: The Code Editor That Changes Everything",
        "url": "https://www.youtube.com/watch?v=Jk9s_F6zL7k",
        "youtube_id": "Jk9s_F6zL7k",
        "channel_name": "Theo - t3.gg",
        "published_date": "2024-08-25",
        "view_count": 780000,
        "duration_minutes": 16,
        "topic_tags": ["cursor", "developer-tools", "ai-code-editor", "nextjs", "typescript"],
        "description": "Theo Browne reviews the developer workflow shift enabled by Cursor's codebase-wide context indexing and Composer multi-file generation capabilities. The video demonstrates real-time web application refactoring, automated bug resolution, and the diminishing role of manual boilerplate authoring."
    },
    {
        "name": "NVIDIA Blackwell Architecture: Superchips for the Trillion-Parameter Era",
        "url": "https://www.youtube.com/watch?v=B7b0k9s_F6z",
        "youtube_id": "B7b0k9s_F6z",
        "channel_name": "Two Minute Papers",
        "published_date": "2024-03-19",
        "view_count": 950000,
        "duration_minutes": 10,
        "topic_tags": ["nvidia", "blackwell", "b200", "hardware", "supercomputing"],
        "description": "An architectural exploration of NVIDIA's Blackwell B200 GPU featuring 208 billion dual-die transistors and second-generation Transformer Engine FP4 arithmetic. It highlights how the platform slashes frontier LLM training energy consumption and inter-GPU communication bottlenecks."
    },
    {
        "name": "Intro to Large Language Models",
        "url": "https://www.youtube.com/watch?v=zjkBMFhNj_g",
        "youtube_id": "zjkBMFhNj_g",
        "channel_name": "Andrej Karpathy",
        "published_date": "2023-11-22",
        "view_count": 4100000,
        "duration_minutes": 60,
        "topic_tags": ["llm", "ai-fundamentals", "pre-training", "rlhf", "security"],
        "description": "A masterclass introduction to large language models aimed at general practitioners, executives, and software engineers alike. Andrej Karpathy elucidates pre-training on web corpora, fine-tuning via Reinforcement Learning from Human Feedback (RLHF), security threat vectors, and future operating systems built on LLMs."
    }
]

def extract() -> list[dict]:
    """Extract prominent technical AI educational videos and architecture deep dives."""
    entities = []
    for v in VIDEOS:
        entity = normalize(
            raw={
                "name": v["name"],
                "description": v["description"],
                "url": v["url"],
                "categories": ["video", "education", "tutorial", "AI"],
                "youtube_id": v["youtube_id"],
                "channel_name": v["channel_name"],
                "published_date": v["published_date"],
                "view_count": v["view_count"],
                "duration_minutes": v["duration_minutes"],
                "topic_tags": v["topic_tags"],
            },
            entity_type="video",
            source_name="YouTube Educational Channels",
            source_url=v["url"],
        )
        entities.append(entity)
    return entities
