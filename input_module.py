import speech_recognition
import pyttsx3 as tts

 




def put_output(text):
        speaker = tts.init()
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[1].id)
        speaker.setProperty('rate', 270)
        speaker.say(text)
        speaker.runAndWait()



def get_input():
        recognizer = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone(device_index=1   ) as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio).lower()
                return note

        except speech_recognition.UnknownValueError as e:
            recognizer = speech_recognition.Recognizer()
            put_output("Could not Understand. Try Again")
            return None


if __name__ == "__main__":
    pass