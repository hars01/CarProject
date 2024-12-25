import speech_recognition as sr
import pyttsx3
import openai
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech rate
engine.setProperty('volume', 0.9)  # Volume

# OpenAI API key setup
openai.api_key = "your_openai_api_key"

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture and return user speech."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you please repeat?")
            return None
        except sr.RequestError as e:
            speak("There seems to be an issue with the service.")
            return None

def process_command(command):
    """Process and execute user command."""
    if "open notepad" in command.lower():
        speak("Opening Notepad")
        os.system("notepad")
    elif "play music" in command.lower():
        speak("Playing music")
        os.system("start wmplayer")  # Adjust this to your music player
    elif "tell me a joke" in command.lower():
        speak("Why don't scientists trust atoms? Because they make up everything!")
    elif "exit" in command.lower():
        speak("Goodbye!")
        exit()
    else:
        # Handle general queries using OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Answer this: {command}",
            max_tokens=100
        )
        speak(response.choices[0].text.strip())

def main():
    speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()