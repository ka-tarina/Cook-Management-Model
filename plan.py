from recipe import Recipe
from cook import Cook
from typing import List
from exceptions import CookNotFoundError


class Plan:
    class CookPlan(Cook):
        def __init__(self, name: str, surname: str, address: str, ph_number: str, num_meals: int):
            super().__init__(name, surname, address, ph_number)
            self.num_meals = num_meals

    def __init__(self, day: str, date: str, meal: Recipe, cooks: List[CookPlan]):
        self.day = day
        self.date = date
        self.meal = meal
        self.cooks = cooks
        self.ingredients = {}

    def add_cook(self, cook: Cook, num_meals: int) -> None:
        """Adds a cook to the list of cooks and adds the number of meals they can make to the total number of
        meals. It also adds the ingredients needed for the number of meals to the dictionary of ingredients"""
        cook_plan = self.CookPlan(cook.name, cook.surname, cook.address, cook.ph_number, num_meals)
        self.cooks.append(cook_plan)
        ingredients = self.meal.calculate_ingredients(num_meals)
        for ingredient_name, measurement, quantity in ingredients:
            if ingredient_name in self.ingredients:
                self.ingredients[ingredient_name] = (measurement, self.ingredients[ingredient_name][1] + quantity)
            else:
                self.ingredients[ingredient_name] = (measurement, quantity)

    def remove_cook(self, cook: CookPlan, num_meals: int) -> None:
        """Removes a cook from the plan and adds the ingredients that the cook would have used to the ingredients dictionary"""
        try:
            self.cooks.remove(cook)
        except ValueError:
            raise CookNotFoundError()
        else:
            ingredients = self.meal.calculate_ingredients(num_meals)
            for ingredient_name, measurement, quantity in ingredients:
                if ingredient_name in self.ingredients:
                    self.ingredients[ingredient_name] = (measurement, self.ingredients[ingredient_name][1] - quantity)
                else:
                    self.ingredients[ingredient_name] = (measurement, -quantity)

    def write_plan(self):
        """Writes a plan for a given day to a file."""
        with open(f"plan_{self.date}.txt", "w") as f:
            f.write(f"{self.day}\n\n")
            f.write(f"Jelo: {self.meal.name}\n")
            for cook_plan in self.cooks:
                num_meals = cook_plan.num_meals
                ingredients = self.meal.calculate_ingredients(num_meals)
                f.write("\n" + cook_plan.show_cook() + "\n")
                f.write(f"Broj obroka: {cook_plan.num_meals}\n")
                f.write("Namirnice:\n")
                for ingredient in ingredients:
                    f.write(f"- {ingredient[0]} ({ingredient[2]} {ingredient[1]})\n")

    @staticmethod
    def create_plan():
        cooks_names = Cook.get_names()
        recipes = Recipe.get_recipe_names()
        print("Izaberati jelo dana:")
        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}. {recipe}")
        recipe_choice = input("Uneti redni broj recepta: ")
        try:
            recipe_choice = int(recipe_choice) - 1
        except ValueError:
            print("Uneti broj nije validan!")
        else:
            if 0 <= recipe_choice < len(recipes):
                meal_for_day = recipes[recipe_choice]
                meal = Recipe.get_recipe(meal_for_day)
            else:
                print("Uneti broj nije validan!")
        day = input("Uneti dan u nedelji za koji kreiramo plan: ")
        date = input("Uneti datum (YYYY-MM-DD): ")
        cooks = []
        all_cooks = Cook.read_cooks()
        some_plan = Plan(day, date, meal, cooks)
        menu = "1. Dodati kuvare dana\n2. Ukloniti kuvara iz plana\n3. Kreirati plan"
        print(menu)
        plan_choice = input("Uneti izabranu opciju: ")
        status = True
        while status:
            if plan_choice == "1":
                print("Odabrati kuvare: ")
                for i in cooks_names:
                    print(i)
                cook_name = input("Uneti ime odabranog kuvara: ")
                cook_surname = input("Uneti prezime odabranog kuvara: ")
                num_meals = int(input("Uneti broj obroka koji će kuvar pripremati: "))
                try:
                    cook = Cook.find_cook(all_cooks, cook_name.capitalize(), cook_surname.capitalize())
                    some_plan.add_cook(cook, num_meals)
                except CookNotFoundError:
                    print("Cook not found!")
            elif plan_choice == "2":
                cook_name = input("Uneti ime kuvara: ")
                cook_surname = input("Uneti prezime kuvara: ")
                num_meals = int(input("Uneti planirani broj obroka: "))
                try:
                    cook = Cook.find_cook(all_cooks, cook_name, cook_surname)
                except CookNotFoundError:
                    print("Kuvar nije dodeljen planu!")
                else:
                    some_plan.remove_cook(cook, num_meals)
            elif plan_choice == "3":
                some_plan.write_plan()
                status = False
            else:
                print("Nepravilan unos!")
            print(menu)
            plan_choice = input("Uneti izabranu opciju: ")
