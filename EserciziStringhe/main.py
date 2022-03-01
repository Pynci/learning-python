# Esercizi tratti dal libro "Python Crash Course"

# 2-3: salvare in una variabile un nome e stampare una frase di saluto
nome = "emilio"
messaggio = f"Ciao {nome}, come stai oggi? Ti va di imparare un po' di python?" # la sintassi con davanti la f serve a "formattare" inserendo i valori delle variabili
print(messaggio)

# 2-4: stampare un nome tutto maiuscolo, tutto minuscolo e con l'iniziale maiuscola
nome = "Matteo"
print(nome.upper())
print(nome.lower())
print(nome.title())

# 2-5: stampare una citazione
autore = "Luca Pinciroli"
frase = "meglio il culo gelato che il gelato nel culo"
citazione = f'{autore} una volta disse: "{frase}".'
print(citazione)

# 2-6: ripulire una stringa dagli spazi indesiderati
stringa = "\nRoberto \t"
print(stringa)
print(stringa.rstrip())
print(stringa.lstrip())
print(stringa.strip())
