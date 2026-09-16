# src/extractors/tasks.py
from src.normalizer import normalize

TASKS = [
    {
        "name": "Write code faster with AI",
        "url": "https://aiorbit.com/tasks/code-generation",
        "task_category": "Software Engineering",
        "complexity": "Intermediate",
        "tools_that_solve_this": ["GitHub Copilot", "Cursor", "Claude Code", "ChatGPT"],
        "example_prompt": "Write a Python script that connects to PostgreSQL and computes running daily active users using SQLAlchemy.",
        "description": "Writing code with AI involves leveraging large language models to generate syntax-accurate, context-aware code functions, unit tests, and API integrations in real time. Developers use conversational or inline suggestions to bypass repetitive boilerplate, adhere to language idioms, and prototype complex features up to 55% faster."
    },
    {
        "name": "Summarize long documents",
        "url": "https://aiorbit.com/tasks/document-summarization",
        "task_category": "Productivity & Research",
        "complexity": "Simple",
        "tools_that_solve_this": ["Claude.ai", "ChatGPT", "Notion AI", "Gemini"],
        "example_prompt": "Summarize this 60-page financial quarterly report highlighting EBITDA margins, unexpected liabilities, and forward guidance.",
        "description": "Document summarization uses long-context foundation models to condense multi-page academic papers, legal filings, and business transcripts into key takeaways and actionable executive briefs. It allows analysts and students to extract salient facts without manual skimming while preserving contextual nuances."
    },
    {
        "name": "Generate images from text prompts",
        "url": "https://aiorbit.com/tasks/image-generation",
        "task_category": "Creative Design",
        "complexity": "Simple",
        "tools_that_solve_this": ["Midjourney", "DALL-E 3", "Stable Diffusion 3.5 Large", "Adobe Firefly"],
        "example_prompt": "An isometric 3D render of a futuristic hydroponic greenhouse on Mars with neon ambient lighting and detailed glass reflections.",
        "description": "Text-to-image generation translates descriptive natural language prompts into photorealistic photography, concept sketches, and marketing illustrations. Diffusion and multimodal transformer models allow creators to rapidly iterate on art direction, storyboards, and advertising collateral without physical photoshoots."
    },
    {
        "name": "Search the web with AI answers",
        "url": "https://aiorbit.com/tasks/ai-search",
        "task_category": "Research & Search",
        "complexity": "Simple",
        "tools_that_solve_this": ["Perplexity", "ChatGPT", "Gemini", "Phind"],
        "example_prompt": "What are the latest regulatory changes affecting generative AI model exports in the European Union as of 2025?",
        "description": "AI-powered web searching synthesizes live internet crawl results into structured, natural language responses accompanied by clickable inline source citations. It eliminates traditional search engine link navigation by evaluating source credibility and reconciling conflicting viewpoints into a coherent briefing."
    },
    {
        "name": "Transcribe audio to text",
        "url": "https://aiorbit.com/tasks/audio-transcription",
        "task_category": "Audio & Media",
        "complexity": "Simple",
        "tools_that_solve_this": ["Whisper Large v3", "Descript", "ElevenLabs"],
        "example_prompt": "Transcribe this 45-minute audio interview into clean English text with speaker diarization and timestamp markers.",
        "description": "Audio transcription converts recorded voice recordings, boardroom meetings, and podcasts into punctuated, speaker-attributed digital text. State-of-the-art automatic speech recognition models operate robustly across background noise, regional accents, and specialized scientific nomenclature."
    },
    {
        "name": "Translate between languages",
        "url": "https://aiorbit.com/tasks/machine-translation",
        "task_category": "Language & Localization",
        "complexity": "Simple",
        "tools_that_solve_this": ["Claude.ai", "ChatGPT", "Gemini", "DeepL"],
        "example_prompt": "Translate this legal terms of service document from English to Japanese ensuring formal business keigo register.",
        "description": "Machine translation harnesses multilingual transformer architectures to translate text between dozens of languages while retaining cultural idioms, formal honorifics, and industry-specific terminology. Global enterprises employ it for real-time customer support localization and multinational legal alignment."
    },
    {
        "name": "Generate videos from text",
        "url": "https://aiorbit.com/tasks/video-generation",
        "task_category": "Creative Media",
        "complexity": "Complex",
        "tools_that_solve_this": ["Runway Gen-3", "Sora", "Luma Dream Machine", "Kling"],
        "example_prompt": "Cinematic drone shot flying through a bioluminescent redwood forest at dusk with volumetric fog and gentle camera roll.",
        "description": "Text-to-video generation utilizes spatio-temporal diffusion models to generate coherent cinematic footage, physical simulations, and digital animation from written prompts. It offers directors fine-grained control over camera trajectories, dynamic lighting, and character motion consistency across video shots."
    },
    {
        "name": "Analyze data and create visualizations",
        "url": "https://aiorbit.com/tasks/data-analysis",
        "task_category": "Data Science",
        "complexity": "Intermediate",
        "tools_that_solve_this": ["ChatGPT", "Claude.ai", "Databricks", "Weights & Biases"],
        "example_prompt": "Load this CSV of customer transactions, calculate monthly churn rates by cohort, and plot an interactive heatmap.",
        "description": "Automated data analysis allows non-technical business professionals to upload unstructured tabular spreadsheets and generate statistical correlations, trend forecasts, and interactive visual charts. LLMs write and execute Python visualization scripts in sandboxed environments to surface hidden business patterns."
    },
    {
        "name": "Draft and refine emails",
        "url": "https://aiorbit.com/tasks/email-drafting",
        "task_category": "Business Communications",
        "complexity": "Simple",
        "tools_that_solve_this": ["Grammarly AI", "Notion AI", "ChatGPT", "Claude.ai"],
        "example_prompt": "Draft an empathetic yet firm email negotiating contract renewal terms with an enterprise client asking for a 15% discount.",
        "description": "Email drafting uses contextual language models to generate professional, persuasive, and grammatically polished corporate correspondence. Users can modulate emotional tone, brevity, and rhetorical posture to ensure clear communication across diverse commercial scenarios."
    },
    {
        "name": "Build software without coding",
        "url": "https://aiorbit.com/tasks/no-code-development",
        "task_category": "Software Engineering",
        "complexity": "Intermediate",
        "tools_that_solve_this": ["Bolt.new", "Lovable", "v0", "Replit AI"],
        "example_prompt": "Create an end-to-end SaaS subscription tracker with user authentication, Stripe checkout, and an analytics dashboard.",
        "description": "Prompt-driven application building enables entrepreneurs to create, test, and deploy interactive web applications and mobile apps entirely through conversational dialogue. Generative app engines automatically write full-stack frontend code, configure database schemas, and deploy cloud hosting."
    },
    {
        "name": "Convert text to realistic speech",
        "url": "https://aiorbit.com/tasks/text-to-speech",
        "task_category": "Audio & Media",
        "complexity": "Simple",
        "tools_that_solve_this": ["ElevenLabs", "Descript", "ChatGPT"],
        "example_prompt": "Convert this audiobook chapter narration into speech using an elderly Scottish narrator voice with expressive dramatic pauses.",
        "description": "Text-to-speech synthesis produces studio-grade, human-like voice recordings with emotional pacing, breath intake nuances, and authentic accents. It powers digital audiobook publishing, accessibility screen readers, automated voiceover narration, and conversational AI agents."
    },
    {
        "name": "Research topics comprehensively",
        "url": "https://aiorbit.com/tasks/deep-research",
        "task_category": "Research & Analysis",
        "complexity": "Complex",
        "tools_that_solve_this": ["Perplexity", "Claude.ai", "NotebookLM", "Gemini"],
        "example_prompt": "Conduct an exhaustive market analysis on solid-state battery commercialization timelines, patent holders, and manufacturing hurdles.",
        "description": "Deep autonomous research coordinates multi-step iterative web searches, document cross-referencing, and synthesized multi-chapter reports on intricate subject matters. AI researchers evaluate hundreds of disparate sources to produce holistic competitive intelligence and academic literature reviews."
    },
    {
        "name": "Debug code automatically",
        "url": "https://aiorbit.com/tasks/code-debugging",
        "task_category": "Software Engineering",
        "complexity": "Intermediate",
        "tools_that_solve_this": ["Cursor", "Claude Code", "GitHub Copilot", "ChatGPT"],
        "example_prompt": "Analyze this memory leak error trace in a high-concurrency Go web server and supply the exact concurrency mutex fix.",
        "description": "Automated code debugging inspects runtime stack traces, memory dumps, and software logic flaws to pinpoint root causes and recommend surgical code patches. AI tools simulate control flow paths, detect edge-case race conditions, and write regression tests to verify bug resolution."
    },
    {
        "name": "Generate music from text",
        "url": "https://aiorbit.com/tasks/music-generation",
        "task_category": "Creative Audio",
        "complexity": "Simple",
        "tools_that_solve_this": ["Suno", "Udio", "ElevenLabs"],
        "example_prompt": "Compose an energetic 90s synth-wave track with driving bass, melodic arpeggios, and nostalgic vocal hooks about highway night driving.",
        "description": "Text-to-music synthesis generates fully arranged and produced musical audio tracks including harmonized vocals, multi-instrument rhythm sections, and cohesive song structures. Content creators, indie game developers, and commercial producers use it for instantaneous royalty-free soundtrack generation."
    },
    {
        "name": "Automate repetitive workflows",
        "url": "https://aiorbit.com/tasks/workflow-automation",
        "task_category": "Operations & RPA",
        "complexity": "Complex",
        "tools_that_solve_this": ["LangChain", "Claude Code", "Playwright MCP Server", "ChatGPT"],
        "example_prompt": "Monitor incoming invoice emails, extract billing tables into JSON, match purchase orders in ERP, and alert Slack on discrepancies.",
        "description": "AI-driven workflow automation chains reasoning models with external API tools and browser automation scripts to perform complex multi-system administrative tasks without human intervention. Autonomous agents extract data across disparate enterprise software silos and handle exceptions intelligently."
    },
    {
        "name": "Extract structured information from documents",
        "url": "https://aiorbit.com/tasks/information-extraction",
        "task_category": "Data Engineering",
        "complexity": "Intermediate",
        "tools_that_solve_this": ["Claude.ai", "LlamaIndex", "ChatGPT", "Scale AI"],
        "example_prompt": "Parse these 50 unstructured medical claim PDFs and output a normalized JSON schema with patient ID, diagnosis codes, and billed amounts.",
        "description": "Document information extraction transforms messy unstructured documents, scanned PDF contracts, and receipts into validated JSON schemas and relational tables. Vision-language models identify tables, key-value entity pairs, and signatures without requiring brittle programmatic regex templates."
    },
    {
        "name": "Train and fine-tune custom AI models",
        "url": "https://aiorbit.com/tasks/model-fine-tuning",
        "task_category": "Machine Learning Ops",
        "complexity": "Complex",
        "tools_that_solve_this": ["Together AI", "Hugging Face", "Weights & Biases", "Replicate"],
        "example_prompt": "Fine-tune a Llama 3.1 8B base model using LoRA adapters on 10,000 domain-specific customer service dialogue transcripts.",
        "description": "Model fine-tuning adapts open-weights foundation models to specialized corporate domains, unique tonal personas, and proprietary API tool-calling formats using Parameter-Efficient Fine-Tuning (PEFT) and LoRA. It grants companies customized, secure intelligence with lower latency and reduced operational costs."
    },
    {
        "name": "Deploy AI applications at scale",
        "url": "https://aiorbit.com/tasks/model-deployment",
        "task_category": "Cloud Infrastructure",
        "complexity": "Complex",
        "tools_that_solve_this": ["vLLM", "Together AI", "Replicate", "Ollama"],
        "example_prompt": "Deploy a distributed vLLM inference cluster on Kubernetes with multi-GPU tensor parallelism, autoscaling, and PagedAttention.",
        "description": "Deploying AI applications involves orchestrating high-performance GPU compute clusters, containerized serving engines, vector databases, and load balancers to deliver sub-second response times under heavy user traffic. Engineers configure quantization, caching, and model parallelism to maximize throughput per watt."
    }
]

def extract() -> list[dict]:
    """Extract standard AI user tasks and capabilities."""
    entities = []
    for t in TASKS:
        entity = normalize(
            raw={
                "name": t["name"],
                "description": t["description"],
                "url": t["url"],
                "categories": ["task", "ai-use-case", t["task_category"].lower()],
                "task_category": t["task_category"],
                "complexity": t["complexity"],
                "tools_that_solve_this": t["tools_that_solve_this"],
                "example_prompt": t["example_prompt"],
            },
            entity_type="task",
            source_name="AIOrbit Task Taxonomy",
            source_url="https://aiorbit.com/tasks",
        )
        entities.append(entity)
    return entities
