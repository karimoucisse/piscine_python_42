from book import Book
from recipe import Recipe
from datetime import date

def main():
    try:
        recipe1 = Recipe("salade", 3, 7, ["tomate", "courgette", "vinaigre"], "starter")
        recipe2 = Recipe("Quiche", 3, 7, ["fromage", "thon", "vinaigre"], "starter")
        recipe_book = Book("mybook")

        recipe_book.add_recipe(recipe1) # ADD recipe1 in recipe book
        recipe_book.add_recipe(recipe2) # ADD recipe2 in recipe book

        get_recipe1 = recipe_book.get_recipe_by_name("salade") # GET recipe by name
        print("Print recipe after a get from recipe book\n", str(get_recipe1))
        
        get_all_starter_recipe = recipe_book.get_recipes_by_types("starter")
        print("\nPrint all starter recipe:")
        for starter_recipe in get_all_starter_recipe:
            print(str(starter_recipe) + '\n')
        
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as ex:
        print(ex) 

if __name__=="__main__":
    main()