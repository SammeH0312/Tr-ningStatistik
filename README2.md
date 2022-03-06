# Python Träningsapp
Detta programm är till för att underlätta med träning. Man ska kunna föra träningsdagbok, få tips om pass men också få tips om hela vecko upplägg. Detta för att underlätta träningen speciellt för nybörjare.

## Koden
Koden börjar med Main där alla utgår från. Beroende på vad inputen i main menyn blir så aktiveras olika funktioner som då har i syfte att göra uppgiften som blev efterfrågad i main menyn som t.e.x att få tips om träningspass. Den använder sig inte av några några biblotek eller utvändiga källor som behöver installeras.

## Uppbyggnad

Koden börjar med listorna för dagens pass och träningsdagboken. Sedan kommer alla listor för träningsupplägg men också några olika pass som man kan ha.

Efter det kommer classen som är till för träningspassen som gör så man ska kunna sortera efter olika saker som t.e.x datum.

Funktionerna efter är de olika som kallas beroende på Main funktionen.
I den första så får man en input som oavsett svar sätts till små bokstäver. EFter det printas det pass man vill ha beroende på svar och om inget svar som printar en lista kommer upp får man texten att man skrivit något fel.
```python
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
```

Nästa funktion är även väldigt lik den över men har andra alternativ

Den sista funktionen är den som lägger till pass i listorna.
Den börjar med att skapa variabel för gympass där den sätter in passet i listan men också fixar med Classen. Efter det kan man välja om man ska lägga till den i träningsdagboken vilket man svar ja eller nej på.
```python
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
```
Sedan i slutet är Main funktionen som är huvudkontrollpanelen där man väljer vad man ska göra.

## Förbättringspotenial
### Fixa så det är enklare att välja i början med menyn
Göra det enklare att välja så man t.e.x slipper skriva Registrera i din träningsdagbok.
### GÖra en grafisk del så det blir mer komplett och snyggt.

## Konsekvenser
Konskvenserna för att denna app skapas kan t.e.x vara att många som jobbar inom denna bransh skulle tappa jobb. Dessa skulle framförallt vara personliga tränare eftersom deras jobb enkelt finns i detta program. Det enda som fattas är hur man gör övningar men i och med youtube videos skulle det inte vara något problem. Däremot kan folk fortfarande välja PTs över denna app för just den hjälpen med formen alltså. De bra konsekvenser kan vara att mer folk går till gymmet för att det är enklare att att lära sig och få hjälp med träningen utan kostnad.