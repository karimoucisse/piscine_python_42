cookbook = {
    "sandwich" :{
        "ingredients":["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
     "cake" :{
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad" :{
        "ingredients": ["avocado", "arugula", "tomatoes","spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}



def print_recipes_name():
    for recipe in cookbook:
        print(recipe)

def print_recipe_details(recipe_name = None):
    if not recipe_name:
        recipe_name = input("Please enter a recipe name to get it details:\n")
    if not recipe_name in list(cookbook.keys()):
        return print("Sorry, this recipe does not exist.")
    recipe = cookbook[recipe_name]
    keys = list(recipe.keys())
    print(f"Recipe for {recipe_name}:")
    print(f" Ingredients list: {recipe[keys[0]]}")
    print(f" To be eaten for {recipe[keys[1]]}.")
    print(f" Takes {recipe[keys[2]]} of cooking.")

def delete_recipe():
    recipe_name = input("Please enter a recipe name to delete it:\n")
    if not recipe_name in list(cookbook.keys()):
        return print("Sorry, this recipe does not exist.")
    cookbook.pop(recipe_name, None)
    if not recipe_name in list(cookbook.keys()):
        print(f"{recipe_name} recipe deleted !")


def print_options_message():
    print("Welcome to the Python Cookbook !")
    print("List of available options:")
    print(" 1: Add a recipe")
    print(" 2: Delete a recipe")
    print(" 3: Print a recipe")
    print(" 4: Print the cookbook")
    print(" 5: Quit\n")

def print_cookbook():
    for recipe in cookbook:
        print_recipe_details(recipe)

def quit_prog():
    print("Cookbook closed. Goodbye!")
    exit() 


def get_input(message, data_type= str):
    value = str()
    while not value:
        value = input(message)
        if(data_type == int and not value.isdigit()):
            print("The preparation time should be a positive number!")
            value = None
            continue            
        if value:
            return value
  fefe
  ffdg
  fgf  

def recipe_formules(i):
    if i == 1:
        cookbook[get_input("Enter a name:\n")] = dict()
    elif i == 2:
        data_list = get_input("Enter ingredients:\n")
        cookbook[list(cookbook)[-1]]["ingredients"] = data_list.split("\n")
    elif i == 3:
        cookbook[list(cookbook)[-1]]["meal"] = get_input("Enter a meal type:\n")
    elif i == 4 :
        prep_time = get_input("Enter a preparation time:\n", int)
        cookbook[list(cookbook)[-1]]["prep_time"] = int(prep_time)
        

def add_recipe():
    for i in range(1, 5):
        recipe_formules(i)
    print("Recipe created !!")


options_functs = {
    '1': add_recipe,
    '2': delete_recipe,
    '3': print_recipe_details,
    '4': print_cookbook,
    '5': quit_prog
}

def main():
    while True:
        print_options_message()
        option = input("Please select an option:\n")
        if not option:
            continue
        funct = options_functs.get(option)
        if not funct :
            print("Sorry, this option does not exist.")
        else :
            funct()       

if __name__=="__main__":
    main()

