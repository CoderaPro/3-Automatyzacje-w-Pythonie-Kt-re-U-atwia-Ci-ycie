# Importujemy bibliotekę matplotlib do tworzenia wykresów
import matplotlib.pyplot as plt

# Definiujemy kategorie wydatków, kolory i przygotowujemy miejsce na kwoty
categories = ["Food", "Transport", "Entertainment", "Bills", "Shopping"]
colors = ["red", "blue", "green", "orange", "purple"]
amounts = []

# Pobieramy dane od użytkownika dla każdej kategorii
for category in categories:
    try:
        amount = float(input(f"How much did you spend on {category}? "))
        amounts.append(amount)  # Dodajemy kwotę do listy wydatków
    except ValueError:
        print(
            "Please enter a valid number."
        )  # Obsługa błędu w przypadku nieprawidłowego wejścia

# Tworzymy wykres kołowy
plt.pie(
    amounts,  # Kwoty wydatków
    labels=categories,  # Etykiety kategorii
    colors=colors,  # Kolory odpowiadające kategoriom
    autopct="%1.1f%%",  # Wyświetlanie procentów na wykresie
)

# Ustawiamy równe proporcje osi, aby wykres był okrągły
plt.axis("equal")

# Wyświetlamy wykres
plt.show()
