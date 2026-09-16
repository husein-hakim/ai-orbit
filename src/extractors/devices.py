# src/extractors/devices.py
from src.normalizer import normalize

DEVICES = [
    {
        "name": "NVIDIA H100 Tensor Core GPU",
        "url": "https://www.nvidia.com/en-us/data-center/h100/",
        "manufacturer": "NVIDIA",
        "device_type": "Data Center GPU",
        "ai_accelerator": True,
        "specs": {
            "memory": "80GB HBM3",
            "memory_bandwidth": "3.35 TB/s",
            "tflops_fp8": 1979,
            "power_watts": 700
        },
        "target_market": "Enterprise Cloud & AI Pre-training",
        "description": "The NVIDIA H100 Tensor Core GPU is the industry-standard accelerator for training and serving massive frontier language models. Built on the Hopper architecture with dedicated Transformer Engine FP8 arithmetic and NVLink 4 interconnects, it delivers up to 9x faster AI training throughput over previous-generation A100 systems."
    },
    {
        "name": "NVIDIA Blackwell B200 GPU",
        "url": "https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/",
        "manufacturer": "NVIDIA",
        "device_type": "Data Center GPU",
        "ai_accelerator": True,
        "specs": {
            "memory": "192GB HBM3e",
            "memory_bandwidth": "8.0 TB/s",
            "tflops_fp4": 4500,
            "power_watts": 1000
        },
        "target_market": "Hyperscale AI Supercomputing",
        "description": "The NVIDIA Blackwell B200 is a dual-die superchip packing 208 billion transistors connected by an ultra-fast 10 TB/s chip-to-chip interface. Engineered for multi-trillion parameter generative AI models, it introduces microscopic FP4 quantization, cutting frontier inference operating costs and energy footprint by up to 25x."
    },
    {
        "name": "Apple M4 Pro",
        "url": "https://www.apple.com/macbook-pro/",
        "manufacturer": "Apple",
        "device_type": "System on Chip (SoC)",
        "ai_accelerator": True,
        "specs": {
            "memory": "Up to 64GB Unified Memory",
            "memory_bandwidth": "273 GB/s",
            "neural_engine_tops": 38,
            "power_watts": 45
        },
        "target_market": "Professional Consumer & Edge AI",
        "description": "Apple M4 Pro is a high-performance system-on-chip manufactured on an advanced 3-nanometer process, engineered for Mac workstations and laptops. It integrates an upgraded 16-core Neural Engine and high-bandwidth unified memory architecture that allows developers to run 70B parameter LLMs locally at interactive speeds without cloud connectivity."
    },
    {
        "name": "AMD Instinct MI300X",
        "url": "https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html",
        "manufacturer": "AMD",
        "device_type": "Data Center GPU",
        "ai_accelerator": True,
        "specs": {
            "memory": "192GB HBM3",
            "memory_bandwidth": "5.3 TB/s",
            "tflops_fp8": 1300,
            "power_watts": 750
        },
        "target_market": "Enterprise Cloud & AI Inference",
        "description": "The AMD Instinct MI300X accelerator is an enterprise compute engine featuring CDNA 3 architecture and an industry-leading 192GB of high-bandwidth memory. It allows complete multi-billion parameter models like Falcon-40B and Llama-70B to fit inside a single accelerator, removing inter-GPU tensor parallel overhead during serving."
    },
    {
        "name": "Google TPU v5e",
        "url": "https://cloud.google.com/tpu/docs/v5e-intro",
        "manufacturer": "Google",
        "device_type": "Tensor Processing Unit (ASIC)",
        "ai_accelerator": True,
        "specs": {
            "memory": "16GB HBM2",
            "memory_bandwidth": "819 GB/s",
            "tflops_int8": 393,
            "power_watts": 250
        },
        "target_market": "Cloud Inference & Mid-Scale Training",
        "description": "Google TPU v5e is a custom-designed application-specific integrated circuit (ASIC) built by Google for cost-effective large-scale AI inference and training workloads. Deployed within Google Cloud pods, it delivers up to 2.5x higher inference performance per dollar compared to earlier generation TPU v4 systems."
    },
    {
        "name": "Intel Gaudi 3",
        "url": "https://www.intel.com/content/www/us/en/products/details/processors/ai-accelerators/gaudi3.html",
        "manufacturer": "Intel",
        "device_type": "AI Accelerator (ASIC)",
        "ai_accelerator": True,
        "specs": {
            "memory": "128GB HBM2e",
            "memory_bandwidth": "3.7 TB/s",
            "tflops_fp8": 1835,
            "power_watts": 600
        },
        "target_market": "Enterprise Cloud & Tier-2 Datacenters",
        "description": "Intel Gaudi 3 is an enterprise AI accelerator manufactured on a 5nm process, engineered to deliver open, standards-based competition in generative AI computing. It features 24 integrated 200GbE Ethernet ports directly on-chip, enabling seamless scale-out clustering across thousands of nodes without proprietary proprietary networking switches."
    },
    {
        "name": "Apple Vision Pro",
        "url": "https://www.apple.com/apple-vision-pro/",
        "manufacturer": "Apple",
        "device_type": "Spatial Computing Headset",
        "ai_accelerator": True,
        "specs": {
            "chips": "Apple M2 + Custom R1 Sensor Processor",
            "sensor_latency": "12 milliseconds",
            "display": "23M pixels Micro-OLED",
            "power_watts": 30
        },
        "target_market": "Consumer & Enterprise Spatial Computing",
        "description": "Apple Vision Pro is an advanced spatial computing device featuring real-time eye tracking, hand gestures, and 3D spatial mapping powered by computer vision neural networks. Its custom dual-chip architecture processes 12 cameras, 5 sensors, and 6 microphones with virtually lag-free 12-millisecond sensor latency."
    },
    {
        "name": "Rabbit r1",
        "url": "https://www.rabbit.tech",
        "manufacturer": "Rabbit Inc",
        "device_type": "AI Handheld Companion",
        "ai_accelerator": False,
        "specs": {
            "processor": "MediaTek Helio P35",
            "camera": "360-degree rotational eye",
            "connectivity": "4G LTE & Wi-Fi",
            "os": "rabbit OS with Large Action Model (LAM)"
        },
        "target_market": "Consumer AI Gadgets",
        "description": "Rabbit r1 is a pocket-sized standalone AI consumer hardware device designed in collaboration with Teenage Engineering. Driven by rabbit OS and the Large Action Model (LAM), it triggers actions across digital services such as hailing rides, ordering food, and playing music without navigating smartphone app menus."
    },
    {
        "name": "Frame AI Glasses",
        "url": "https://brilliant.xyz",
        "manufacturer": "Brilliant Labs",
        "device_type": "Multimodal Smart Eyewear",
        "ai_accelerator": False,
        "specs": {
            "weight": "Under 40 grams",
            "display": "Micro-OLED prism",
            "connectivity": "Bluetooth 5.0",
            "open_source": "Full open-source hardware & firmware"
        },
        "target_market": "Developers & Everyday Consumers",
        "description": "Frame AI Glasses are lightweight, open-source smart glasses equipped with an integrated camera, microphone, and geometric micro-OLED prism display. Powered by an integrated multimodal AI assistant named Noa, they provide real-time visual translations, web lookup overlays, and calorie estimations directly in the user's field of vision."
    },
    {
        "name": "NVIDIA Jetson AGX Orin",
        "url": "https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/",
        "manufacturer": "NVIDIA",
        "device_type": "Embedded Edge AI Module",
        "ai_accelerator": True,
        "specs": {
            "memory": "64GB 256-bit LPDDR5",
            "memory_bandwidth": "204.8 GB/s",
            "ai_performance_tops": 275,
            "power_watts": "15W to 60W configurable"
        },
        "target_market": "Autonomous Robotics, Drones & Smart Healthcare",
        "description": "NVIDIA Jetson AGX Orin is the world's most capable edge AI platform, delivering 275 TOPS of neural compute within a compact energy-efficient module. It runs advanced vision transformers, SLAM spatial localization, and multimodal sensor fusion locally on autonomous delivery drones, surgical robots, and agricultural equipment."
    }
]

def extract() -> list[dict]:
    """Extract premier AI hardware, server accelerators, and edge computing devices."""
    entities = []
    for d in DEVICES:
        entity = normalize(
            raw={
                "name": d["name"],
                "description": d["description"],
                "url": d["url"],
                "categories": ["device", "hardware", d["device_type"].lower()],
                "manufacturer": d["manufacturer"],
                "device_type": d["device_type"],
                "ai_accelerator": d["ai_accelerator"],
                "specs": d["specs"],
                "target_market": d["target_market"],
            },
            entity_type="device",
            source_name="Official Hardware Specifications",
            source_url=d["url"],
        )
        entities.append(entity)
    return entities
