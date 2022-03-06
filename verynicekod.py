dagens_pass = []    #Listor för att regga dagens pass och andra listan för att ha alla pass som man reggar
Traningsdagbok = []
x = ""
y = ""
z = ""
# Olika pass som rekommenderas
benpass = ["squats 3x10", "ben press 3x10", "Utfallssteg 3x10", "tå hävningar"]
pushpass = ["bänkpress 3x10", "Sne Bänkpress 3x10", "Dips 3x10", "Cable Flies 3x10"]
pullpass = ["Marklyft 3x10", "Pull ups 3x10", "Stående Rodd 3x10", "Bicep Curls 3x10", "Preacher Curls 3x10"]
#Olika träningsupplägg
#7 gånger i veckan
all_week = ["Måndag = Bröst och Axlar", "Tisdag = Rygg och Traps", "Onsdag = Armar", "Torsdag = Ben", "Fredag = Bröst och Axlar", "Lördag = Rygg och traps", "Söndag = Ben"]
#6 gånger i veckan
push_pull_ben = ["Måndag = Pushpass", "Tisdag = Pullpass", "Onsdag = Benpass", "Torsdag = Pushpass", "Fredag = Pullpass", "Lördag = Benpass", "Söndag = Vilodag"]
arnolds_pass = ["Måndag = Bröst och Rygg", "Tisdag = Axlar och Armar", "Onsdag = Ben och Ländrygg", "Torsdag = Bröst och Rygg", "Fredag = Axlar och Armar", "Lördag = Ben och Ländrygg", "Söndag ?"]
#5 gånger i veckan
fem_gang = ["Måndag = Bröst och Rygg", "Tisdag = Armar", "Onsdag = Benpass", "Torsdag = Bröst och Rygg", "Fredag = Vilodag", "Lördag = Benpass", "Söndag = Vilodag"]
#4 gånger i veckan
överkropp_underkropp = ["Måndag = Överkropp","Tisdag = Vilodag" ,"Onsdag = Underkopp","Torsdag = Vilodag","Fredag = Överkropp", "Lördag = Vilodag" "Söndag = Underkropp"]
hel_kropp = ["Måndag = Överkropp", "Tisdag = Ben", "Onsdag = Vilodag", "Torsdag = Hela kroppen", "Fredag = Vilodag", "Lördag = Hela Kroppen", "Söndag = Vilodag"]
#3 gånger i veckan 
överkropp_underkropp2 = ["Måndag = Överkropp", "Tisdag = Vilodag", "Onsdag = Ben", "Torsdag = Vilodag", "Fredag = Hela kroppen", "Lördag = Vilodag", "Söndag = Vilodag"]
hel_kropp2 = ["Måndag = Hela Kroppen", "Tisdag = Vilodag", "Onsdag = Hela Kroppen", "Torsdag = Vilodag", "Fredag = Hela Kroppen", "Lördag = Vilodag", "Söndag = Vilodag"]
#2 gånger i veckan
överkropp_underkropp3 = ["Måndag = Överkropp", "Tisdag = Vilodag", "Onsdag = Vilodag", "Torsdag = Underkropp", "Fredag = Vilodag", "Lördag = Vilodag", "Söndag = Vilodag"]
hel_kropp3 = ["Måndag = Hela Kroppen", "Tisdag = Vilodag", "Onsdag = Vilodag", "Torsdag = Hela Kroppen", "Fredag = Vilodag", "Lördag = Vilodag", "Söndag = Vilodag"]

class Traningspass: #Klass för när man väljer så man ska kunna sortera och bilda ett pass
    def __init__(self, datum, muskel, tyngd):
        self.datum = datum
        self.muskel = muskel
        self.tyngd = tyngd

    def __str__(self) -> str:
        return f""


def traningspassfunc(): #func att lägga till tips om pass
    a = input("Vill du göra ett pushpass, pullpass eller benpass?")
    a_lower = a.lower()
    if a_lower == "pushpass":
        print(*pushpass)
    elif a_lower == "pullpass":
        print(*pullpass)
    elif a_lower == "benpass":
        print(*benpass)
    else:
        print("Något blev fel som t.e.x stav fel prova igen")


def traningsupplaggfunc():
    a = input("Hur ofta vill du träna? du kan välja från två gånger i veckan till sju gångar i veckan! svara med siffror")
    if a == "2":
        c = input("Det finns två alternativ vilka vill du se? Helkropps varianten där du tränar hela kroppen under ett pass eller upplägget där du tränar över och under kropp separat?")
        c_lower = c.lower()
        if c_lower == "helkropp":
            print(*hel_kropp3)
        elif c_lower == "överkropp och underkropp":
            print(*överkropp_underkropp3)
        else:
            print("SVARA RÄTT!")
    elif a == "3":
        c = input("Det finns två alternativ vilka vill du se? Helkropps varianten där du tränar hela kroppen under ett pass eller upplägget där du tränar över och under kropp separat?")
        c_lower = c.lower()
        if c_lower == "helkropp":
            print(*hel_kropp2)
        elif c_lower == "överkropp och underkropp":
            print(*överkropp_underkropp2)
        else:
            print("SVARA RÄTT!")
    elif a == "4":
        c = input("Det finns två alternativ vilka vill du se? Helkropps varianten där du tränar hela kroppen under ett pass eller upplägget där du tränar över och under kropp separat?")
        c_lower = c.lower()
        if c_lower == "helkropp":
            print(*hel_kropp)
        elif c_lower == "överkropp och underkropp":
            print(*överkropp_underkropp)
        else:
            print("SVARA RÄTT!")
    elif a == "5":
        print(fem_gang)
    elif a == "6":
        c = input("Det finns två alternativ. Antingen väljer du push,pull,ben upplägget eller arnold upplägget")
        c_lower = c.lower()
        if c_lower == "push,pull,ben":
            print(*push_pull_ben)
        elif c_lower == "arnold":
            print(*arnolds_pass)
        else:
            print("SVARA RÄTT")
    else:
        print("Något blev fel som t.e.x stav fel prova igen")


def laggatillipasslista(): #Function att lägga till i dagens pass i träningsdagboken
    
    gympass = Traningspass( x, y, z) #Passet som läggs till i dagenspass
    dagens_pass.append(gympass)
    
    a = input("Vill du lägga till detta pass i en lista? Ja eller nej? ")
    a_lower = a.lower()
    if a_lower == "ja":
        Traningsdagbok.append(dagens_pass)
        print("Ok! Passet är Inlagt på din träningsdagbok")
        print(Traningsdagbok)
    elif a_lower == "nej":
        print("Ok! Passet är borttaget")
    else:
        print("Något blev fel som t.e.x stav fel prova igen")

def main(): #Alternativen där saker ska hända när man väljer
    v = input("Välkommen! Vill du se träningspass, träningsdagbok, träningsupplägg eller registrera i din träningsdagbok? ")
    v_lower = v.lower()
    if v_lower == "träningspass":
        traningspassfunc()
    elif v_lower == "träningsdagbok":
        print(Traningsdagbok)
    elif v_lower == "träningsupplägg":
        traningsupplaggfunc()
    elif v_lower == "registrera i din träningsdagbok":
        x , y, z = input("Vilken datum är det idag? ex 22-02-2022"), input("Vad har du tränat? bröst"), input("Hur tungt tränade du?")
        laggatillipasslista()
    else:
        print("Något blev fel som t.e.x stav fel prova igen")
main()
