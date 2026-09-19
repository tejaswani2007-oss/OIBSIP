"""A beginner-friendly voice assistant with a text fallback."""

from datetime import datetime
import re
import threading
import webbrowser
from urllib.parse import quote_plus

import requests

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

try:
    import speech_recognition as sr
except ImportError:
    sr = None

try:
    import pywhatkit
except ImportError:
    pywhatkit = None


class VoiceAssistant:
    """Handle simple commands using speech when available or typed text."""

    def __init__(self) -> None:
        self.speaker = pyttsx3.init() if pyttsx3 else None
        self.recognizer = sr.Recognizer() if sr else None
        self.use_microphone = self.recognizer is not None

    def speak(self, message: str) -> None:
        print(f"Assistant: {message}")
        if self.speaker:
            self.speaker.say(message)
            self.speaker.runAndWait()

    def set_reminder(self, minutes: int, message: str) -> None:
        def remind() -> None:
            self.speak(f"Reminder: {message}")

        timer = threading.Timer(minutes * 60, remind)
        timer.daemon = True
        timer.start()
        self.speak(f"I will remind you in {minutes} minutes to {message}.")

    def get_weather(self, city: str) -> None:
        try:
            response = requests.get(
                f"https://wttr.in/{quote_plus(city)}?format=j1", timeout=10
            )
            response.raise_for_status()
            current = response.json()["current_condition"][0]
            temperature = current["temp_C"]
            description = current["weatherDesc"][0]["value"]
            self.speak(f"The weather in {city} is {description}, {temperature} degrees Celsius.")
        except (requests.RequestException, KeyError, IndexError, ValueError):
            self.speak("I could not retrieve the weather right now.")

    def answer_question(self, topic: str) -> None:
        try:
            response = requests.get(
                f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote_plus(topic)}",
                timeout=10,
            )
            response.raise_for_status()
            summary = response.json().get("extract")
            self.speak(summary or "I could not find an answer for that topic.")
        except (requests.RequestException, KeyError, ValueError):
            self.speak("I could not find an answer right now.")

    def listen(self) -> str:
        if not self.use_microphone:
            try:
                return input("You: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                return "exit"

        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = self.recognizer.recognize_google(audio)
            print(f"You: {command}")
            return command.lower()
        except KeyboardInterrupt:
            return "exit"
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            self.speak("I did not understand that. Please try again.")
        except sr.RequestError:
            self.speak("Speech recognition is unavailable, so please type your command.")
            self.use_microphone = False
        except OSError:
            self.speak("I cannot access a microphone, so please type your command.")
            self.use_microphone = False
        return ""

    def handle_command(self, command: str) -> bool:
        if not command:
            return True

        if re.search(r"\b(quit|exit|goodbye|stop)\b", command):
            self.speak("Goodbye!")
            return False

        if re.search(r"\b(hello|hi|hey)\b", command):
            self.speak("Hello! How can I help you?")
        elif "time" in command:
            self.speak(datetime.now().strftime("The time is %I:%M %p."))
        elif "date" in command or "day" in command:
            self.speak(datetime.now().strftime("Today is %A, %B %d, %Y."))
        elif command.startswith("remind me in "):
            match = re.match(r"remind me in (\d+) minutes? to (.+)", command)
            if match:
                self.set_reminder(int(match.group(1)), match.group(2))
            else:
                self.speak("Say: remind me in 10 minutes to take a break.")
        elif command.startswith("weather"):
            city = re.sub(r"^weather\s*(in\s*)?", "", command).strip()
            self.get_weather(city or "your location")
        elif command.startswith("who is ") or command.startswith("what is "):
            topic = re.sub(r"^(who is|what is)\s+", "", command).strip()
            self.answer_question(topic)
        elif command.startswith("search ") or command.startswith("look up "):
            query = re.sub(r"^(search|look up)\s+", "", command).strip()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={quote_plus(query)}")
                self.speak(f"Here are the search results for {query}.")
            else:
                self.speak("What would you like me to search for?")
        elif re.search(r"\bplay\b", command):
            song = re.sub(r"^.*?\bplay\s+", "", command).strip()
            if song:
                url = f"https://www.youtube.com/results?search_query={quote_plus(song)}"
                try:
                    if pywhatkit:
                        pywhatkit.playonyt(song)
                        self.speak(
                            f"Opening the first YouTube result for {song}. "
                            "Press Play if the browser blocks autoplay."
                        )
                    else:
                        raise RuntimeError("pywhatkit is not installed")
                except Exception:
                    print(f"Opening search results: {url}")
                    webbrowser.open_new_tab(url)
                    self.speak(f"I opened YouTube search results for {song}. Press Play to start.")
            else:
                self.speak("What song would you like me to play?")
        elif "help" in command:
            self.speak(
                "Try hello, time, date, weather in London, remind me in 1 minute to stretch, "
                "who is Ada Lovelace, play a song, search, or exit."
            )
        else:
            self.speak("I do not know that command yet. Say help to see what I can do.")
        return True

    def run(self) -> None:
        self.speak("Hello! I am ready. Say help for available commands.")
        while self.handle_command(self.listen()):
            pass


if __name__ == "__main__":
    VoiceAssistant().run()