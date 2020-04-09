# # Creating an audio file and play

# import google text to speech library
from gtts import gTTS
# import os package
import os
# process text to audio
text = gTTS("Welcome to PacketPrep")

# write the file 
text.save("message.mp3")

#play the file
os.system("mpg321 message.mp3")
# os.system("start message.mp3")