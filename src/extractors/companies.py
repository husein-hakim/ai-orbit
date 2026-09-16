# src/extractors/companies.py
from src.normalizer import normalize

COMPANIES = [
    {
        "name": "Anthropic",
        "url": "https://anthropic.com",
        "founding_year": 2021,
        "headquarters": "San Francisco, CA",
        "industry_sector": "AI Safety & Foundation Models",
        "notable_products": ["Claude 3.5 Sonnet", "Claude.ai", "Model Context Protocol", "Claude Code"],
        "funding_stage": "Series E ($7B+)",
        "employee_count": "500-1000",
        "description": "Anthropic is an AI safety and research company dedicated to building reliable, interpretable, and steerable AI systems. Founded by former senior members of OpenAI, the organization created the Claude foundation model family and originated the Model Context Protocol (MCP) to standardize AI integration."
    },
    {
        "name": "OpenAI",
        "url": "https://openai.com",
        "founding_year": 2015,
        "headquarters": "San Francisco, CA",
        "industry_sector": "Artificial General Intelligence",
        "notable_products": ["ChatGPT", "GPT-4o", "DALL-E 3", "Sora", "OpenAI o1"],
        "funding_stage": "Private ($150B+ valuation)",
        "employee_count": "1000-5000",
        "description": "OpenAI is an AI research and deployment enterprise committed to ensuring that artificial general intelligence benefits all of humanity. It pioneered mainstream conversational AI with ChatGPT and developed leading multimodal generative models including GPT-4o, DALL-E, and Sora."
    },
    {
        "name": "Google DeepMind",
        "url": "https://deepmind.google",
        "founding_year": 2010,
        "headquarters": "London, United Kingdom",
        "industry_sector": "Scientific AI & Foundation Systems",
        "notable_products": ["Gemini", "AlphaFold", "Gemma", "AlphaCode"],
        "funding_stage": "Subsidiary (Alphabet)",
        "employee_count": "1000-5000",
        "description": "Google DeepMind is the premier scientific artificial intelligence research laboratory of Alphabet. Its multidisciplinary breakthroughs span structural biology with AlphaFold, game theory with AlphaGo, and frontier multimodal language intelligence with the Gemini foundation architecture."
    },
    {
        "name": "Mistral AI",
        "url": "https://mistral.ai",
        "founding_year": 2023,
        "headquarters": "Paris, France",
        "industry_sector": "Open AI Infrastructure",
        "notable_products": ["Mistral Large 2", "Mixtral 8x22B", "Codestral", "Le Chat"],
        "funding_stage": "Series B ($6B+ valuation)",
        "employee_count": "100-250",
        "description": "Mistral AI is a European AI company focused on delivering openly accessible, high-efficiency generative language models to global developers. Founded by alumni of Meta AI and DeepMind, it is recognized for pioneering sparse Mixture-of-Experts architectures with world-class inference speeds."
    },
    {
        "name": "Cohere",
        "url": "https://cohere.com",
        "founding_year": 2019,
        "headquarters": "Toronto, Canada",
        "industry_sector": "Enterprise Generative AI",
        "notable_products": ["Command R+", "Cohere Embed", "Cohere Rerank"],
        "funding_stage": "Series D ($5B+ valuation)",
        "employee_count": "250-500",
        "description": "Cohere provides cloud-agnostic enterprise large language models designed for mission-critical search, classification, and retrieval-augmented generation. It emphasizes data privacy, on-premise deployment flexibility, and multi-tenant security guarantees for Global 2000 enterprises."
    },
    {
        "name": "Hugging Face",
        "url": "https://huggingface.co",
        "founding_year": 2016,
        "headquarters": "New York, NY",
        "industry_sector": "AI Collaboration Platform",
        "notable_products": ["Transformers", "Hugging Face Hub", "Inference Endpoints", "Spaces"],
        "funding_stage": "Series D ($4.5B valuation)",
        "employee_count": "250-500",
        "description": "Hugging Face is the central collaborative platform and open-source registry where the global machine learning community shares models, datasets, and applications. Its ubiquitous Python libraries power modern NLP, computer vision, and audio pipelines across academia and industry."
    },
    {
        "name": "Stability AI",
        "url": "https://stability.ai",
        "founding_year": 2020,
        "headquarters": "London, United Kingdom",
        "industry_sector": "Generative Media & Diffusion Models",
        "notable_products": ["Stable Diffusion 3.5", "SDXL", "Stable Video Diffusion", "Stable Audio"],
        "funding_stage": "Series A",
        "employee_count": "100-250",
        "description": "Stability AI develops open-access diffusion foundation models across imaging, video, 3D generation, and audio synthesis. It democratized generative media creation globally by releasing checkpoint weights that enable developers to run photorealistic text-to-image models on consumer hardware."
    },
    {
        "name": "Midjourney",
        "url": "https://midjourney.com",
        "founding_year": 2021,
        "headquarters": "San Francisco, CA",
        "industry_sector": "Generative Visual Arts",
        "notable_products": ["Midjourney v6", "Midjourney Web Editor"],
        "funding_stage": "Bootstrapped (Profitable)",
        "employee_count": "50-100",
        "description": "Midjourney is an independent research lab exploring new mediums of thought and expanding the imaginative powers of the human species. Led by David Holz, the self-funded organization produces world-renowned photorealistic and painterly visual synthesis engines accessible via chat and web canvas interfaces."
    },
    {
        "name": "ElevenLabs",
        "url": "https://elevenlabs.io",
        "founding_year": 2022,
        "headquarters": "New York, NY",
        "industry_sector": "Voice AI & Audio Research",
        "notable_products": ["Voice Cloning", "Text-to-Speech API", "Dubbing Studio", "Conversational AI"],
        "funding_stage": "Series B ($1.1B valuation)",
        "employee_count": "100-250",
        "description": "ElevenLabs is a voice technology research company creating software that brings natural emotion, pacing, and multi-lingual inflections to synthesized human speech. Its low-latency text-to-speech APIs and voice-cloning capabilities power audiobooks, video localization, and interactive gaming experiences."
    },
    {
        "name": "Runway",
        "url": "https://runwayml.com",
        "founding_year": 2018,
        "headquarters": "New York, NY",
        "industry_sector": "AI Video Generation & VFX",
        "notable_products": ["Gen-3 Alpha", "Gen-2", "Motion Brush", "Runway Studios"],
        "funding_stage": "Series C ($1.5B valuation)",
        "employee_count": "100-250",
        "description": "Runway builds multimodal AI systems that advance creative workflows across cinematography, commercial advertising, and visual effects. Its generative video architectures, notably Gen-3 Alpha, grant filmmakers granular camera, motion, and temporal control over synthesized video sequences."
    },
    {
        "name": "Perplexity AI",
        "url": "https://perplexity.ai",
        "founding_year": 2022,
        "headquarters": "San Francisco, CA",
        "industry_sector": "Conversational Search Engine",
        "notable_products": ["Perplexity Pro", "Sonar Models", "Perplexity Enterprise Pro"],
        "funding_stage": "Series B ($3B+ valuation)",
        "employee_count": "100-250",
        "description": "Perplexity AI operates a conversational answer engine that pairs real-time web retrieval with LLM synthesis to deliver direct, cited answers. It challenges conventional algorithmic search by synthesizing multiple reputable online sources into concise, multi-perspective summaries."
    },
    {
        "name": "Together AI",
        "url": "https://together.ai",
        "founding_year": 2022,
        "headquarters": "San Francisco, CA",
        "industry_sector": "Cloud AI Compute & Inference",
        "notable_products": ["Together Inference Engine", "GPU Clusters", "Fine-Tuning Platform"],
        "funding_stage": "Series A ($1.25B valuation)",
        "employee_count": "100-250",
        "description": "Together AI is an AI cloud platform enabling researchers and developers to train, fine-tune, and deploy open-source generative models at maximum hardware efficiency. Its proprietary inference engine delivers leading token throughput and minimal latency across NVIDIA H100 GPU clusters."
    },
    {
        "name": "Replicate",
        "url": "https://replicate.com",
        "founding_year": 2019,
        "headquarters": "San Francisco, CA",
        "industry_sector": "Serverless ML Deployment",
        "notable_products": ["Replicate Cloud API", "Cog Container Tool"],
        "funding_stage": "Series B ($350M valuation)",
        "employee_count": "50-100",
        "description": "Replicate enables software engineers to run open-source machine learning models in the cloud with just a few lines of code via serverless APIs. It automates GPU autoscaling, containerization with open-source Cog, and cold-start minimization for thousands of production AI applications."
    },
    {
        "name": "Scale AI",
        "url": "https://scale.com",
        "founding_year": 2016,
        "headquarters": "San Francisco, CA",
        "industry_sector": "AI Data Infrastructure & RLHF",
        "notable_products": ["Scale Data Engine", "SEAL Leaderboards", "GenAI Platform"],
        "funding_stage": "Series F ($13.8B valuation)",
        "employee_count": "1000-5000",
        "description": "Scale AI delivers the data infrastructure required to train and align frontier foundational artificial intelligence models. It provides enterprise data annotation, automated synthetic data generation, and RLHF (Reinforcement Learning from Human Feedback) pipelines for autonomous vehicles and LLMs."
    },
    {
        "name": "Pinecone",
        "url": "https://pinecone.io",
        "founding_year": 2019,
        "headquarters": "New York, NY",
        "industry_sector": "Vector Database Infrastructure",
        "notable_products": ["Pinecone Serverless", "Vector Search API"],
        "funding_stage": "Series B ($750M valuation)",
        "employee_count": "100-250",
        "description": "Pinecone provides a fully managed, cloud-native vector database engineered for ultra-low latency semantic search and high-throughput RAG systems. Its serverless architecture decouples indexing compute from storage, lowering production retrieval costs for enterprise AI applications."
    },
    {
        "name": "LangChain",
        "url": "https://langchain.com",
        "founding_year": 2022,
        "headquarters": "San Francisco, CA",
        "industry_sector": "AI Application Frameworks",
        "notable_products": ["LangChain Framework", "LangGraph", "LangSmith"],
        "funding_stage": "Series A ($200M+ valuation)",
        "employee_count": "50-100",
        "description": "LangChain builds the standard open-source framework and enterprise observability tooling for building production-ready LLM agents and workflows. Its LangGraph library introduces cyclic multi-agent graph orchestration, while LangSmith provides debugging, testing, and latency monitoring."
    },
    {
        "name": "Weights & Biases",
        "url": "https://wandb.ai",
        "founding_year": 2017,
        "headquarters": "San Francisco, CA",
        "industry_sector": "MLOps & Observability",
        "notable_products": ["W&B Models", "W&B Weave", "W&B Artifacts"],
        "funding_stage": "Series C ($1B+ valuation)",
        "employee_count": "250-500",
        "description": "Weights & Biases is the enterprise developer platform for machine learning practitioners to track experiments, manage datasets, and evaluate generative models. Trusted by OpenAI, Meta, and Toyota, it streamlines collaboration throughout model pre-training and reinforcement alignment."
    },
    {
        "name": "DeepSeek",
        "url": "https://deepseek.com",
        "founding_year": 2023,
        "headquarters": "Hangzhou, China",
        "industry_sector": "Frontier AI Research & Reasoning",
        "notable_products": ["DeepSeek-V3", "DeepSeek-R1", "DeepSeek Coder"],
        "funding_stage": "Private Research Firm",
        "employee_count": "100-250",
        "description": "DeepSeek is an artificial intelligence research organization renowned for developing cutting-edge open-weights reasoning models and novel MoE architectures. It gained global prominence by proving that frontier-level reasoning benchmarks can be achieved with radical hardware and token efficiency."
    },
    {
        "name": "xAI",
        "url": "https://x.ai",
        "founding_year": 2023,
        "headquarters": "San Francisco, CA",
        "industry_sector": "Frontier AI & Scientific Reasoning",
        "notable_products": ["Grok-2", "Grok Vision", "Colossus Supercomputer"],
        "funding_stage": "Series B ($50B valuation)",
        "employee_count": "100-250",
        "description": "xAI is an AI company founded by Elon Musk with the mission to understand the true nature of the universe through advanced mathematical and physical reasoning. It deployed the Colossus 100k liquid-cooled H100 supercomputer cluster in Memphis to train the Grok model family."
    },
    {
        "name": "Figure AI",
        "url": "https://figure.ai",
        "founding_year": 2022,
        "headquarters": "Sunnyvale, CA",
        "industry_sector": "Autonomous Humanoid Robotics",
        "notable_products": ["Figure 01", "Figure 02"],
        "funding_stage": "Series B ($2.6B valuation)",
        "employee_count": "100-250",
        "description": "Figure AI develops autonomous general-purpose humanoid robots designed to deploy dexterous labor across manufacturing, logistics, and warehousing. In partnership with OpenAI and BMW, it integrates vision-language intelligence directly into robotic actuation for real-world manipulation."
    },
    {
        "name": "Anysphere",
        "url": "https://cursor.com",
        "founding_year": 2022,
        "headquarters": "San Francisco, CA",
        "industry_sector": "AI Developer Environments",
        "notable_products": ["Cursor Code Editor", "Cursor Composer"],
        "funding_stage": "Series A ($400M+ valuation)",
        "employee_count": "20-50",
        "description": "Anysphere is the AI research lab behind Cursor, an AI-native code editor built as a fork of VS Code with deeply integrated frontier models. Its Composer feature orchestrates multi-file code modifications, codebase indexing, and conversational terminal debugging."
    },
    {
        "name": "NVIDIA",
        "url": "https://nvidia.com",
        "founding_year": 1993,
        "headquarters": "Santa Clara, CA",
        "industry_sector": "Accelerated Computing & AI Hardware",
        "notable_products": ["H100 Tensor Core GPU", "Blackwell B200", "CUDA", "NVIDIA NIM"],
        "funding_stage": "Public (NASDAQ: NVDA)",
        "employee_count": "10000+",
        "description": "NVIDIA is the global leader in accelerated computing hardware, graphics processing units, and high-performance interconnects driving modern AI. Its CUDA software ecosystem, Tensor Core architectures, and Blackwell platform power virtually all frontier generative training clusters globally."
    },
    {
        "name": "Databricks",
        "url": "https://databricks.com",
        "founding_year": 2013,
        "headquarters": "San Francisco, CA",
        "industry_sector": "Data Intelligence & Lakehouse",
        "notable_products": ["Databricks Lakehouse", "Mosaic AI", "DBRX Foundation Model"],
        "funding_stage": "Series I ($43B valuation)",
        "employee_count": "5000+",
        "description": "Databricks is a data intelligence platform that combines data engineering, analytics, and machine learning into a unified Lakehouse architecture. Through its Mosaic AI acquisition, it empowers enterprises to train custom generative models and build governed RAG solutions atop proprietary corporate data."
    },
    {
        "name": "Groq",
        "url": "https://groq.com",
        "founding_year": 2016,
        "headquarters": "Mountain View, CA",
        "industry_sector": "Ultra-Fast AI Inference Hardware",
        "notable_products": ["LPU Inference Engine", "GroqCloud"],
        "funding_stage": "Series D ($2.8B valuation)",
        "employee_count": "250-500",
        "description": "Groq builds the Language Processing Unit (LPU), an innovative deterministic processor architecture optimized specifically for ultra-low latency sequential inference. Its GroqCloud delivers record-setting generation speeds exceeding 500 tokens per second on open-weights LLMs like Llama and Mistral."
    },
    {
        "name": "Harvey",
        "url": "https://harvey.ai",
        "founding_year": 2022,
        "headquarters": "San Francisco, CA",
        "industry_sector": "Legal AI Platform",
        "notable_products": ["Harvey Assistant", "Contract Analysis Engine"],
        "funding_stage": "Series C ($1.5B valuation)",
        "employee_count": "100-250",
        "description": "Harvey develops domain-specific generative AI solutions custom-tailored for premier corporate law firms, in-house counsel, and professional service institutions. Partnering with OpenAI, it automates complex contract analysis, regulatory due diligence, and legal research across global jurisdictions."
    },
    {
        "name": "Writer",
        "url": "https://writer.com",
        "founding_year": 2020,
        "headquarters": "San Francisco, CA",
        "industry_sector": "Full-Stack Enterprise Generative AI",
        "notable_products": ["Palmyra LLMs", "Writer Knowledge Graph", "Writer AI Studio"],
        "funding_stage": "Series C ($1.9B valuation)",
        "employee_count": "250-500",
        "description": "Writer is a full-stack generative AI platform designed for enterprise operations, marketing, and product development teams. Its proprietary Palmyra model family and integrated Knowledge Graph enforce corporate brand guidelines, factual precision, and strict enterprise security governance."
    },
    {
        "name": "Synthesia",
        "url": "https://synthesia.io",
        "founding_year": 2017,
        "headquarters": "London, United Kingdom",
        "industry_sector": "AI Avatar Video Generation",
        "notable_products": ["Synthesia STUDIO", "Expressive Avatars"],
        "funding_stage": "Series C ($1B valuation)",
        "employee_count": "250-500",
        "description": "Synthesia is a generative video platform that transforms standard text scripts into realistic presentation videos featuring photorealistic AI avatars. It enables corporate enterprises to produce multilingual training, sales enablement, and customer support videos without cameras, microphones, or studio sets."
    },
    {
        "name": "Character.AI",
        "url": "https://character.ai",
        "founding_year": 2021,
        "headquarters": "Menlo Park, CA",
        "industry_sector": "Conversational Entertainment & Companions",
        "notable_products": ["Character.AI Web/Mobile", "Character Voice"],
        "funding_stage": "Strategic Licensing (Google)",
        "employee_count": "100-250",
        "description": "Character.AI is a consumer conversational AI platform founded by Transformer co-authors Noam Shazeer and Daniel De Freitas. It allows millions of global users to create, share, and converse with adaptable persona-driven virtual companions across creative writing, education, and entertainment."
    }
]

def extract() -> list[dict]:
    """Extract prominent AI startups, foundation labs, and enterprise infrastructure providers."""
    entities = []
    for c in COMPANIES:
        entity = normalize(
            raw={
                "name": c["name"],
                "description": c["description"],
                "url": c["url"],
                "categories": ["company", "AI", c["industry_sector"]],
                "founding_year": c["founding_year"],
                "headquarters": c["headquarters"],
                "industry_sector": c["industry_sector"],
                "notable_products": c["notable_products"],
                "funding_stage": c["funding_stage"],
                "employee_count": c["employee_count"],
            },
            entity_type="company",
            source_name="Official Company Profiles",
            source_url=c["url"],
        )
        entities.append(entity)
    return entities
