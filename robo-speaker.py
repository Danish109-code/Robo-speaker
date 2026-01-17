import pyttsx3

def robo_speaker():
    engine = pyttsx3.init()

    engine.setPriperty('rate' , 160)
    voice = engine.getProperty('voice')
    engine.setProperty('voice' , voices[0].id)

    print("Robo Speaker is Ready(type 'exit' to quit)")

    while True:
        text = input("you: ")

        if text.lower() =="exit":
            engine.say("Thank you.  Goodbye!")
            engine.runAndWait()
            break

        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    robo_speaker()
