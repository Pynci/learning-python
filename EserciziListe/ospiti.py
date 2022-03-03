# Primi esercizi sulle liste (gli array vengono chiamati così in python)

# 3-4: Saluti agli ospiti
listaOspiti = ["Mamma", "Papà", "Nonno", "Nonna"]
print(f"Hey {listaOspiti[0]}, vieni a cena da noi stasera?")
print(f"Ciao {listaOspiti[1]}, ti va di venire a cena dopo la partita?")
print(f"Hey {listaOspiti[2]} eccoti! Vieni a cena quando torni dalla montagna?")
print(f"Ciao {listaOspiti[3]}, dai sali con noi a cena!")
print("") # spaziatura

# 3-5: Qualcuno non è potuto venire
print(f"{listaOspiti[1]} non ha fatto in tempo a venire")
listaOspiti[1] = "Sara"

print(f"Hey {listaOspiti[0]}, vieni a cena da noi stasera?")
print(f"Ciao {listaOspiti[1]}, ti va di venire a cena?")
print(f"Hey {listaOspiti[2]} eccoti! Vieni a cena quando torni dalla montagna?")
print(f"Ciao {listaOspiti[3]}, dai sali con noi a cena!")
print("")

# 3-6: ho comprato un tavolo più grande, è in arrivo
print("Ho trovato un tavolo grande in cantina, ci sono dei nuovi invitati!")
listaOspiti.insert(0,"Zio")
listaOspiti.insert(2, "Zia")
listaOspiti.append("Rio")       #avrei anche potuto scrivere listaOspiti.insert(-1, "Rio")
print(f"Hey {listaOspiti[0]}, vieni a cena da noi stasera?")
print(f"Ciao {listaOspiti[1]}, ti va di venire a cena?")
print(f"Hey {listaOspiti[2]} eccoti! Vieni a cena quando torni dalla montagna?")
print(f"Ciao {listaOspiti[3]}, dai sali con noi a cena!")
print(f"Ciao {listaOspiti[4]}, ti va di venire a cena?")
print(f"Ciao {listaOspiti[5]}, ti va di venire a cena?")
print("")

# 3-7: il tavolo non fa in tempo ad arrivare
primoSacrificato = listaOspiti.pop()
secondoSacrificato = listaOspiti.pop()
terzoSacrificato = listaOspiti.pop()
quartoSacrificato = listaOspiti.pop()
quintoSacrificato = listaOspiti.pop()
print(f"Mi dispiace {primoSacrificato}, purtroppo non ho più posto per ospitarti...")
print(f"Mi dispiace {secondoSacrificato}, purtroppo non ho più posto per ospitarti...")
print(f"Mi dispiace {terzoSacrificato}, purtroppo non ho più posto per ospitarti...")
print(f"Mi dispiace {quartoSacrificato}, purtroppo non ho più posto per ospitarti...")
print(f"Mi dispiace {quintoSacrificato}, purtroppo non ho più posto per ospitarti...")

print(f"Hey {listaOspiti[0]}, tu sei ancora invitato")
print(f"Ciao {listaOspiti[1]}, tu sei ancora invitata")

# 3-9: quanti invitati?
print(f"Sono state invitate {len(listaOspiti)} persone.")

del listaOspiti[0]
del listaOspiti[1]