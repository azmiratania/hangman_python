from random import randint

# This function takes an integer input and displays corresponding ASCII art.
def display_pics(n):

    graphics =["""

   
        
        
        
         
         
  
 

""","""

   
        
        
        
         
         
  
 _____

""","""

   
  |      
  |      
  |       
  |       
  |       
  |
 _|___

""","""

   _______
  |/      |
  |      
  |       
  |       
  |       
  |
 _|___

""","""

   _______
  |/      |
  |      (_)
  |       
  |       
  |       
  |
 _|___

""","""

   _______
  |/      |
  |      (_)
  |       |
  |       |
  |       
  |
 _|___

""","""

   _______
  |/      |
  |      (_)
  |      \|
  |       |
  |       
  |
 _|___

""","""

   _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |       
  |
 _|___

""","""

   _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      / 
  |
 _|___

""","""

   _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      / \ GAME OVER
  |
 _|___

""","""





    (_)
    \|/
     |
    / \ YOU WIN!

"""]

    print(graphics[n])











# This function allows the user to choose a category.
# Upon choosing a category, a random word selected from category list.
# This function returns the random word and the choosen category name. 
def choose_category():
    
    # Convert string to uppercase and store the words seperated by spaces into the list.
    animals = 'alligator giraffe monkey hippopotamus chameleon gorilla kitten panda sheep rabbit'.upper().split()
    fruits = 'apple orange pear banana blackberry mango peach lychee durian watermelon'.upper().split()
    country = 'Bangladesh China Brazil Singapore India Vietnam Nepal Japan Canada Mexico'.upper().split()
    flowers = 'rose sunflower jasmine dahlia gardenia poppy daffodil daisy tulip hydrangea'.upper().split()


    # Prompt user to choose a category until a valid input is provided. 
    while 1:
        # Handle errors on non-numeric inputs.
        try:
            category_choice = int(input("1. Animals\n2. Fruits\n3. Country\n4. Flowers\nChoose a category [1-4]: "))
        except:
            category_choice = 0
        if category_choice >= 1 and category_choice <= 4:
            break
        else:
            print("Please enter a choice between 1 and 4.\n")

    # Generate a random word from category based on user's category choice
    if category_choice == 1:
        word = animals[randint(0,9)]
        category_name = "Animals"
    elif category_choice == 2:
        word = fruits[randint(0,9)]
        category_name = "Fruits"
    elif category_choice == 3:
        word = country[randint(0,9)]
        category_name = "Country"
    elif category_choice == 4:
        word = flowers[randint(0,9)]
        category_name = "Flowers"
        

    print("\nThe category you have choosen is: ",category_name,"\n" )

    # Return a list containing the random word and category name.
    return [word,category_name]












# This function takes an integer input and displays corresponding alert messages.
def alert_message(n):
    messageList = ["""

-------------------------------------------
| You have already guessed this character |
-------------------------------------------

""","""

-------------------------------------------
|        Character not in the word        |
-------------------------------------------

""","""

-------------------------------------------
|       You can only input alphabets      |
-------------------------------------------

""","""

-------------------------------------------
|     You guessed the word correctly      |
-------------------------------------------

""","""

--------------------------------------------------------
| Please enter either a single character or whole word |
--------------------------------------------------------

""","""

-----------------------------------------------
| That is not the correct match! Keep trying! |
-----------------------------------------------

"""]

    print (messageList[n])
