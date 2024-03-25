import random
import word_list
random_number = random.randint(0,len(word_list.words)-1)

print("Welcome THE HANGMAN")
print("**************")
random_word=word_list.words[random_number]
word=""
letter_in_word=[]
for x in range (len(random_word)):
    word += "_"
    letter_in_word.append(word[x])
    
for i in range(len(word_list.words[random_number])):
    print(word[i], end=" ")
   
print(" ")    

number_of_guesses = 0 
letter_guess = []
true =0
while true!=1:
    print ("To make a guess press 1 ")
    print( "To say a letter press 2")
    operation = input()
    if operation=="2":
        letterr = input("Say letter: ").upper()
        letter_guess.append(letterr)
        for x in range(len(letter_in_word)):
            if letterr == random_word[x]:
                letter_in_word[x]=letterr
        else:
            print("the letter {0} is not in the word ".format(letterr))
        for item in letter_in_word:
            print(item, end=" ")
               
                     
    print(" ")          
    if operation=="1":
        guess= input("What is your guess: ").upper()
        number_of_guesses += 1 
        if guess == word_list.words[random_number]:
            print("You got it on {0}th try".format(number_of_guesses))
            true +=1
        else:
            print("you got it wrong! try again")
            
   






        
    
    
    


        

