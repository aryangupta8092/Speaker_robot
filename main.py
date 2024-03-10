import pyttsx3
if __name__ == '__main__':
    print("Welcome to my robot speaker created by Aryan Gupta")
    os = pyttsx3.init()
    while True:
        x = input("Enter what do you want to speak: ")
        if x == "q":
            os.say("Goodbye")
            os.runAndWait()
            break
        os.say(x)
        os.runAndWait()
