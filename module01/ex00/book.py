from datetime import date

class Book:

    def __init__ (self, name: str, last_update= date.today(), creation_date = date.today(), 
            recipes_list= {"starter": list(), "lunch": list(), "dessert": list()}):
        self.name = name
        self.last_update = date.today()
        self.creation_date = date.today()
        self.recipes_list = recipes_list

        assert name, "Name can't be NULL"
        assert date.today(),  "last_update can't be NULL"
        assert date.today(), "creation_date can't be NULL" 
        assert recipes_list, "recipes_list can't be NULL"

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        recipes = self.recipes_list.get(recipe_type)
        # assert recipes, "recipe_type don't exist"
        return recipes

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        new_recipe = recipe
        self.recipes_list[recipe.recipe_type].append(new_recipe)
        self.last_update = date.today()
        # print(self.recipes_list[recipe.recipe_type].name)
        