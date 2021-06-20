import re

#Audio
RE_MP3 = re.compile('^.*(.mp3)$', re.IGNORECASE)
RE_WAV = re.compile('^.*(.wav)$', re.IGNORECASE)

#Image
RE_JPG = re.compile('^.*(.jpg|.jpeg)$', re.IGNORECASE)
RE_PNG = re.compile('^.*(.png)$', re.IGNORECASE)
RE_ALL = re.compile('^.*(.jpg|.jpeg|.png)$', re.IGNORECASE)

#Doc
RE_DOC = re.compile('^.*(.doc|.docx)$', re.IGNORECASE)

