import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say ")
    audio = r.listen(source) 

    try:
        text = r.rec(audio,language='es-Es')
        print(text)
    except:
        print("Error") 
