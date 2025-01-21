from vosk import Model, KaldiRecognizer
import pyaudio
import json


def recognize_letter():
    # Load the Vosk model
    model_path = "C:\\Users\\smara\\Downloads\\vosk-model-small-en-us-0.15\\vosk-model-small-en-us-0.15"  # Replace with your model directory
    model = Model(model_path)

    # Initialize the recognizer
    recognizer = KaldiRecognizer(model, 16000)

    # Open microphone input stream
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
    stream.start_stream()

    print("Spune o literă...")

    while True:
        # Read data from the microphone
        data = stream.read(4096, exception_on_overflow=False)

        # Process the audio data
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "").strip()

            # Validate the text as a single letter
            if len(text) == 1 and text.isalpha():
                print(f"Litera recunoscută: {text}")
                break
            else:
                print("Nu am înțeles o literă validă. Încearcă din nou.")

    # Stop the audio stream
    stream.stop_stream()
    stream.close()
    mic.terminate()

    return text


# Run the function
if __name__ == "__main__":
    recognized_letter = recognize_letter()
    print(f"Litera finală: {recognized_letter}")
