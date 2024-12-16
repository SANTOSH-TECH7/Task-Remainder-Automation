import pyttsx3

engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}, Gender: {'Male' if 'male' in voice.name.lower() else 'Female'}")
