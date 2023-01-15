import datetime
import typing as t
from recipe import Recipe
from exceptions import EmptyRecipeListError

"""Model for shopping list class."""


class ShoppingList:
    """Model of an instance of the ShoppingList class."""
    def __init__(self, recipes: t.List[Recipe], servings: t.Dict[Recipe, int]):
        """Initialize the ShoppingList object."""
        if not recipes:
            raise EmptyRecipeListError()
        self.date = datetime.date.today()
        self.recipes = recipes
        self.ingredients = {}
        for recipe, num_servings in servings.items():
            ingredients = recipe.calculate_ingredients(num_servings)
            self.ingredients[recipe.name] = ingredients

    def create_shopping_list(self):
        """Creates a shopping list by adding the quantities of each ingredient in the list of recipes."""
        shopping_list = {}
        for recipe in self.recipes:
            for ingredient in self.ingredients[recipe.name]:
                if ingredient[0] in shopping_list:
                    shopping_list[ingredient[0]]["quantity"] += ingredient[2]
                else:
                    shopping_list[ingredient[0]] = {"measurement": ingredient[1], "quantity": ingredient[2]}
        return shopping_list

    def write_shopping_list(self):
        """Writes the shopping list to a file."""
        with open(f"spisak_za_nabavku_{self.date}.txt", "w") as f:
            for ingredient, info in self.create_shopping_list().items():
                f.write(f"- {ingredient} ({info['quantity']} {info['measurement']})\n")
