import re
from typing import List
from exceptions import CookNotFoundError, CookAlreadyExistsError

"""Model for cook."""


class Cook:
    """Model of an instance of the Cook."""
    def __init__(self, name: str, surname: str, address: str, ph_number: str):
        """Initialize the Cook object."""
        self.name = name
        self.surname = surname
        self.address = address
        self.ph_number = ph_number

    def show_cook(self):
        """Return a string representation of the Cook object."""
        return f"Ime i prezime: {self.name} {self.surname}\nAdresa: {self.address}\nBroj telefona: {self.ph_number}"

    @staticmethod
    def add_cook(cooks: List["Cook"], cook: "Cook") -> None:
        """Appends a Cook object to a list of Cook objects."""
        if cook in cooks:
            raise CookAlreadyExistsError()
        else:
            cooks.append(cook)

    @staticmethod
    def remove_cook(cooks: List["Cook"], cook: "Cook") -> None:
        """Removes a Cook object from a list of Cook objects."""
        try:
            cooks.remove(cook)
        except ValueError:
            raise CookNotFoundError()

    @staticmethod
    def write_cooks(cooks: List["Cook"]):
        """Writes a file from a list of Cook objects."""
        with open("kuvari.txt", "r") as f:
            existing_cooks = {line.strip() for line in f}
        with open("kuvari.txt", "a") as f:
            for cook in cooks:
                cook_str = "Kuvar:\n" + cook.show_cook() + "\n\n"
                if cook_str not in existing_cooks:
                    f.write(cook_str)
                    existing_cooks.add(cook_str)

    @staticmethod
    def get_names() -> List:
        cook_names = []
        with open("kuvari.txt", "r") as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line.startswith("Ime i prezime:"):
                    name_sur = line.split(":")[1].strip()
                    cook_names.append(name_sur)
                i += 1
        return cook_names

    @staticmethod
    def read_cooks() -> List["Cook"]:
        """Reads a file and returns a list of Cook objects."""
        cooks = []
        with open("kuvari.txt", "r") as f:
            lines = f.readlines()
            name = ""
            surname = ""
            address = ""
            phone_number = ""
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line == "Kuvar:":
                    name = ""
                    surname = ""
                    address = ""
                    phone_number = ""
                elif line.startswith("Ime i prezime:"):
                    name_sur = line.split(":")[1].strip()
                    name = name_sur.split()[0]
                    surname = name_sur.split()[1]
                elif line.startswith("Adresa:"):
                    address = line.split(":")[1].strip()
                elif line.startswith("Broj telefona:"):
                    phone_number = line.split(":")[1].strip()
                if name and surname and address and phone_number:
                    cook = Cook(name, surname, address, phone_number)
                    cooks.append(cook)
                i += 1
        return cooks

    @classmethod
    def create_cook(cls):
        """Prompts the user for the name, surname, address, and phone number of a cook and returns a Cook object."""
        while True:
            try:
                name = input("Uneti ime: ").capitalize()
                if not name:
                    raise ValueError("Ime nije uneseno.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                surname = input("Uneti prezime: ").capitalize()
                if not surname:
                    raise ValueError("Prezime nije uneseno.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                address = input("Uneti adresu: ")
                if not address:
                    raise ValueError("Adresa nije uneta.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                ph_number = input("Uneti broj telefona: ")
                if not ph_number:
                    raise ValueError("Broj telefona nije unet.")
                elif not re.match(r"^\d{3}-\d{3}-\d{4}$", ph_number):
                    raise ValueError("Broj telefona mora biti u formatu XXX-XXX-XXXX")
                break
            except ValueError as e:
                print(e)
        return Cook(name, surname, address, ph_number)

    @staticmethod
    def display_cooks(cooks: List["Cook"]) -> None:
        """Displays a list of Cook objects."""
        for i, cook in enumerate(cooks, start=1):
            print(f"{i}. {cook.show_cook()}")

    @staticmethod
    def search_cook(cooks: List["Cook"], query: str) -> "Cook" or None:
        """Takes a list of Cook objects and a string, and returns a list of Cook objects"""
        match = None
        for cook in cooks:
            if query in cook.name or query in cook.surname or query in cook.ph_number:
                match = cook
            elif match is None:
                print("Kuvar ne postoji u listi.")
        return match

    @staticmethod
    def find_cook(cooks, name, surname):
        for cook in cooks:
            if cook.name == name and cook.surname == surname:
                return cook
        raise CookNotFoundError()

    @staticmethod
    def manage_cooks(cooks):
        """Asks the user to choose an action(add/remove cook), and preforms the chosen action."""
        status = True
        while status:
            action = input(
                "Izabrati opciju:\n1. Dodaj kuvara u listu\n2. Obriši kuvara iz liste\n3. Prikaži listu kuvara\n"
                "4. Pretraži listu kuvara\n5. Kraj programa\nUneti izabranu opciju: ")
            try:
                if action == "1":
                    cook = Cook.create_cook()
                    Cook.add_cook(cooks, cook)
                    print("Kuvar je dodat uspešno!")
                    more = input("1. Nastavi\n2. Nazad na upravljanje kuvarima\nUneti izabranu opciju: ")
                    while more == "1":
                        continue
                    else:
                        status = True
                elif action == "2":
                    quiery = input("Uneti ime, prezime ili broj telefona traženog kuvara: ")
                    cook = Cook.search_cook(cooks, quiery.capitalize())
                    try:
                        Cook.remove_cook(cooks, cook)
                        print("Kuvar je obrisan uspešno!")
                    except CookNotFoundError as e:
                        print(e)
                    more = input("1. Nastavi\n2. Nazad na upravljanje kuvarima\nUneti izabranu opciju: ")
                    while more == "1":
                        continue
                    else:
                        status = True
                elif action == "3":
                    Cook.display_cooks(cooks)
                elif action == "4":
                    quiery = input("Uneti ime, prezime ili broj telefona traženog kuvara: ")
                    try:
                        cook = Cook.search_cook(cooks, quiery.capitalize())
                        print(cook.show_cook())
                    except CookNotFoundError():
                        print("Kuvar nije u listi.")
                elif action == "5":
                    Cook.write_cooks(cooks)
                    return cooks
                else:
                    raise ValueError("Uneta opcija ne postoji")
            except ValueError as e:
                print(e)
