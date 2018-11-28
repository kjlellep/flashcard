import random
import codecs

class Window:



def mainloop():
    while True:
        sisend = input("Failist küsimuste sisse lugemiseks kirjuta 1.\n"
                       "Uue küsimuse lisamiseks kirjuta 2.\n"
                       "Küsimustiku välja printimiseks kirjuta 3.\n"
                       "Harjutamise alustamiseks kirjuta 4 (enne peab andmed sisse lugema).\n"
                       "Lõpetamiseks kirjuta exit.\n")
        if sisend == "1":
            sisselugemine()
        elif sisend == "2":
            lisamine()
        elif sisend == "3":
            printimine()
        elif sisend == "4":
            questionloop(kysimustik)
        elif sisend == "exit":
            print("Shutting down.")
            break
        else:
            print("Vale sisend.")

def sisselugemine():
    failinimi = input("Sisesta failinimi: ")
    global kysimustik
    kysimustik = {}
    try:
        with codecs.open(failinimi, encoding='utf-8') as f:
            for line in f:
                rida = line.split("\\")
                kysimustik[rida[0]] = rida[1].strip()
    except FileNotFoundError:
        print("Antud nimega faili ei leitud!")
        sisselugemine()
    toprint = input("Kui tahad küsimused ja vastused välja printida, kirjuta 1.\n"
                    "Kui ei taha, vajuta lihtsalt Enter.")
    if toprint == "1":
        printimine()
    return kysimustik

def printimine():
    for keys in kysimustik:
        print(keys)
        print(kysimustik[keys])

def questionloop(kysimustik):
    dict2 = kysimustik.copy()
    print("Kui tahad mingi hetk lõpetada, siis vasta küsimusele 'stop'.")
    while any(kysimustik) == True:
        try:
            question = random.choice(list(dict2.keys()))
            print(question)
            vastus = input()
            if vastus.lower() == dict2[question].lower():
                print("Õige!")
                dict2.pop(question)
            elif vastus.lower() == "stop":
                print("Lõpetame ära.")
                break
            elif vastus.lower() == "exit":
                print("Väljumiseks kirjuta 'stop'.")
            else:
                print("Vale vastus.")
        except IndexError:
            print("Küsimused said otsa!")
            break

def lisamine():
    print("Kui enam küsimusi lisada ei soovi, kirjuta 'stop'.")
    while True:
        question = input("Sisesta küsimus:\n")
        if question == "stop":
            break
        elif question in kysimustik:
            print("See küsimus on juba olemas!")
        elif question not in kysimustik:
            vastus = input("Sisesta küsimuse vastus:\n")
            kysimustik[question] = vastus


mainloop()