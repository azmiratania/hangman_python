import time

# Import the HangmanFunctions.py module, which contains the funtions, from the same folder
import HangmanFunctions


# Allow the user to play again
while 1:
    # Call choose_category function and store the random word and category name
    cat_list = HangmanFunctions.choose_category()
    word = cat_list[0]
    category_name = cat_list[1]

    word_length = len(word)
    print("The word to guess is",word_length," characters long")

    # Seperate the individual characters of the random word
    word_list = list(word)

    # Create a empty list to store correctly guessed words
    guessed_char = list(word)
    for i in range(0,word_length):
        guessed_char[i] = ""

    # An empty list to store previously guessed characers
    previous_inputs = []

    max_tries = 9
    tries = 0
    guess_char = ""

    while 1:
        # Call ASCII art function with current number of tries
        HangmanFunctions.display_pics(tries)

        # Check if the user exceeded 9 tries and end the game 
        if tries >= max_tries:
            print("YOU FAIL!")
            print("Correct word: ",word)
            break

        # Display category name with blank lines or correct guessed characters
        print(category_name,":", end = " ")
        for i in range(0, word_length):
            # Check if currently guessed characters is correct
            if guess_char == word_list[i]:
                guessed_char[i] = guess_char
                print(guessed_char[i],end =" ")
            # Display correctly guessed previous characters    
            elif guessed_char[i] == word_list[i]:
                print(guessed_char[i],end =" ")
            else:
                print("_",end =" ")
        print()

        # Check if all the characters have been correctly guessed
        if guessed_char == word_list:
            HangmanFunctions.display_pics(10)
            break

        # Display all previously guessed characters
        if len(previous_inputs)> 0:
            print("Previous guesses: ",end = "")
            for d in previous_inputs:
                print(d,end = " ")
            print()

        # Ask the user for a character    
        guess_char = input("Please input a character or guess the word: ")

        guess_char = guess_char.upper()
        input_length = len(guess_char)
        
        # Check if user entered a single character
        if input_length == 1:
            charnum = ord(guess_char)
            # Check the character is an alphabet, otherwise display error message
            if (charnum >= 65 and charnum <=90) or (charnum >= 97 and charnum <= 122):
                # Check that the character has been previously entered
                if guess_char in previous_inputs:
                    HangmanFunctions.alert_message(0)
                # Check if the user entered a correct character
                elif guess_char in word_list:
                    previous_inputs.append(guess_char)
                # For wrong character input, increment tries by 1 and show error message.
                else:
                    tries+=1
                    previous_inputs.append(guess_char)
                    HangmanFunctions.alert_message(1)
            else:
                HangmanFunctions.alert_message(2)
        # Check if the user guessed the whole word, otherwise display error
        elif input_length == word_length:
            # Check if the whole word was correctly guessed
            if guess_char == word:
                HangmanFunctions.alert_message(3)
                HangmanFunctions.display_pics(10)
                break
            else:
                tries+=1
                HangmanFunctions.alert_message(5)
        else:
            HangmanFunctions.alert_message(4)

    # Prompt the user to play again
    playAgain = input("Would you like to play again? (Y/N): ")
    if playAgain == "N" or playAgain == "n" :
        break
    else:  
        print()
        print()
        print() 
