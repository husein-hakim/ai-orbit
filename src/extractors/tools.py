# src/extractors/tools.py
from src.normalizer import normalize

TOOLS = [
    {
        "name": "ChatGPT",
        "url": "https://chatgpt.com",
        "company": "OpenAI",
        "primary_category": "Conversational Assistant",
        "pricing": "Freemium",
        "platforms": ["Web", "macOS", "Windows", "iOS", "Android"],
        "api_available": True,
        "description": "ChatGPT is OpenAI's flagship conversational artificial intelligence service powered by the GPT-4o and OpenAI o1 reasoning model series. It assists users with writing, brainstorming, analytical coding, mathematics, and live voice interactions across desktop and mobile devices."
    },
    {
        "name": "Claude.ai",
        "url": "https://claude.ai",
        "company": "Anthropic",
        "primary_category": "Conversational Assistant",
        "pricing": "Freemium",
        "platforms": ["Web", "macOS", "Windows", "iOS", "Android"],
        "api_available": True,
        "description": "Claude.ai is Anthropic's browser and desktop assistant interface featuring the Claude 3.5 Sonnet and Haiku foundation models. It incorporates Artifacts for real-time visualization of code and mockups, alongside Project Workspaces for managing specialized enterprise knowledge contexts."
    },
    {
        "name": "Gemini",
        "url": "https://gemini.google.com",
        "company": "Google",
        "primary_category": "Conversational Assistant",
        "pricing": "Freemium",
        "platforms": ["Web", "iOS", "Android", "Workspace"],
        "api_available": True,
        "description": "Gemini is Google's consumer AI assistant natively integrated with Google Workspace, YouTube, Google Maps, and Flights. It leverages Gemini 1.5 Pro's long-context multimodal reasoning to parse complex user files, summarize documents, and generate creative multimedia outputs."
    },
    {
        "name": "Cursor",
        "url": "https://cursor.com",
        "company": "Anysphere",
        "primary_category": "AI Code Editor",
        "pricing": "Freemium",
        "platforms": ["macOS", "Windows", "Linux"],
        "api_available": False,
        "description": "Cursor is an AI-first code editor designed for software engineering efficiency, built upon a high-performance fork of Visual Studio Code. It features full-codebase vector semantic indexing, terminal command prediction, and a Composer interface for executing complex multi-file codebase edits."
    },
    {
        "name": "GitHub Copilot",
        "url": "https://github.com/features/copilot",
        "company": "GitHub",
        "primary_category": "Code Generation & Autocomplete",
        "pricing": "Paid",
        "platforms": ["VS Code", "Visual Studio", "JetBrains IDEs", "Neovim"],
        "api_available": True,
        "description": "GitHub Copilot is an AI pair programmer that provides context-aware inline code suggestions, docstring generation, and automated unit test authoring directly within modern IDEs. It supports enterprise repository indexing and natural language chat assistance across thousands of software frameworks."
    },
    {
        "name": "Midjourney",
        "url": "https://midjourney.com",
        "company": "Midjourney",
        "primary_category": "Visual Generation & Art",
        "pricing": "Paid",
        "platforms": ["Discord", "Web Canvas"],
        "api_available": False,
        "description": "Midjourney is a text-to-image synthesis tool widely recognized for its high aesthetic fidelity, photorealism, and nuanced stylistic rendering. Accessible via Discord and dedicated web interfaces, it provides professional artists with inpainting, outpainting, and character consistency controls."
    },
    {
        "name": "Perplexity",
        "url": "https://perplexity.ai",
        "company": "Perplexity AI",
        "primary_category": "AI Search Engine",
        "pricing": "Freemium",
        "platforms": ["Web", "iOS", "Android", "macOS"],
        "api_available": True,
        "description": "Perplexity is an AI-powered conversational search platform that provides comprehensive, citation-backed answers to natural language questions in real time. It unifies web indexing with LLM reasoning, allowing users to verify assertions directly against reputable source references."
    },
    {
        "name": "Notion AI",
        "url": "https://notion.so/product/ai",
        "company": "Notion",
        "primary_category": "Workplace Productivity",
        "pricing": "Paid",
        "platforms": ["Web", "macOS", "Windows", "iOS", "Android"],
        "api_available": False,
        "description": "Notion AI is a connected workplace intelligence assistant embedded directly within the Notion productivity workspace. It enables knowledge workers to search company databases with natural language, synthesize meeting action items, and draft business documentation in seconds."
    },
    {
        "name": "Runway Gen-3",
        "url": "https://runwayml.com",
        "company": "Runway",
        "primary_category": "Video Generation & Editing",
        "pricing": "Freemium",
        "platforms": ["Web", "iOS"],
        "api_available": True,
        "description": "Runway Gen-3 Alpha is a state-of-the-art generative video system capable of creating photorealistic, cinema-grade video clips from text prompts or reference still imagery. It provides motion brush controls, realistic camera trajectory panning, and consistent character physics."
    },
    {
        "name": "ElevenLabs",
        "url": "https://elevenlabs.io",
        "company": "ElevenLabs",
        "primary_category": "Speech Synthesis & Voice AI",
        "pricing": "Freemium",
        "platforms": ["Web", "API", "iOS"],
        "api_available": True,
        "description": "ElevenLabs provides realistic voice generation, instant zero-shot voice cloning, and multilingual audio dubbing for digital media creators and software developers. Its models capture emotional subtleties, vocal pauses, and human cadence across 29 languages."
    },
    {
        "name": "Suno",
        "url": "https://suno.com",
        "company": "Suno AI",
        "primary_category": "Music Generation",
        "pricing": "Freemium",
        "platforms": ["Web", "iOS"],
        "api_available": False,
        "description": "Suno is a generative music platform that transforms natural language prompts into complete musical compositions with vocal tracks, instrumental arrangements, and lyrics. It supports diverse genres from acoustic folk to electronic pop, democratizing music creation for creators."
    },
    {
        "name": "Udio",
        "url": "https://udio.com",
        "company": "Udio",
        "primary_category": "Music Generation",
        "pricing": "Freemium",
        "platforms": ["Web"],
        "api_available": False,
        "description": "Udio is an AI music creation service founded by former Google DeepMind researchers that synthesizes full fidelity songs across classical, jazz, and modern electronic styles. It offers granular structural controls including intro customization, sectional stem extension, and vocal customization."
    },
    {
        "name": "v0",
        "url": "https://v0.dev",
        "company": "Vercel",
        "primary_category": "Frontend UI Generation",
        "pricing": "Freemium",
        "platforms": ["Web"],
        "api_available": True,
        "description": "v0 is a generative frontend user interface tool created by Vercel that converts natural language prompts and UI screenshots into clean React and Tailwind CSS components. It allows developers to iteratively design and immediately copy accessible UI components into production web projects."
    },
    {
        "name": "Bolt.new",
        "url": "https://bolt.new",
        "company": "StackBlitz",
        "primary_category": "Full-Stack Web App Builder",
        "pricing": "Freemium",
        "platforms": ["Web"],
        "api_available": False,
        "description": "Bolt.new is an in-browser AI development environment powered by WebContainers that prompts, creates, runs, and deploys full-stack web applications entirely inside the browser. It enables real-time execution of Node.js servers, npm dependencies, and frontend frameworks with zero local setup."
    },
    {
        "name": "Lovable",
        "url": "https://lovable.dev",
        "company": "Lovable",
        "primary_category": "Full-Stack Web App Builder",
        "pricing": "Freemium",
        "platforms": ["Web"],
        "api_available": False,
        "description": "Lovable is an AI software engineer platform designed to build polished full-stack web applications, landing pages, and internal SaaS dashboards from conversational prompts. It integrates database connectivity, GitHub repository synchronization, and rapid cloud deployment."
    },
    {
        "name": "Replit AI",
        "url": "https://replit.com",
        "company": "Replit",
        "primary_category": "Cloud Software Development",
        "pricing": "Freemium",
        "platforms": ["Web", "iOS", "Android"],
        "api_available": True,
        "description": "Replit AI is an autonomous software development assistant integrated directly into Replit's cloud computing and hosting platform. It generates complete web apps, debugs runtime terminal stack traces, and provisions cloud hosting infrastructure automatically through chat prompts."
    },
    {
        "name": "Grammarly AI",
        "url": "https://grammarly.com",
        "company": "Grammarly",
        "primary_category": "Writing Assistant & Communications",
        "pricing": "Freemium",
        "platforms": ["Web", "Chrome", "macOS", "Windows", "iOS"],
        "api_available": True,
        "description": "Grammarly AI provides contextual writing enhancement, tone adjustment, and automated document synthesis across email clients, web browsers, and enterprise word processors. It helps professionals accelerate document drafting while preserving individual voice and brand clarity."
    },
    {
        "name": "Ollama",
        "url": "https://ollama.com",
        "company": "Ollama",
        "primary_category": "Local LLM Runtime",
        "pricing": "Free",
        "platforms": ["macOS", "Linux", "Windows"],
        "api_available": True,
        "description": "Ollama is a local deployment and inference application that allows developers to run open-weights language models like Llama, Mistral, and DeepSeek privately on their personal computers. It features an OpenAI-compatible HTTP API, automatic GPU hardware detection, and an intuitive CLI interface."
    },
    {
        "name": "LM Studio",
        "url": "https://lmstudio.ai",
        "company": "LM Studio",
        "primary_category": "Local LLM Desktop App",
        "pricing": "Free",
        "platforms": ["macOS", "Windows", "Linux"],
        "api_available": True,
        "description": "LM Studio is an intuitive desktop graphical application that lets users discover, download, and run any GGUF quantized language model entirely offline on consumer laptops and workstations. It includes chat testing playgrounds and an embedded local inference server."
    },
    {
        "name": "Claude Code",
        "url": "https://docs.anthropic.com/en/docs/agents-and-tools/claude-code",
        "company": "Anthropic",
        "primary_category": "CLI Agentic Coding Tool",
        "pricing": "Paid (API Usage)",
        "platforms": ["macOS", "Linux", "Windows"],
        "api_available": True,
        "description": "Claude Code is an agentic command-line interface tool created by Anthropic that connects directly into developers' local terminal environments. It leverages native Model Context Protocol (MCP) tool bindings to read directories, edit files, execute test suites, and perform Git commits autonomously."
    },
    {
        "name": "Phind",
        "url": "https://phind.com",
        "company": "Phind",
        "primary_category": "AI Search for Developers",
        "pricing": "Freemium",
        "platforms": ["Web", "VS Code Extension"],
        "api_available": True,
        "description": "Phind is an intelligent search and answer engine custom-engineered for software developers and technical architects. It searches technical documentation, GitHub issues, and Stack Overflow discussions, generating executable code snippets and comprehensive architectural guidance."
    },
    {
        "name": "Descript",
        "url": "https://descript.com",
        "company": "Descript",
        "primary_category": "Audio & Video Editing",
        "pricing": "Freemium",
        "platforms": ["macOS", "Windows", "Web"],
        "api_available": False,
        "description": "Descript is an AI-powered media production suite that allows podcasters and video creators to edit audio and video as simply as editing a text document. It provides automated transcription, studio sound background noise removal, filler word cleanup, and Overdub voice synthesis."
    }
]

def extract() -> list[dict]:
    """Extract widely used AI applications and developer tools."""
    entities = []
    for t in TOOLS:
        entity = normalize(
            raw={
                "name": t["name"],
                "description": t["description"],
                "url": t["url"],
                "categories": ["tool", "software", t["primary_category"]],
                "pricing": t["pricing"],
                "platforms": t["platforms"],
                "primary_category": t["primary_category"],
                "api_available": t["api_available"],
                "company": t["company"],
            },
            entity_type="tool",
            source_name="Official Tool Registry",
            source_url=t["url"],
        )
        entities.append(entity)
    return entities
