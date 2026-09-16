# src/extractors/creative.py
from src.normalizer import normalize

CREATIVE_TOOLS = [
    {
        "name": "DALL-E 3",
        "url": "https://openai.com/dall-e-3",
        "company": "OpenAI",
        "output_type": "Image",
        "pricing": "Paid / Integrated in ChatGPT",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "DALL-E 3 is OpenAI's advanced image generation system that translates complex, nuanced natural language descriptions into highly detailed images. Built natively into ChatGPT, it excels at following verbose prompt constraints, rendering legible typography, and rendering intricate spatial scenes."
    },
    {
        "name": "Stable Diffusion",
        "url": "https://stability.ai",
        "company": "Stability AI",
        "output_type": "Image",
        "pricing": "Open Source / Freemium",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "Stable Diffusion is a pioneering open-source latent diffusion model family developed by Stability AI, CompVis, and Runway. By running efficiently on consumer GPUs, it enables artists, researchers, and developers worldwide to train custom LoRA adapters and automate image generation pipelines."
    },
    {
        "name": "Midjourney",
        "url": "https://midjourney.com",
        "company": "Midjourney",
        "output_type": "Image",
        "pricing": "Paid",
        "api_available": False,
        "quality_tier": "Professional",
        "description": "Midjourney is an independent generative image engine recognized for its signature cinematic aesthetics, intricate photorealism, and nuanced artistic textures. Accessible through dedicated web and Discord interfaces, it offers professional creators inpainting, image variation, and style tuning."
    },
    {
        "name": "Suno",
        "url": "https://suno.com",
        "company": "Suno AI",
        "output_type": "Music & Vocals",
        "pricing": "Freemium",
        "api_available": False,
        "quality_tier": "Consumer",
        "description": "Suno is a generative music platform that composes radio-ready songs complete with expressive vocals, harmonies, and rich instrumentation from simple text prompts. It democratizes musical composition for casual creators, content producers, and independent songwriters across diverse musical genres."
    },
    {
        "name": "Udio",
        "url": "https://udio.com",
        "company": "Udio",
        "output_type": "Music & Vocals",
        "pricing": "Freemium",
        "api_available": False,
        "quality_tier": "Professional",
        "description": "Udio is an AI music creation suite built by former Google DeepMind researchers that synthesizes full fidelity songs with nuanced acoustic arrangements. It provides granular compositional controls including intro/outro editing, sectional track extension, and custom stem separation."
    },
    {
        "name": "Runway Gen-3",
        "url": "https://runwayml.com",
        "company": "Runway",
        "output_type": "Video",
        "pricing": "Freemium",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "Runway Gen-3 Alpha is a multimodal generative video platform that creates photorealistic cinematic clips with coherent physical motion and camera movements. It offers filmmakers granular control using Motion Brush brushes, customized camera pans, and consistent character physics across shots."
    },
    {
        "name": "Kling AI",
        "url": "https://klingai.com",
        "company": "Kuaishou",
        "output_type": "Video",
        "pricing": "Freemium",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "Kling AI is a generative video model developed by Kuaishou that produces high-definition video sequences up to two minutes long at 30 frames per second. It simulates real-world physical dynamics accurately, allowing creators to generate complex character motion and fluid interactions."
    },
    {
        "name": "Pika",
        "url": "https://pika.art",
        "company": "Pika Labs",
        "output_type": "Video",
        "pricing": "Freemium",
        "api_available": True,
        "quality_tier": "Consumer",
        "description": "Pika is an intuitive video generation platform that enables users to bring ideas, static illustrations, and photos to life as dynamic video animations. It includes creative physics modifiers like melting, inflating, and exploding objects, paired with automated sound effects generation."
    },
    {
        "name": "ElevenLabs",
        "url": "https://elevenlabs.io",
        "company": "ElevenLabs",
        "output_type": "Voice & Audio",
        "pricing": "Freemium",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "ElevenLabs is a voice AI research platform that delivers emotionally resonant speech synthesis, voice cloning, and multilingual video dubbing across 29 languages. Its low-latency audio APIs power dynamic digital narration, interactive game dialogues, and automated video localization."
    },
    {
        "name": "Adobe Firefly",
        "url": "https://www.adobe.com/products/firefly.html",
        "company": "Adobe",
        "output_type": "Image & Vector Graphics",
        "pricing": "Freemium / Creative Cloud",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "Adobe Firefly is a family of creative generative AI models trained exclusively on licensed Adobe Stock images and public domain content to guarantee commercial safety. Integrated natively into Photoshop and Illustrator, it powers Generative Fill, Generative Expand, and text-to-vector artwork."
    },
    {
        "name": "Luma Dream Machine",
        "url": "https://lumalabs.ai/dream-machine",
        "company": "Luma AI",
        "output_type": "Video",
        "pricing": "Freemium",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "Luma Dream Machine is a high-speed video generation model that converts text prompts and reference photos into physically consistent, realistic 5-second video shots. It maintains continuous motion flow and photorealistic lighting, enabling directors to rapidly storyboard and visualize movie scenes."
    },
    {
        "name": "HeyGen",
        "url": "https://heygen.com",
        "company": "HeyGen",
        "output_type": "Avatar Video",
        "pricing": "Freemium",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "HeyGen is an AI video generation platform that creates studio-quality spokesperson and avatar videos from simple text scripts. It features photo-to-avatar generation, flawless lip-syncing across 175 languages, and automated voice cloning for enterprise marketing and training."
    },
    {
        "name": "Ideogram",
        "url": "https://ideogram.ai",
        "company": "Ideogram",
        "output_type": "Typography & Image",
        "pricing": "Freemium",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "Ideogram is an image generation model renowned for its ability to render legible, stylized, and complex typography seamlessly inside digital artwork. Graphic designers, merchandise creators, and branding agencies rely on it for posters, logos, and marketing banners."
    },
    {
        "name": "Flux",
        "url": "https://blackforestlabs.ai",
        "company": "Black Forest Labs",
        "output_type": "Image",
        "pricing": "Open Source / API",
        "api_available": True,
        "quality_tier": "Professional",
        "description": "Flux is a 12-billion parameter text-to-image model family developed by Black Forest Labs, founded by the original creators of Stable Diffusion. Utilizing a hybrid multimodal transformer architecture, it achieves exceptional visual fidelity, precise anatomy, and prompt adherence."
    }
]

def extract() -> list[dict]:
    """Extract generative creative tools across image, video, music, and voice."""
    entities = []
    for c in CREATIVE_TOOLS:
        entity = normalize(
            raw={
                "name": c["name"],
                "description": c["description"],
                "url": c["url"],
                "categories": ["creative", "generative-ai", c["output_type"].lower()],
                "output_type": c["output_type"],
                "pricing": c["pricing"],
                "api_available": c["api_available"],
                "quality_tier": c["quality_tier"],
                "company": c["company"],
            },
            entity_type="creative",
            source_name="Creative AI Directory",
            source_url=c["url"],
        )
        entities.append(entity)
    return entities
