import os

from magic_hour import Client


API_KEY = os.getenv("MAGIC_HOUR_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "MAGIC_HOUR_API_KEY is not set."
    )


client = Client(token=API_KEY)


def generate_video():
    print("Connecting to Magic Hour...")
    print("Starting free LTX 2.3 video generation...")

    result = client.v1.text_to_video.generate(
        name="Multimodal AI Test Video",
        end_seconds=5.0,
        model="ltx-2.3",
        orientation="landscape",
        resolution="480p",
        style={
            "prompt": (
                "A cinematic futuristic city at night, "
                "neon lights reflecting on wet streets, "
                "cars moving through the city, "
                "smooth camera movement, realistic lighting, "
                "high detail, cinematic atmosphere."
            )
        },
        wait_for_completion=True,
        download_outputs=True,
        download_directory="video_generation",
    )

    print("\n--- Video Result ---")
    print(result)
    print("\nVideo generation completed!")


if __name__ == "__main__":
    generate_video()