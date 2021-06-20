from PIL import Image
from docx2pdf import convert
import os
import pydub
import re
import regex

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        Known Formats

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

IMAGE

"""


def toPNG(path, outputPath):
    image = Image.open(path)
    image.save(outputPath + getFileName(path) + ".png")

def toJPG(path, outputPath):
    image = Image.open(path)
    #Removes the transparency not supported by the JPEG format
    image = image.convert('RGB')
    print(outputPath + getFileName(path) + ".jpg")
    image.save(outputPath + getFileName(path) + ".jpg")

def toPDF(path, outputPath):
    image = Image.open(path)
    image.save(outputPath + getFileName(path) + ".pdf")


"""

TEXT

"""

#TODO : Make it windows only
def docxToPDF(path, outputPath):
    convert(path, outputPath + getFileName(path) + ".pdf")


"""

AUDIO

"""

def toAudioFormats(path, inputFormat, outputFormat, outputPath):
    audio_file = pydub.AudioSegment.from_file(path, format=inputFormat)
    audio_file.export("input.wav", format=outputFormat)


#toAudioFormats("output.mp3", "mp3", "wav")



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        Files Conversion

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
Checks if the input format corresponds to the format selected in the GUI.
If not, it returns False
It it matches, it returns True
"""
def checksInputFormat(path, conversionMode, input, output):
    print(path)

    #No conversion mode selected
    if conversionMode == -1:
        return

    #One file selected
    elif conversionMode == 1:
        path = [path[0]]    #Converts the string into an array

    #Several files selected
    elif conversionMode == 2:
        path = path[0]
    
    #Full directory selected
    else:
        #Gets all files in the specified directory
        path = os.listdir(path)

        if len(path) == 0:
            return False

    for file in path:
        print(file)
        if input == "mp3" and re.match(regex.RE_MP3, file) == None:
            return False
    
        elif input == "wav" and re.match(regex.RE_WAV, file) == None:
            return False

        elif input == "jpg" and re.match(regex.RE_JPG, file) == None:
            return False
        
        elif input == "png" and re.match(regex.RE_PNG, file) == None:
            return False
        
        elif input == "all_images" and re.match(regex.RE_ALL, file) == None:
            return False

        elif input == "doc" and re.match(regex.RE_DOC, file) == None:
            return False
    
    return True


"""
Converts the file(s) into the designated format
"""
def convertFile(path, conversionMode, input, output):
    try:
        os.mkdir("output")
    except:
        print("Le dossier existe déjà")

    outputPath = "./output/"

    #No conversion mode selected
    if conversionMode == -1:
        return

    #One file selected
    elif conversionMode == 1:
        path = [path[0]]    #Converts the string into an array

    #Several files selected
    elif conversionMode == 2:
        path = path[0]
    
    #Full directory selected
    else:
        #Gets all files in the specified directory
        path = os.listdir(path)

        if len(path) == 0:
            return False
    
    #Converts the file into the designated format
    for file in path:
        print(file)
        if input == "mp3" or input == "wav":
            toAudioFormats(file, inputFormat=input, outputFormat=output, outputPath=outputPath)
    
        elif input == "jpg" and output == "png":
            toPNG(file, outputPath)

        elif input == "png" and output == "jpg":
            toJPG(file, outputPath)
        
        elif input == "all_images":
            toPDF(file, outputPath)
        
        elif input == "doc":
            docxToPDF(file, outputPath)
    

"""
Isolates the file name inside the path
"""
def getFileName(file):
    letter = ''
    name = ""
    count = 1

    while letter != '/':
        name = letter + name
        letter = file[len(file)-count]
        print(name + "\n") 
        count += 1
    
    name = removeExtension(name)

    return name


"""
Removes the extension of the namefile
"""
def removeExtension(file):
    letter = ''
    name = ""
    count = 1

    while True:
        letter = file[len(file)-count]
        count += 1
        if letter == '.':
            break
    
    count -= 1
    for i in range (0,len(file)-count):
        name = name + file[i] 
    
    return name

