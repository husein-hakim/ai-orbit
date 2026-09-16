# src/extractors/personal.py
from src.normalizer import normalize

PERSONAL_ASSISTANTS = [
    {
        "name": "Pi",
        "url": "https://inflection.ai",
        "company": "Inflection AI",
        "personality_type": "Empathetic Conversational Companion",
        "pricing": "Free",
        "platforms": ["Web", "iOS", "Android", "WhatsApp"],
        "has_memory": True,
        "description": "Pi, created by Inflection AI, is a personal intelligence designed to be kind, supportive, and emotionally attuned in daily conversational interactions. Built upon the Inflection-2.5 foundation model, it acts as an empathetic sounding board, mentor, and thoughtful conversational companion for users navigating personal decisions."
    },
    {
        "name": "Replika",
        "url": "https://replika.com",
        "company": "Luka Inc",
        "personality_type": "AI Companion & Emotional Confidant",
        "pricing": "Freemium",
        "platforms": ["iOS", "Android", "Web", "Oculus VR"],
        "has_memory": True,
        "description": "Replika is a customizable AI companion application that forms unique emotional bonds through daily open-ended dialogue. It utilizes dynamic long-term memory and 3D customizable avatars to offer non-judgmental emotional support, cognitive journaling, and mood reflection exercises."
    },
    {
        "name": "Character.AI",
        "url": "https://character.ai",
        "company": "Character.AI",
        "personality_type": "Roleplay & Multi-Persona Companion",
        "pricing": "Freemium",
        "platforms": ["Web", "iOS", "Android"],
        "has_memory": True,
        "description": "Character.AI enables millions of users to converse with adaptable virtual personalities ranging from historical philosophers and fictional figures to creative writing collaborators. It features realistic vocal synthesis and dynamic episodic memory, fostering engaging interactive entertainment."
    },
    {
        "name": "Dot",
        "url": "https://new.computer",
        "company": "New Computer",
        "personality_type": "Reflective Personal Life Companion",
        "pricing": "Paid",
        "platforms": ["iOS"],
        "has_memory": True,
        "description": "Dot is an intelligent personal life companion designed by Apple and Google alumni to help users make sense of their days, goals, and thoughts. It constructs an evolving personal memory graph, proactively surfacing forgotten insights, reading recommendations, and thoughtful check-ins over time."
    },
    {
        "name": "Nomi AI",
        "url": "https://nomi.ai",
        "company": "Nomi AI",
        "personality_type": "Humanlike Companion with Spatial Context",
        "pricing": "Freemium",
        "platforms": ["Web", "iOS", "Android"],
        "has_memory": True,
        "description": "Nomi AI creates conversational artificial companions that exhibit nuanced humor, emotional authenticity, and stable long-term relationship memory. Nomis possess personal opinions and situational awareness, engaging in shared voice calls and creative roleplay sessions."
    },
    {
        "name": "Hume AI",
        "url": "https://hume.ai",
        "company": "Hume AI",
        "personality_type": "Empathic Voice Interface (EVI)",
        "pricing": "Freemium",
        "platforms": ["Web", "API"],
        "has_memory": False,
        "description": "Hume AI develops the Empathic Voice Interface (EVI), a conversational voice AI that analyzes acoustic vocal inflections, pauses, and emotional tones to respond with appropriate human empathy. Grounded in computational psychology, it aligns AI behavior to human wellbeing and authentic emotion."
    },
    {
        "name": "Woebot",
        "url": "https://woebothealth.com",
        "company": "Woebot Health",
        "personality_type": "CBT Mental Health Coach",
        "pricing": "Free / Clinical",
        "platforms": ["iOS", "Android"],
        "has_memory": True,
        "description": "Woebot is a clinically validated mental health companion that delivers Cognitive Behavioral Therapy (CBT) techniques through brief daily conversational check-ins. Designed in partnership with Stanford University clinicians, it guides users in reframing cognitive distortions and developing emotional resilience."
    },
    {
        "name": "Wysa",
        "url": "https://wysa.com",
        "company": "Wysa Inc",
        "personality_type": "Emotional Wellness & Mindfulness Guide",
        "pricing": "Freemium",
        "platforms": ["iOS", "Android"],
        "has_memory": True,
        "description": "Wysa is an AI-driven emotional support guide designed to help individuals combat anxiety, stress, and sleep deprivation through evidence-based mindfulness and CBT interventions. It ensures anonymous, privacy-protected dialogue, triaging clinical concerns with recommended breathing exercises."
    },
    {
        "name": "Youper",
        "url": "https://youper.ai",
        "company": "Youper Inc",
        "personality_type": "Interactive Mood Tracker & Therapy Companion",
        "pricing": "Freemium",
        "platforms": ["iOS", "Android", "Web"],
        "has_memory": True,
        "description": "Youper is an empathetic mental health assistant that assists users in tracking mood variations, unravelling emotional triggers, and managing daily stress through conversational psychology. It integrates real-time psychological questionnaires to deliver personalized self-care interventions."
    },
    {
        "name": "Kindroid",
        "url": "https://kindroid.ai",
        "company": "Kindroid",
        "personality_type": "Bespoke Personal Companion",
        "pricing": "Freemium",
        "platforms": ["Web", "iOS", "Android"],
        "has_memory": True,
        "description": "Kindroid offers personalized virtual companions with customizable backstories, high-fidelity neural voices, and photorealistic AI selfie generation. Its memory architecture maintains conversational continuity over months, forming deep conversational rapport with users."
    }
]

def extract() -> list[dict]:
    """Extract personal AI assistants, companions, and wellness guides."""
    entities = []
    for p in PERSONAL_ASSISTANTS:
        entity = normalize(
            raw={
                "name": p["name"],
                "description": p["description"],
                "url": p["url"],
                "categories": ["personal", "assistant", "companion", p["personality_type"].lower()],
                "personality_type": p["personality_type"],
                "pricing": p["pricing"],
                "platforms": p["platforms"],
                "has_memory": p["has_memory"],
                "company": p["company"],
            },
            entity_type="personal",
            source_name="Personal AI Registries",
            source_url=p["url"],
        )
        entities.append(entity)
    return entities
