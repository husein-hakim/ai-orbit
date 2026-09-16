# src/relationship_mapper.py
import uuid
from datetime import datetime

def make_rel_id(subject_id: str, predicate: str, object_id: str) -> str:
    """Generate deterministic UUID for relationships."""
    key = f"{subject_id}:{predicate}:{object_id}"
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, key))

CANONICAL_RELATIONSHIPS = [
    # Company -> develops -> Model
    ("Anthropic", "develops", "Claude 3.5 Sonnet", "model"),
    ("Anthropic", "develops", "Claude 3.5 Haiku", "model"),
    ("OpenAI", "develops", "GPT-4o", "model"),
    ("OpenAI", "develops", "GPT-4o mini", "model"),
    ("OpenAI", "develops", "OpenAI o1", "model"),
    ("Google DeepMind", "develops", "Gemini 1.5 Pro", "model"),
    ("Google DeepMind", "develops", "Gemini 2.0 Flash", "model"),
    ("Google DeepMind", "develops", "Gemma 2 27B", "model"),
    ("Meta", "develops", "Llama 3.1 405B", "model"),
    ("Mistral AI", "develops", "Mistral Large 2", "model"),
    ("DeepSeek", "develops", "DeepSeek-V3", "model"),
    ("DeepSeek", "develops", "DeepSeek-R1", "model"),
    ("Microsoft", "develops", "Phi-3 Mini", "model"),
    ("Cohere", "develops", "Cohere Command R+", "model"),
    ("Stability AI", "develops", "Stable Diffusion 3.5 Large", "model"),
    ("Stability AI", "develops", "Stable Diffusion", "creative"),
    ("OpenAI", "develops", "Whisper Large v3", "model"),
    ("OpenAI", "develops", "DALL-E 3", "creative"),

    # Company -> develops -> Tool
    ("Anthropic", "develops", "Claude.ai", "tool"),
    ("Anthropic", "develops", "Claude Code", "tool"),
    ("OpenAI", "develops", "ChatGPT", "tool"),
    ("Google", "develops", "Gemini", "tool"),
    ("Anysphere", "develops", "Cursor", "tool"),
    ("GitHub", "develops", "GitHub Copilot", "tool"),
    ("Perplexity AI", "develops", "Perplexity", "tool"),
    ("Runway", "develops", "Runway Gen-3", "tool"),
    ("ElevenLabs", "develops", "ElevenLabs", "tool"),
    ("Suno AI", "develops", "Suno", "tool"),
    ("Udio", "develops", "Udio", "tool"),
    ("Vercel", "develops", "v0", "tool"),
    ("StackBlitz", "develops", "Bolt.new", "tool"),
    ("Lovable", "develops", "Lovable", "tool"),
    ("Replit", "develops", "Replit AI", "tool"),
    ("Grammarly", "develops", "Grammarly AI", "tool"),
    ("Ollama", "develops", "Ollama", "tool"),
    ("LM Studio", "develops", "LM Studio", "tool"),
    ("Phind", "develops", "Phind", "tool"),
    ("Descript", "develops", "Descript", "tool"),
    ("LangChain", "develops", "LangChain", "repository"),

    # Company -> makes -> Device / Hardware
    ("NVIDIA", "makes", "NVIDIA H100 Tensor Core GPU", "device"),
    ("NVIDIA", "makes", "NVIDIA Blackwell B200 GPU", "device"),
    ("NVIDIA", "makes", "NVIDIA Jetson AGX Orin", "device"),
    ("Apple", "makes", "Apple M4 Pro", "device"),
    ("Apple", "makes", "Apple Vision Pro", "device"),
    ("AMD", "makes", "AMD Instinct MI300X", "device"),
    ("Google", "makes", "Google TPU v5e", "device"),
    ("Intel", "makes", "Intel Gaudi 3", "device"),
    ("Rabbit Inc", "makes", "Rabbit r1", "device"),
    ("Brilliant Labs", "makes", "Frame AI Glasses", "device"),

    # Company -> makes -> Robot
    ("Figure AI", "makes", "Figure 02", "robot"),
    ("Tesla", "makes", "Optimus Gen 2", "robot"),
    ("Boston Dynamics", "makes", "Spot", "robot"),
    ("Boston Dynamics", "makes", "Atlas (Electric)", "robot"),
    ("Boston Dynamics", "makes", "Stretch", "robot"),
    ("Agility Robotics", "makes", "Digit", "robot"),
    ("Unitree Robotics", "makes", "Unitree H1", "robot"),
    ("1X Technologies", "makes", "1X Neo", "robot"),
    ("Apptronik", "makes", "Apptronik Apollo", "robot"),
    ("Sanctuary AI", "makes", "Sanctuary Phoenix", "robot"),

    # Tool -> built_on -> Model
    ("ChatGPT", "built_on", "GPT-4o", "model"),
    ("Claude.ai", "built_on", "Claude 3.5 Sonnet", "model"),
    ("Claude Code", "built_on", "Claude 3.5 Sonnet", "model"),
    ("Gemini", "built_on", "Gemini 1.5 Pro", "model"),
    ("Cursor", "built_on", "Claude 3.5 Sonnet", "model"),
    ("GitHub Copilot", "built_on", "GPT-4o", "model"),
    ("NotebookLM", "built_on", "Gemini 1.5 Pro", "model"),

    # Model -> runs_on -> Device
    ("Llama 3.1 405B", "runs_on", "NVIDIA H100 Tensor Core GPU", "device"),
    ("DeepSeek-V3", "runs_on", "NVIDIA H100 Tensor Core GPU", "device"),
    ("DeepSeek-R1", "runs_on", "NVIDIA H100 Tensor Core GPU", "device"),
    ("GPT-4o", "runs_on", "NVIDIA Blackwell B200 GPU", "device"),
    ("Gemini 1.5 Pro", "runs_on", "Google TPU v5e", "device"),
    ("Phi-3 Mini", "runs_on", "Apple M4 Pro", "device"),
    ("Gemma 2 27B", "runs_on", "NVIDIA Jetson AGX Orin", "device"),

    # Tool -> solves -> Task
    ("GitHub Copilot", "solves", "Write code faster with AI", "task"),
    ("Cursor", "solves", "Write code faster with AI", "task"),
    ("Claude Code", "solves", "Write code faster with AI", "task"),
    ("Cursor", "solves", "Debug code automatically", "task"),
    ("Claude.ai", "solves", "Summarize long documents", "task"),
    ("ChatGPT", "solves", "Summarize long documents", "task"),
    ("Midjourney", "solves", "Generate images from text prompts", "task"),
    ("DALL-E 3", "solves", "Generate images from text prompts", "task"),
    ("Perplexity", "solves", "Search the web with AI answers", "task"),
    ("Whisper Large v3", "solves", "Transcribe audio to text", "task"),
    ("Runway Gen-3", "solves", "Generate videos from text", "task"),
    ("ElevenLabs", "solves", "Convert text to realistic speech", "task"),
    ("Suno", "solves", "Generate music from text", "task"),
    ("Udio", "solves", "Generate music from text", "task"),
    ("v0", "solves", "Build software without coding", "task"),
    ("Bolt.new", "solves", "Build software without coding", "task"),
    ("Lovable", "solves", "Build software without coding", "task"),
    ("Grammarly AI", "solves", "Draft and refine emails", "task"),
    ("NotebookLM", "solves", "Research topics comprehensively", "task"),

    # Company -> competitor_of -> Company
    ("Anthropic", "competitor_of", "OpenAI", "company"),
    ("Mistral AI", "competitor_of", "OpenAI", "company"),
    ("xAI", "competitor_of", "OpenAI", "company"),
    ("Perplexity AI", "competitor_of", "Google DeepMind", "company"),
    ("Midjourney", "competitor_of", "Stability AI", "company"),
    ("Suno AI", "competitor_of", "Udio", "company"),
    ("Figure AI", "competitor_of", "Tesla", "company"),
    ("AMD", "competitor_of", "NVIDIA", "company"),
    ("Intel", "competitor_of", "NVIDIA", "company"),

    # Video -> tutorial_for -> Tool / Model / Framework
    ("Let's build GPT: from scratch, in code, spelled out", "tutorial_for", "GPT-4o", "model"),
    ("Attention in transformers, visually explained", "tutorial_for", "huggingface/transformers", "repository"),
    ("Building Autonomous AI Agents with LangGraph and MCP", "tutorial_for", "langchain-ai/langchain", "repository"),
    ("Cursor AI: The Code Editor That Changes Everything", "tutorial_for", "Cursor", "tool"),
    ("DeepSeek-V3 Explained: MoE Architecture and Breakthrough Efficiency", "tutorial_for", "DeepSeek-V3", "model"),
    ("Building Production RAG Systems: Chunking, Embeddings, and Reranking", "tutorial_for", "run-llama/llama_index", "repository"),

    # Entity -> part_of -> Collection
    ("awesome-mcp-servers", "part_of", "awesome-mcp-servers", "collection"),
    ("langchain-ai/langchain", "part_of", "awesome-llm", "collection"),
    ("run-llama/llama_index", "part_of", "awesome-llm", "collection"),
    ("Llama 3.1 405B", "part_of", "OpenLLM Leaderboard", "collection"),
    ("Claude 3.5 Sonnet", "part_of", "LMSYS Chatbot Arena", "collection"),
    ("GPT-4o", "part_of", "LMSYS Chatbot Arena", "collection"),
    ("Gemini 1.5 Pro", "part_of", "LMSYS Chatbot Arena", "collection"),
    ("DeepSeek-V3", "part_of", "LMSYS Chatbot Arena", "collection"),

    # News -> featured_in / reports_on
    ("Anthropic Launches Claude 3.5 Sonnet Setting New Coding Standard", "featured_in", "Claude 3.5 Sonnet", "model"),
    ("OpenAI Introduces GPT-4o with Native Real-Time Multimodal Capabilities", "featured_in", "GPT-4o", "model"),
    ("Meta Open-Sources Llama 3.1 405B to Champion Open AI Ecosystems", "featured_in", "Llama 3.1 405B", "model"),
    ("DeepSeek Releases DeepSeek-V3 Disrupting Frontier AI Economics", "featured_in", "DeepSeek-V3", "model"),
    ("Google DeepMind Unveils Gemini 1.5 Pro with Breakthrough 2M Context Window", "featured_in", "Gemini 1.5 Pro", "model"),
]

