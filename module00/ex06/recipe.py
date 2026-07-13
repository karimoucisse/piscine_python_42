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
        recipe_name = input("Please enter a recipe name to get its details:\n")
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

def print_cookbook():
    for recipe in cookbook:
        print_recipe_details(recipe)

def print_options_message():
    print("Welcome to the Python Cookbook !")
    print("List of available options:")
    print(" 1: Add a recipe")
    print(" 2: Delete a recipe")
    print(" 3: Print a recipe")
    print(" 4: Print the cookbook")
    print(" 5: Quit\n")

def get_input(message, list_max = 1, data_type= str):
    value = list()
    while len(value) < list_max:
        data = input(message)
        if(data_type == int and not data.isdigit()):
            print("The preparation time should be a positive number!")
            continue
        if data:
            value.append(data)
    return value

def recipe_formules(i):
    if i == 1:
        cookbook[get_input("Enter a name:")[0]] = dict()
    elif i == 2:
        cookbook[list(cookbook)[-1]]["ingredients"] = get_input("Enter ingredients:", 3)
    elif i == 3:
        cookbook[list(cookbook)[-1]]["meal"] = get_input("Enter a meal type:")[0]
    else :
        cookbook[list(cookbook)[-1]]["prep_time"] = get_input("Enter a preparation time:", 1, int)[0]
    return


def add_recipe():
    new_recipe = dict()
    for i in range(1, 5):
        recipe_formules(i)
    print("Recipe created !!")
    return

def quit_prog():
    print("Cookbook closed. Goodbye!")
    exit()   

def main():
    # options = {
    #     "1": add_recipe(),
    #     "2": delete_recipe(),
    #     "3": print_recipe_details(),
    #     "4": print_cookbook(),
    #     "5": quit_prog()    
    # }
    while True:
        print_options_message()
        option = input("Please select an option:\n")
        if not option:
            continue
        
        # if(option in list(options.keys())):
        #     print[option]
        # else:
        #     print("Sorry, this option does not exist.")
        if(option == "1"): 
            add_recipe(),
        elif(option == "2"): 
            delete_recipe(),
        elif(option == "3"): 
            print_recipe_details(),
        elif(option == "4"): 
            print_cookbook(),
        elif(option == "5"): 
            quit_prog()
        else:
            print("Sorry, this option does not exist.")

if __name__=="__main__":
    main()