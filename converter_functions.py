from PIL import Image
from docx2pdf import convert
import os
import pydub

#path = "test.jpg"
path = "output.png"

"""

IMAGE

"""
#TODO : séparer mode fichier seulement ET mode dossier entier

def toPNG(path):
    image = Image.open(path)
    image.save("output.png")

def toJPG(path):
    image = Image.open(path)
    image.save("output.jpg")

def toPDF(path):
    image = Image.open(path)
    image.save("output.pdf")


"""

TEXTE

"""

#TODO : Make it windows only
def docxToPDF(path):
    convert(path, "./output.pdf")


"""

AUDIO

"""

def toAudioFormats(path, inputFormat, outputFormat):
    audio_file = pydub.AudioSegment.from_file(path, format=inputFormat)
    audio_file.export("input.wav", format=outputFormat)


#toAudioFormats("output.mp3", "mp3", "wav")

toJPG("test.png")