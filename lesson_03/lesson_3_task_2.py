from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S23", "+7-898-353-01-74"),
    Smartphone("Samsung", "A9", "+7-846-186-45-23"),
    Smartphone("Samsung", "S24", "+7-875-435-74-24"),
    Smartphone("iPhone", "16Pro", "+7-865-372-86-77"),
    Smartphone("iPhone", "7", "+7-888-733-56-64")
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.num}")
