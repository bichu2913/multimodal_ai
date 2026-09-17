import whisper


print("Loading Whisper model...")
model = whisper.load_model("base")


def transcribe_audio(audio_path):
    print("Transcribing audio...")

    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["text"].strip()


if __name__ == "__main__":
    audio_file = "stt/audio.mp4"

    text = transcribe_audio(audio_file)

    print("\n--- Transcription ---")
    print(text)