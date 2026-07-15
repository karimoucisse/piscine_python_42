class Recipe:

    def __init__(self, name: str, cooking_lvl: range(1, 5), cooking_time: int,
                ingredients: list, recipe_type: str, description=None) :
        self.name= name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        assert name, "Name can't be NULL"
        assert cooking_lvl,  "cooking_lvl can't be NULL"
        assert cooking_time, "cooking_time can't be NULL" 
        assert ingredients, "ingredients can't be NULL"
        assert recipe_type, "recipe_type can't be NULL"
        
    def __str__(self):
        text=f"{self.name} Infos:\n Cooking level: {self.cooking_lvl}\n Ingredients: {self.ingredients}\n Type: {self.recipe_type}"
        return text