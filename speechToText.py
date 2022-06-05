import speech_recognition as sr


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please..")
        return "None"
    return query


if __name__ == "__main__":
    a = 1
    while a:
        takecommand()
        a = int(input("Press 0 to exit.....\n"))
