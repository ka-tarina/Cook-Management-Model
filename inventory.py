import os
import re
from typing import Dict, Tuple

#U potpunosti sam zaboravila da sam napravila ovaj modul, primetila sam ga tek pred predaju, tako da predajem bez implementacije.


class Inventory:
    def __init__(self, inventory_file: str = "inventory.txt"):
        self.inventory_file = inventory_file

    def add_ingredient(self, ingredient: str, quantity: float, unit: str) -> None:
        """Add ingredient to the inventory."""
        if self.check_ingredient_exists(ingredient):
            self.update_ingredient_quantity(ingredient, quantity)
        else:
            with open(self.inventory_file, "a") as f:
                f.write(f"{ingredient},{quantity},{unit}\n")

    def remove_ingredient(self, ingredient: str, quantity: float) -> None:
        """Remove an ingredient from the inventory."""
        if self.check_ingredient_exists(ingredient):
            self.update_ingredient_quantity(ingredient, -quantity)
        else:
            raise ValueError (f"Sastojak '{ingredient}' ne postoji u magacinu.")

    def check_ingredient_exists(self, ingredient: str) -> bool:
        """Checks if an ingredient exists in the inventory."""
        with open(self.inventory_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.split(",")[0] == ingredient:
                    return True
            return False

    def update_ingredient_quantity(self, ingredient:str, quantity: float) -> None:
        """Update the quantity of an ingredient in the inventory."""
        with open(self.inventory_file, "r") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            items = line.split(",")
            if items[0] == ingredient:
                new_quantity = float(items[1]) + quantity
                if new_quantity < 0:
                    raise ValueError(f"Količina sastojaka ne može biti manja od 0.")
                else:
                    lines[i] = f"{ingredient},{new_quantity},{items[2]}"
                    break
        else:
            raise ValueError(f"Sastojak '{ingredient}' ne postoji u magacinu/inventaru.")
        with open(self.inventory_file, "w") as f:
            f.writelines(lines)

    def get_ingredient_quantity(self, ingredient:str) -> Tuple[float, str]:
        """Get the quantity and unit of an ingredient in the inventory."""
        with open(self.inventory_file, "r") as f:
            lines = f.readlines()
        for line in lines:
            items = line.split(",")
            if items[0] == ingredient:
                return float(items[1]), items[2].strip()
        raise ValueError(f"Sastojak '{ingredient}' ne postoji u magacinu/inventaru.")

    def get_inventory(self) -> Dict[str, Tuple[float, str]]:
        """Get the entire warehouse inventory as dictionary."""
        inventory = {}
        with open(self.inventory_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                items = line.split(",")
                ingredient = items[0]
                quantity = float(items[1])
                unit = items[2].strip()
                inventory[ingredient] = (quantity, unit)
        return inventory
