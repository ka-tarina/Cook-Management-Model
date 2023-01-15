import sys
import typing as t


class Menu:
    def __init__(self, title: str, options: t.List[str]):
        self.title = title
        self.options = options

    def display(self):
        """Displays the menu options."""
        print(self.title)
        print("\n".join(self.options))

    def choose(self) -> str:
        """Prompts the user to choose an option from the menu and returns it."""
        choice = input("Uneti izabranu opciju: ")
        if choice not in (i[0] for i in self.options):
            raise ValueError("Opcija ne postoji.")
        return choice
