# src/extractors/robots.py
from src.normalizer import normalize

ROBOTS = [
    {
        "name": "Figure 02",
        "url": "https://figure.ai",
        "manufacturer": "Figure AI",
        "form_factor": "Humanoid",
        "ai_system": "OpenAI Vision-Language Models & On-Board Neural Networks",
        "release_status": "Commercial Pilot",
        "primary_use": "Automotive Manufacturing & Logistics",
        "description": "Figure 02 is a commercially deployable autonomous humanoid robot designed for dexterous industrial manipulation in hazardous and repetitive warehouse environments. Equipped with 16 degrees of freedom hands, on-board vision-language neural networks, and speech reasoning, it executes sub-millimeter precision assembly tasks alongside human workers."
    },
    {
        "name": "Optimus Gen 2",
        "url": "https://tesla.com/optimus",
        "manufacturer": "Tesla",
        "form_factor": "Humanoid",
        "ai_system": "Tesla Full Self-Driving (FSD) Neural Network & Occupancy Network",
        "release_status": "Internal Deployment & Testing",
        "primary_use": "Factory Assembly & General Automation",
        "description": "Tesla Optimus Gen 2 is a general-purpose bipedal robot designed to take over dangerous, repetitive, or boring physical manufacturing tasks. Leveraging Tesla's end-to-end trained vision neural networks and custom-actuated sensory fingers, it demonstrates delicate egg manipulation, autonomous walking balance, and factory battery sorting."
    },
    {
        "name": "Spot",
        "url": "https://bostondynamics.com/products/spot/",
        "manufacturer": "Boston Dynamics",
        "form_factor": "Quadruped",
        "ai_system": "Autowalk Navigation & Vision Inspection AI",
        "release_status": "Commercial",
        "primary_use": "Industrial Inspection & Remote Sensing",
        "description": "Spot is an agile quadruped mobile robot engineered to traverse unstructured industrial terrains, climb stairs, and navigate hazardous environments with dynamic balance. Outfitted with thermal imaging, acoustic leak detectors, and autonomous inspection software, it automates routine data capture across power plants and construction sites."
    },
    {
        "name": "Atlas (Electric)",
        "url": "https://bostondynamics.com/atlas/",
        "manufacturer": "Boston Dynamics",
        "form_factor": "Humanoid",
        "ai_system": "Reinforcement Learning & Whole-Body Trajectory Optimization",
        "release_status": "Commercial Development",
        "primary_use": "Automotive Logistics & Heavy Industrial Assembly",
        "description": "The fully electric Atlas robot is Boston Dynamics' next-generation humanoid designed for real-world commercial automation without hydraulic limitations. Featuring 360-degree rotational joint actuators and AI-driven spatial planning, it executes dynamic object sorting and heavy payload lifting with fluid acrobatic motion."
    },
    {
        "name": "Digit",
        "url": "https://agilityrobotics.com",
        "manufacturer": "Agility Robotics",
        "form_factor": "Humanoid Biped",
        "ai_system": "Agility Arc Cloud Fleet Manager & Spatial AI",
        "release_status": "Commercial",
        "primary_use": "Logistics & Tote Handling",
        "description": "Digit is a bipedal mobile robot developed by Agility Robotics engineered specifically for bulk material handling and tote moving within warehouse distribution hubs. Deployed in live fulfillment centers by Amazon and GXO Logistics, it seamlessly navigates human-centric aisles, loading docks, and conveyor stations."
    },
    {
        "name": "Unitree H1",
        "url": "https://unitree.com/h1",
        "manufacturer": "Unitree Robotics",
        "form_factor": "Humanoid",
        "ai_system": "End-to-End Reinforcement Learning Locomotion",
        "release_status": "Commercial",
        "primary_use": "Research & Dynamic Industrial Operations",
        "description": "Unitree H1 is a high-speed universal humanoid robot capable of running at over 3.3 meters per second using advanced high-torque joint motors and 3D LiDAR vision. Built as an open platform for academic and industrial laboratories, it accelerates research in dynamic locomotion, obstacle recovery, and athletic physical intelligence."
    },
    {
        "name": "1X Neo",
        "url": "https://1x.tech",
        "manufacturer": "1X Technologies",
        "form_factor": "Humanoid",
        "ai_system": "Embodied Foundation Models & Shadow Teleoperation",
        "release_status": "Announced Consumer Beta",
        "primary_use": "Domestic Assistance & Light Industrial",
        "description": "1X Neo is an intelligent bipedal humanoid robot engineered explicitly for safe domestic and personal home assistance. Backed by OpenAI, its biomimetic muscle-tendon architecture and soft-touch exterior allow it to safely clean, organize domestic goods, and perform delicate home chores alongside family members."
    },
    {
        "name": "Stretch",
        "url": "https://bostondynamics.com/products/stretch/",
        "manufacturer": "Boston Dynamics",
        "form_factor": "Mobile Arm on Omnidirectional Base",
        "ai_system": "High-Throughput Vision Box Detection & Machine Learning",
        "release_status": "Commercial",
        "primary_use": "Shipping Container Unloading & Logistics",
        "description": "Stretch is a specialized mobile logistics robot designed by Boston Dynamics to automate the grueling task of unloading shipping containers and truck trailers. Utilizing a heavy-duty vacuum gripper arm and computer vision box detection, it moves up to 800 packages per hour continuously without fatigue."
    },
    {
        "name": "Apptronik Apollo",
        "url": "https://apptronik.com",
        "manufacturer": "Apptronik",
        "form_factor": "Humanoid",
        "ai_system": "Modular Cognitive Stack & Force-Control Actuation",
        "release_status": "Commercial Pilot",
        "primary_use": "Manufacturing & Supply Chain Warehousing",
        "description": "Apptronik Apollo is a modular humanoid robot built for factory and supply chain integration, developed in collaboration with NASA and Mercedes-Benz. It features swappable battery packs for continuous 22-hour shifts, an intuitive digital face display for human interaction, and compliant force-sensing actuators."
    },
    {
        "name": "Sanctuary Phoenix",
        "url": "https://sanctuary.ai",
        "manufacturer": "Sanctuary AI",
        "form_factor": "Humanoid (Upper Torso & Wheeled/Biped)",
        "ai_system": "Carbon Cognitive Architecture & Haptic Teleoperation",
        "release_status": "Commercial Pilot",
        "primary_use": "Retail, Hospitality, & Industrial Sorting",
        "description": "Phoenix is a general-purpose humanoid robot powered by Sanctuary AI's proprietary Carbon cognitive architecture. Designed to mirror human sensory-motor intelligence, it boasts industry-leading 20 degrees of freedom robotic hands with micro-haptic feedback, enabling high dexterity tasks from stocking supermarket shelves to assembling electrical parts."
    }
]

def extract() -> list[dict]:
    """Extract prominent autonomous AI robotics systems and humanoid platforms."""
    entities = []
    for r in ROBOTS:
        entity = normalize(
            raw={
                "name": r["name"],
                "description": r["description"],
                "url": r["url"],
                "categories": ["robot", "robotics", "embodied-ai", r["form_factor"].lower()],
                "manufacturer": r["manufacturer"],
                "form_factor": r["form_factor"],
                "ai_system": r["ai_system"],
                "release_status": r["release_status"],
                "primary_use": r["primary_use"],
            },
            entity_type="robot",
            source_name="Official Robotics Manufacturer Documentation",
            source_url=r["url"],
        )
        entities.append(entity)
    return entities
