import calendar
from pyexpat import native_encoding  

dagens_pass = []
exakt_pass = []

x = input("Vilken datum är det idag?")
y = input("Vad har du tränat?")
z = input("Hur tungt tränade du?")


def traningspassfunc():
    traningspass = []
    muskelgrupper = open("Tillämpad Programmering/träningspass.txt", "r", encoding="utf8")
    traningspass.append(muskelgrupper)
    return traningspass

def tyngdfunc():
    tyngd = []
    tyngdlista = open("Tillämpad Programmering/tyngd.txt", "r", encoding="utf8")
    tyngd.append(tyngdlista)
    return tyngd

