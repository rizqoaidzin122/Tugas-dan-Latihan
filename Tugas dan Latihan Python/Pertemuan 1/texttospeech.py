from gtts import gTTS
import os
text = "halo"
bahasa = "id"
file = gTTS(text=text,lang=bahasa)
file.save("halo.mp3")
os.system("start halo.mp3")
