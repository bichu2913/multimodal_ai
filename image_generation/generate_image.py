import torch
from diffusers import StableDiffusionPipeline

MODEL_NAME = "runwayml/stable-diffusion-v1-5"

print("Loading image generation model...")

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

print("Image generation model loaded!")


def generate_image(prompt, output_file):
    print("Generating image...")

    image = pipe(
        prompt,
        num_inference_steps=20
    ).images[0]

    image.save(output_file)

    print(f"Image saved to: {output_file}")


if __name__ == "__main__":
    prompt = "A futuristic city at night, neon lights, cinematic, highly detailed"

    output_file = "image_generation/generated_image.png"

    generate_image(prompt, output_file)