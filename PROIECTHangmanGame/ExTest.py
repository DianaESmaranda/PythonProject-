import speech_recognition as sr

recognizer = sr.Recognizer()

# Verifică toate microfoanele disponibile
print("Microfoane disponibile:", sr.Microphone.list_microphone_names())

# Încearcă să folosești microfonul implicit
with sr.Microphone() as source:
    print("Aștept pentru semnal...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source)
    print("Înregistrat!")
    try:
        print("Recunoaștere:", recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Nu am înțeles.")
    except sr.RequestError as e:
        print(f"Eroare de rețea: {e}")
