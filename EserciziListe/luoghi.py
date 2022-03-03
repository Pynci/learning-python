# 3-8: "ribaltamenti" di liste
luoghiDaVisitare = ["Sidney", "New York", "Barcellona", "Tokyo", "Roma"]
print(f"lista originale: {luoghiDaVisitare}")

print(f"lista ordinata temporaneamente: {sorted(luoghiDaVisitare)}")     # sorted non è un metodo, è una funzione!
print(f"lista originale: {luoghiDaVisitare}")

print(f"lista ordinata al contrario temporaneamente: {sorted(luoghiDaVisitare, reverse=True)}")     # sorted non è un metodo, è una funzione! NB: True ha la T maiuscola
print(f"lista originale: {luoghiDaVisitare}")

luoghiDaVisitare.reverse()
print(f"lista rovesciata: {luoghiDaVisitare}")
print(f"lista originale: {luoghiDaVisitare}")

luoghiDaVisitare.reverse()
print(f"lista ripristinata: {luoghiDaVisitare}")
print(f"lista originale: {luoghiDaVisitare}")

luoghiDaVisitare.sort()
print(f"lista ordinata: {luoghiDaVisitare}")
print(f"lista originale: {luoghiDaVisitare}")

luoghiDaVisitare.sort(reverse=True)
print(f"lista ordinata al contrario: {luoghiDaVisitare}")
print(f"lista originale: {luoghiDaVisitare}")