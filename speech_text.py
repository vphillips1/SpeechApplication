import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def record_text():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening...")
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
            return MyText
        
        except sr.RequestError as e:
            print("Could not request results;{0}",format(e))

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
    return 

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return 

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

while True:
    text = record_text()
    output_text(text)
    
    print(text)