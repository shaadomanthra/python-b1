# # Creating an audio file

# import google text to speech library
from gtts import gTTS

# process text to audio
text = gTTS("sample audio")

# write the file 
text.save('day1/sample_audio.mp3')