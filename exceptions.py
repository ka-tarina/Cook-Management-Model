class Exceptions(Exception):
    """Class to define custom exceptions for the Cook module"""
    def __init__(self, message):
        super().__init__(message)


class CookAlreadyExistsError(Exceptions):
    """Exception raised when a Cook object is added to the list, but it already exists in the list"""
    def __init__(self):
        super().__init__("Kuvar već postoji u listi.")


class CookNotFoundError(Exceptions):
    """Exception raised when a Cook object is not found in the list"""
    def __init__(self):
        super().__init__("Kuvar nije u listi.")


class RecipeNotFoundError(Exceptions):
    """Exception raised when a recipe file is not found"""
    def __init__(self):
        super().__init__("Recept ne postoji.")


class InvalidServingsError(Exceptions):
    """Exception raised when the number of servings is invalid."""
    def __init__(self):
        super().__init__("Broj obroka mora biti veći od 0.")


class InvalidDateError(Exceptions):
    """Exception raised when date is not of type datetime"""
    def __init__(self):
        super().__init__("Datum nije u datetime formatu - DD.MM.GGGG.")


class EmptyRecipeListError(Exceptions):
    """Exception raised when recipe list is empty"""
    def __init__(self):
        super().__init__("Lista recepata ne može briti prazna.")
