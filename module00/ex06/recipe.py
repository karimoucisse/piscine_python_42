cookbook = {
    "Sandwich" :{
        "ingredients":["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
     "Cake" :{
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad" :{
        "ingredients": ["avocado", "arugula", "tomatoes","spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_recipes_name():
    for recipe in cookbook:
        print(recipe)

def print_recipe_details(recipe_name):
    recipe = cookbook[recipe_name]
    keys = list(recipe.keys())
    print(f"{keys[0]}: {', '.join(recipe[keys[0]])}")
    print(f"{keys[1]}: {recipe[keys[1]]}")
    print(f"{keys[2]}: {recipe[keys[2]]}")

def delete_recipe(recipe_name):
    cookbook.pop(recipe_name, None)

def print_menu_message:
    

# def get_input(message, list_max = 1):
#     value = list()

#     while not value and len(value) < list_max:
#         data = input(message)
#         if data:
#             value.append(data)
#     return value

# def recips_formule(i):
#         if i == 1:
#             cookbook[get_input("Enter a name:")[0]] = dict()
#         elif i == 2:
#             cookbook[list(cookbook)[-1]]["ingredients"] = get_input("Enter ingredients:", 3)
#         elif i == 3:
#             cookbook[list(cookbook)[-1]]["meal"] = get_input("Enter a meal type:")[0]
#         else :
#             cookbook[list(cookbook)[-1]]["prep_time"] = get_input("Enter a preparation time:")[0]


# def add_recipe():
#     new_recipe = dict()
#     for i in range(1, 5):
#         recips_formule(i)


    
add_recipe()