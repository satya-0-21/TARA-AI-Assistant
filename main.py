import speech_recognition as sr
import pyttsx3
import datetime

class TARAAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170)
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        """Outputs audio response"""
        print(f"T.A.R.A: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self, language='te-IN'):
        """Listens for audio input in English or Telugu"""
        with sr.Microphone() as source:
            print("HUD: Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            # Using Google's recognizer for bilingual support (Telugu/English)
            command = self.recognizer.recognize_google(audio, language=language)
            print(f"User: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            self.speak("Network connection error.")
            return ""

    def launch_hud(self):
        """Placeholder for the Marvel-inspired visual HUD"""
        print("--- Initiating T.A.R.A Visual HUD ---")
        self.speak("Systems online. Ready for your command.")

if __name__ == "__main__":
    ai = TARAAssistant()
    ai.launch_hud()
    # Basic loop for testing English and Telugu commands
    # command = ai.listen(language='te-IN') 
  
