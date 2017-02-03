# Add an import statement here so we can use the random.choice function.
import random

# Create a dictionary of 15 Spanish or French words and their English
# translations. Call the dict vocab. 
vocab = {'negro' : 'black' ,
         'blanco' : 'white' ,
         'greis' : 'grey' ,
         'rojo' : 'red' ,
         'azul' : 'blue' ,
         'amarillo' : 'yellow' ,
         'verde' : 'green' ,
         'naranja' : 'orange' ,
         'azul marino' : 'navy blue',
         'creama' : 'cream' ,
         'rosa' : 'pink' ,
         'violeta' : 'violet' }
         

# Start the game.
print("Let's play Flash Cards!")
right = 0


# Loop until the player gets 7 consecutive words correct.
while right < 7:
    # Create a list called spanish (or french) which contains the
    # keys from your vocab dict.
    spanish = list(vocab.keys())
         

    # Use the choice function to select a random word from the
    # list of keys. Store this word in a variable called question.
    question = random.choice(spanish)

    # Store the corresponding value for that key in a variable
    # called answer.
    answer = vocab[question]

    # Print the question word and prompt the user for a guess.
    print('what is the translation of ' + question + ' in english')
    guess = input('Type here -->    ')
         

    # If guess is equal to answer, print a message stating so and
    # increase the right total by 1. Otherwise, print a message
    # telling the player the correct answer and reset right to zero.
    if guess == answer:
         print('good job ese')
         right += 1
    else:
         print('yeeeeeeeeeet you missed that')
         print('it was acutally')
         print(answer)
         right = 0
    

    # Print the number of consecutive correct answers so far.
    print(' your streak is ' + str(right) + ' words correct')

    # Delete this comment and the pass statement below.
    pass


          
# End the game.
print("Good job. That's 7 correct answers in a row. You win!")
