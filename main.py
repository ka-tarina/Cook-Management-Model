from cook import Cook
from plan import Plan
from recipe import Recipe
from shopping_list import ShoppingList
from menu import Menu


def main():
    global cook, meal
    menu = Menu(
        "Dobrodošli u program Logistika!\nIzaberite neku od sledećih opcija:",
        [
        "1. Upravljanje kuvarima",
        "2. Kreiranje recepta",
        "3. Kreiranje spiska za nabavku",
        "4. Kreiranje plana za dan",
        "5. Kraj programa"
    ])

    cook1 = Cook("Marko", "Markovic", "Primorska 18", "064-444-4444")
    cooks = [cook1]

    ans = True

    while ans:
        try:
            menu.display()
            choice = menu.choose()
            if choice == "1":
                Cook.manage_cooks(cooks)
                print("Kuvari su uređeni!")
                ans = False
            elif choice == "2":
                recipe = Recipe.create_recipe()
                recipe.write_recipe()
                print("Recept je kreiran!")
                ans = False
            elif choice == "3":
                selected_recipes = []
                recipes = Recipe.get_recipe_names()
                print("Odabrati recepte:")
                for i, recipe in enumerate(recipes, start=1):
                    print(f"{i}. {recipe}")
                while True:
                    recipe_choice = input("Uneti redni broj recepta ili 'kraj' za kraj unosa: ")
                    if recipe_choice.lower() == "kraj":
                        break
                    else:
                        try:
                            recipe_choice = int(recipe_choice) - 1
                        except ValueError:
                            print("Redni broj ne postoji u listi.")
                        else:
                            if 0 <= recipe_choice < len(recipes):
                                selected_recipe_name = recipes[recipe_choice]
                                selected_recipe = Recipe.get_recipe(selected_recipe_name)
                                selected_recipes.append(selected_recipe)
                            else:
                                print("Uneti validan broj!")
                servings = {}
                for recipe in selected_recipes:
                    servings[recipe] = int(input(f"Uneti broj obroka za nabavku za {recipe.name}: "))
                shopping_list = ShoppingList(selected_recipes, servings)
                shopping_list.write_shopping_list()
                print("Spisak za nabavku je kreiran!")
                ans = False
            elif choice == "4":
                Plan.create_plan()
                print("Plan je kreiran!")
                break
            elif choice == "5":
                ans = False
            else:
                raise ValueError("Uneta opcija ne postoji...")
        except ValueError:
            print("Uneta opcija ne postoji... ")
        print("Kraj programa.")


if __name__ == "__main__":
    main()
