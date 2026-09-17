import pyttsx3


def text_to_speech(text, output_file):
    engine = pyttsx3.init()

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    engine.save_to_file(text, output_file)
    engine.runAndWait()


if __name__ == "__main__":
    text = "Hello, welcome to my multimodal AI project."

    output_file = "tts/output.wav"

    text_to_speech(text, output_file)

    print(f"Audio saved to: {output_file}")