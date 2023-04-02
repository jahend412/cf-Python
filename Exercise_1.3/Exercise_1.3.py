recipes_list = []
ingrediants_list = []

n = int(input("Enter the number of recipes: "))


def take_recipe(name="No name", cooking_time="No cooking time", ingredients="no ingredients", difficulty="no diffculty", recipe="no recipe"):
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time: "))
    ingrediants = input("Enter the ingrediants: ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingrediants': ingrediants.split(', '),
        'difficulty': difficulty
    }
    return recipe


for x in range(n):
    recipe = take_recipe()
    for ingrediant in recipe['ingrediants']:
        if ingrediant not in ingrediants_list:
            ingrediants_list.append(ingrediant)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if int(recipe['cooking_time']) < 10 and len(recipe['ingrediants']) < 4:
        difficulty = 'Easy'
    elif int(recipe['cooking_time']) < 10 and len(recipe['ingrediants']) >= 4:
        difficulty = 'Medium'
    elif int(recipe['cooking_time']) >= 10 and len(recipe['ingrediants']) < 4:
        difficulty = 'Intermediate'
    elif int(recipe['cooking_time']) >= 10 and len(recipe['ingrediants']) >= 4:
        difficulty = 'Hard'

    print('============================================')
    print("Recipe name: " + recipe['name'])
    print('Cooking Time (min): ', recipe['cooking_time'])
    print("Ingrediants: ")
    for ingrediant in recipe['ingrediants']:
        print(ingrediant)
    print("Difficulty: " + difficulty)
    print('============================================')

print('''Ingrediants available across all recipes 
--------------------------------------------''')
ingrediants_list = []
for recipe in recipes_list:
    for ingrediant in recipe['ingrediants']:
        ingrediants_list.append(ingrediant)
    for i in ingrediants_list:
        print(i)
