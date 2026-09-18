from google import genai


def main():
    print("Connecting to Gemini...")

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Explain what multimodal AI means in one sentence.",
    )

    print("\n--- Gemini Response ---")
    print(response.text)


if __name__ == "__main__":
    main()