from PIL import Image
from transformers import AutoProcessor, AutoModelForImageTextToText


MODEL_NAME = "HuggingFaceTB/SmolVLM-256M-Instruct"


print("Loading vision model...")

processor = AutoProcessor.from_pretrained(MODEL_NAME)

model = AutoModelForImageTextToText.from_pretrained(
    MODEL_NAME
)

print("Vision model loaded!")


def analyze_image(image_path, question):
    image = Image.open(image_path).convert("RGB")

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image"
                },
                {
                    "type": "text",
                    "text": question
                }
            ]
        }
    ]

    prompt = processor.apply_chat_template(
        messages,
        add_generation_prompt=True
    )

    inputs = processor(
        text=prompt,
        images=[image],
        return_tensors="pt"
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    response = processor.batch_decode(
        outputs,
        skip_special_tokens=True
    )[0]

    return response


if __name__ == "__main__":
    image_path = "vision/text.jpg"

    question = "Describe what you see in this image."

    result = analyze_image(image_path, question)

    print("\n--- Vision Result ---")
    print(result)