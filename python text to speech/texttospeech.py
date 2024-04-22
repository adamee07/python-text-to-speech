from gtts import gTTS
import os

while True:
    answer = input("enter what you want the robot to say (or 'exit' to quit): \n")
    
    if answer.lower() == 'exit':
        break
    
    tts = gTTS(text=answer, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)
    
    os.system(f"start {audio_file}")

print("see you later!")