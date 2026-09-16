# src/extractors/new_entities.py
from src.normalizer import normalize

NEW_ENTITIES = [
    {
        "name": "DeepSeek-R1",
        "url": "https://deepseek.com",
        "launch_date": "2025-01",
        "entity_subtype": "model",
        "launch_source": "Official Research Blog",
        "hype_level": "High",
        "description": "DeepSeek-R1 is an open-weights reasoning model developed through large-scale reinforcement learning without prior supervised fine-tuning warmups. It demonstrated that self-generated chains-of-thought and verification rewards can match proprietary reasoning benchmarks while open-sourcing all training weights and recipes."
    },
    {
        "name": "Manus",
        "url": "https://manus.im",
        "launch_date": "2025-03",
        "entity_subtype": "agent",
        "launch_source": "ProductHunt & Global Launch",
        "hype_level": "High",
        "description": "Manus is a general-purpose autonomous AI agent designed to execute multi-step digital workflows across web research, financial analysis, and software development. Operating asynchronously in cloud browser environments, it navigates websites, creates documents, and executes code to deliver finished deliverables."
    },
    {
        "name": "Google Jules",
        "url": "https://jules.google",
        "launch_date": "2024-12",
        "entity_subtype": "agent",
        "launch_source": "Google Research",
        "hype_level": "High",
        "description": "Google Jules is an autonomous coding agent that integrates directly into GitHub workflows to clone repositories, run unit tests, and resolve open bug issues. Operating as an asynchronous pull request collaborator, it reviews code diffs and writes regression tests before proposing fixes."
    },
    {
        "name": "Apple Intelligence",
        "url": "https://www.apple.com/apple-intelligence/",
        "launch_date": "2024-10",
        "entity_subtype": "platform",
        "launch_source": "Apple WWDC",
        "hype_level": "High",
        "description": "Apple Intelligence is a personal intelligence system deeply integrated into iOS, iPadOS, and macOS that combines on-device neural models with Private Cloud Compute. It powers system-wide writing tools, image clean-up utilities, priority notifications, and context-aware Siri actions while safeguarding personal user privacy."
    },
    {
        "name": "GPT-4o mini",
        "url": "https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/",
        "launch_date": "2024-07",
        "entity_subtype": "model",
        "launch_source": "OpenAI Announcements",
        "hype_level": "High",
        "description": "GPT-4o mini is OpenAI's cost-efficient small language model supporting 128k token context windows and multimodal text and vision processing. Designed to replace GPT-3.5 Turbo at a fraction of the inference cost, it enables scalable agentic workflows, document processing, and customer support bots."
    },
    {
        "name": "Claude 3.5 Haiku",
        "url": "https://www.anthropic.com/news/claude-3-5-haiku",
        "launch_date": "2024-11",
        "entity_subtype": "model",
        "launch_source": "Anthropic Newsroom",
        "hype_level": "High",
        "description": "Claude 3.5 Haiku is Anthropic's fastest and most cost-effective frontier model, matching the coding and reasoning benchmark performance of the previous flagship Claude 3 Opus. It is optimized for high-speed sub-agent execution, high-volume data extraction, and real-time interactive user interfaces."
    },
    {
        "name": "Gemini 2.0 Flash",
        "url": "https://deepmind.google/technologies/gemini/flash/",
        "launch_date": "2024-12",
        "entity_subtype": "model",
        "launch_source": "Google DeepMind",
        "hype_level": "High",
        "description": "Gemini 2.0 Flash is Google DeepMind's next-generation multimodal model engineered for low-latency real-time agentic experiences. It introduces native streaming audio input and output, real-time spatial video understanding, and multi-modal tool-calling capabilities at fast response speeds."
    },
    {
        "name": "Qwen QwQ-32B",
        "url": "https://qwenlm.github.io/blog/qwq-32b-preview/",
        "launch_date": "2024-11",
        "entity_subtype": "model",
        "launch_source": "Alibaba Cloud",
        "hype_level": "Medium",
        "description": "Qwen QwQ-32B is an experimental open-weights reasoning model from Alibaba Cloud that incorporates step-by-step thinking for complex mathematical deduction and coding challenges. It achieves benchmark scores competitive with much larger proprietary models while running on consumer workstations."
    },
    {
        "name": "Lovable",
        "url": "https://lovable.dev",
        "launch_date": "2024-10",
        "entity_subtype": "tool",
        "launch_source": "ProductHunt",
        "hype_level": "High",
        "description": "Lovable is an AI software engineer that generates full-stack web applications, landing pages, and internal admin panels from natural language conversations. It provides instant live browser previews, synchronized GitHub code commits, and seamless backend Supabase database integration."
    },
    {
        "name": "Bolt.new",
        "url": "https://bolt.new",
        "launch_date": "2024-09",
        "entity_subtype": "tool",
        "launch_source": "StackBlitz Announcement",
        "hype_level": "High",
        "description": "Bolt.new is an in-browser development environment powered by StackBlitz WebContainers that prompts, executes, and deploys full-stack web applications without requiring local software installations. It provides live container execution of Node.js servers, npm dependencies, and frontend frameworks."
    },
    {
        "name": "Cursor 0.40",
        "url": "https://cursor.com/blog",
        "launch_date": "2024-09",
        "entity_subtype": "tool",
        "launch_source": "Anysphere Blog",
        "hype_level": "High",
        "description": "Cursor 0.40 introduced Composer, an agentic multi-file code editing canvas that allows software engineers to orchestrate complex architectural refactors across entire repositories simultaneously. It incorporates speculative code edits and terminal command execution within a cohesive developer interface."
    },
    {
        "name": "NotebookLM",
        "url": "https://notebooklm.google.com",
        "launch_date": "2024-06",
        "entity_subtype": "tool",
        "launch_source": "Google I/O",
        "hype_level": "High",
        "description": "NotebookLM is a personalized AI research assistant created by Google that grounds its responses exclusively in user-uploaded documents, PDFs, and notes. Its standout Audio Overview feature autonomously synthesizes complex source material into engaging, lifelike two-host podcast discussions."
    },
    {
        "name": "OpenAI o1",
        "url": "https://openai.com/o1/",
        "launch_date": "2024-09",
        "entity_subtype": "model",
        "launch_source": "OpenAI Announcements",
        "hype_level": "High",
        "description": "OpenAI o1 is a reasoning foundation model designed to spend more time thinking before answering, using reinforcement learning to generate private chains of thought. It demonstrates doctoral-level problem-solving capabilities across competitive programming, advanced physics, and mathematical Olympiads."
    }
]

def extract() -> list[dict]:
    """Extract recently launched high-impact AI models, agents, and applications."""
    entities = []
    for n in NEW_ENTITIES:
        entity = normalize(
            raw={
                "name": n["name"],
                "description": n["description"],
                "url": n["url"],
                "categories": ["new", "recent-launch", n["entity_subtype"]],
                "launch_date": n["launch_date"],
                "entity_subtype": n["entity_subtype"],
                "launch_source": n["launch_source"],
                "hype_level": n["hype_level"],
            },
            entity_type="new",
            source_name=n["launch_source"],
            source_url=n["url"],
        )
        entities.append(entity)
    return entities
