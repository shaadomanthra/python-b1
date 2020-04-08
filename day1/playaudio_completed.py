# # Creating an audio file and play

# import google text to speech library
from gtts import gTTS

# import os package
import os

# process text to audio
text = gTTS("welcome to PacketPrep")

# write the file 
text.save('day1/welcome_to_packetprep.mp3')

#play the file
os.system("mpg321 day1/welcome_to_packetprep.mp3")