def build_relationships(all_entities: list[dict]) -> dict:
    """
    Construct the ecosystem relationship graph by matching entities.
    """
    entity_by_type_name = {}
    entity_by_name = {}

    for e in all_entities:
        name = e.get("name", "").strip().lower()
        etype = e.get("entity_type", "").strip().lower()
        entity_by_type_name[(etype, name)] = e
        if name not in entity_by_name:
            entity_by_name[name] = e
        
        # Index short names for convenient lookups
        short = name.split(" ")[0].lower()
        if (etype, short) not in entity_by_type_name:
            entity_by_type_name[(etype, short)] = e
        if short not in entity_by_name:
            entity_by_name[short] = e

    relationships = []
    seen_rel_ids = set()

    # 1. Process canonical relationships
    for s_name, predicate, o_name, obj_expected_type in CANONICAL_RELATIONSHIPS:
        s_ent = entity_by_name.get(s_name.lower())
        o_ent = entity_by_type_name.get((obj_expected_type.lower(), o_name.lower())) or entity_by_name.get(o_name.lower())
        
        if s_ent and o_ent and s_ent["id"] != o_ent["id"]:
            rel_id = make_rel_id(s_ent["id"], predicate, o_ent["id"])
            if rel_id not in seen_rel_ids:
                seen_rel_ids.add(rel_id)
                relationships.append({
                    "id": rel_id,
                    "subject_id": s_ent["id"],
                    "subject_name": s_ent["name"],
                    "subject_type": s_ent["entity_type"],
                    "predicate": predicate,
                    "object_id": o_ent["id"],
                    "object_name": o_ent["name"],
                    "object_type": o_ent["entity_type"],
                    "confidence": 1.0,
                    "source": "canonical_ecosystem_graph"
                })

    # 2. Dynamic MCP relationships: MCP -> integrates_with -> Supported Clients / Tools
    for e in all_entities:
        if e.get("entity_type") == "mcp":
            supported = e.get("supported_clients", [])
            if isinstance(supported, str):
                supported = [s.strip() for s in supported.split(",")]
            
            for client in supported:
                c_ent = entity_by_name.get(client.lower())
                if c_ent and c_ent["id"] != e["id"]:
                    rel_id = make_rel_id(e["id"], "integrates_with", c_ent["id"])
                    if rel_id not in seen_rel_ids:
                        seen_rel_ids.add(rel_id)
                        relationships.append({
                            "id": rel_id,
                            "subject_id": e["id"],
                            "subject_name": e["name"],
                            "subject_type": "mcp",
                            "predicate": "integrates_with",
                            "object_id": c_ent["id"],
                            "object_name": c_ent["name"],
                            "object_type": c_ent["entity_type"],
                            "confidence": 0.95,
                            "source": "mcp_client_compatibility"
                        })

    # 3. Dynamic Tool -> Task relationships: Tool -> solves -> Task
    for e in all_entities:
        if e.get("entity_type") == "task":
            tools = e.get("tools_that_solve_this", [])
            for t_name in tools:
                t_ent = entity_by_name.get(t_name.lower())
                if t_ent and t_ent["id"] != e["id"]:
                    rel_id = make_rel_id(t_ent["id"], "solves", e["id"])
                    if rel_id not in seen_rel_ids:
                        seen_rel_ids.add(rel_id)
                        relationships.append({
                            "id": rel_id,
                            "subject_id": t_ent["id"],
                            "subject_name": t_ent["name"],
                            "subject_type": t_ent["entity_type"],
                            "predicate": "solves",
                            "object_id": e["id"],
                            "object_name": e["name"],
                            "object_type": "task",
                            "confidence": 0.90,
                            "source": "task_solution_mapping"
                        })

    # 4. Dynamic Company -> Product relationships: Company -> develops/makes -> Product
    for e in all_entities:
        company_name = e.get("company") or e.get("manufacturer") or e.get("provider")
        if company_name:
            comp_ent = entity_by_name.get(company_name.lower())
            if comp_ent and comp_ent["id"] != e["id"] and comp_ent["entity_type"] == "company":
                pred = "makes" if e["entity_type"] in {"device", "robot"} else "develops"
                rel_id = make_rel_id(comp_ent["id"], pred, e["id"])
                if rel_id not in seen_rel_ids:
                    seen_rel_ids.add(rel_id)
                    relationships.append({
                        "id": rel_id,
                        "subject_id": comp_ent["id"],
                        "subject_name": comp_ent["name"],
                        "subject_type": "company",
                        "predicate": pred,
                        "object_id": e["id"],
                        "object_name": e["name"],
                        "object_type": e["entity_type"],
                        "confidence": 0.95,
                        "source": "organization_attribution"
                    })

    # Assemble metadata
    predicates_used = sorted(list(set(r["predicate"] for r in relationships)))
    return {
        "metadata": {
            "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_relationships": len(relationships),
            "entity_count": len(all_entities),
            "predicates_used": predicates_used
        },
        "relationships": relationships
    }
