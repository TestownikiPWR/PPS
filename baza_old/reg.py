import os
files = []

for f in os.listdir("C:/Users/Frynio/Desktop/PPS-testownik-291/PPS - testownik - 291/baza"):
    if f.endswith(".txt"):
        files.append(f)

for file in files:
    f = open(file, "r")
    if "szybkość" in f.read().lower():
        print(f)
    f.close()
        
