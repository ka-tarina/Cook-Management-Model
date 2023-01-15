import os
import re
import typing as t
from exceptions import RecipeNotFoundError, InvalidServingsError

"""Model for recipe class."""


class Recipe:
    """Model of an instance of the Recipe class."""
    def __init__(self, name: str, ingredients: t.List[t.Tuple[str, str, float]], servings: int):
        """Initialize the Recipe object."""
        if servings <= 0:
            raise InvalidServingsError()
        self.name = name
        self.ingredients = ingredients
        self.servings = servings

    def write_recipe(self):
        """Saves the recipe to a folder named recipes"""
        if not os.path.exists('recipes'):
            os.mkdir('recipes')
        with open(f"recipes/{self.name}.txt", "w") as f:
            f.write(f"{self.name} ({self.servings} obroka)\n")
            f.write("Sastojci:\n")
            for ingredient in self.ingredients:
                f.write(f"- {ingredient[0]} ({ingredient[2]} {ingredient[1]})\n")

    def calculate_ingredients(self, num_servings: int) -> t.List[t.Tuple[str, str, float]]:
        """Returns a list of ingredients with the quantities adjusted for the new number of servings."""
        ingredients = []
        for ingredient in self.ingredients:
            ingredient_name, measurement, quantity = ingredient
            new_quantity = quantity * num_servings / self.servings
            ingredients.append((ingredient_name, measurement, new_quantity))
        return ingredients

    @classmethod
    def create_recipe(cls) -> "Recipe":
        """Makes a Recipe instance from user input."""
        name = input("Uneti ime obroka: ")
        servings = int(input("Uneti broj obroka: "))
        ingredients = []
        while True:
            print("Za kraj unosa uneti 'kraj'")
            ingredient_name = input("Uneti sastojak: ")
            if ingredient_name.lower() == "kraj":
                break
            ingredient_measurement = input("Uneti jedinicu mere: ")
            try:
                ingredient_quantity = float(input("Uneti količinu: "))
                ingredients.append((ingredient_name, ingredient_measurement, ingredient_quantity))
            except ValueError:
                print("Količina mora biti broj.")
        return cls(name, ingredients, servings)

    @staticmethod
    def get_recipe_names():
        """Returns a list of names of recipes in the current directory by searching for files ending in ".txt"."""
        recipe_names = []
        for file in os.listdir("recipes"):
            if file.endswith(".txt"):
                recipe_names.append(file[:-4])
        if not recipe_names:
            raise RecipeNotFoundError()
        return recipe_names

    @classmethod
    def get_recipe(cls, name: str) -> "Recipe":
        """Returns a Recipe object with the given name."""
        with open(f"recipes/{name}.txt", "r") as f:
            lines = f.readlines()
        servings_line = lines[0]
        servings_match = re.search(r"\((\d+) obroka\)", servings_line)
        servings = int(servings_match.group(1))
        ingredients = []
        for line in lines[2:]:
            ingredient_match = re.search(r"- (\w+) \((\d+\.\d+)\s*(kg|l|g|ml|kom)\)", line)
            ingredient_name = ingredient_match.group(1)
            ingredient_quantity = float(ingredient_match.group(2))
            ingredient_unit = ingredient_match.group(3)
            ingredients.append((ingredient_name, ingredient_unit, ingredient_quantity))
        return cls(name, ingredients, servings)
