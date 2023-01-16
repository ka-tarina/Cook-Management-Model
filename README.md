README
Description

This project is a model for cook management. It includes classes for Cooks, Recipes, Shopping List, and Plan. The program allows users to add, remove, and manage cooks, as well as create and manage recipes, create a shopping list, and create a plan for meals.
Requirements

    Python 3.x
    typing library

Usage

    Run the main program file using the command python main.py.
    The program will prompt the user to choose an action from a menu.
    The user can choose to manage cooks, recipes, shopping list, or plan.
    Selecting the option to manage cooks will allow the user to add, remove or search cooks.
    Selecting the option to manage recipes will allow the user to create, view, or delete recipes.
    Selecting the option to manage shopping list will allow the user to create a shopping list based on the recipes and servings specified.
    Selecting the option to manage plan will allow the user to add or remove cooks from the plan, and assign them the number of meals they will be cooking.

Classes

    Cook: This class deals with a list of cooks and has methods to show, add, remove, write, get names and read cooks.
    Recipe: This class deals with recipes that the cooks cook, has methods to write recipes, calculate ingredients, create and get recipe names.
    Shopping list: This class deals with the shopping list for cooks based on recipes, has methods to create and write shopping list.
    Plan: This class deals with recipes assigned to cooks and right amounts of food, has methods to add or remove cooks from the plan and assign them the number of meals they will be cooking.

Note

    The program has a method to find the cook which raises a CookNotFoundError if the cook is not found.
    The program has a method to find the recipe which raises a RecipeNotFoundError if the recipe is not found.
    The program has a method to find the recipe which raises a ShoppingListNotFoundError if the shopping list is not found.
    The program has a method to find the recipe which raises a PlanNotFoundError if the plan is not found.
