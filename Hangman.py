import time
import random

#welcoming the user
name = input("please tell me your name :")
time.sleep(1)

print ("Hello, " + name, "let's play hangman")
time.sleep(1)

print (" ")



super_heroes=("antman","iron man","thor","hulk","spider man","captain america","dr strange","batman","aquaman")


countries=("india","australia","japan","china","russia","america","denmark","south africa")

sports=("tennis","basketball","badminton","cricket","football","hockey","baseball")



print("enter 1 for category SUPER HEROES\n")
time.sleep(1)

print('Enter 2 for category COUNTRIES\n')
time.sleep(1)
print('Enter 3 for category SPORTS\n')
time.sleep(1)
choice=int(input("Enter your choice:"))
time.sleep(1)

if(choice==1):

    print("you have chosen super heroes as your category")
    word=random.choice(super_heroes)    
if(choice==2):

    print("you have chosen countries as your category")
    word=random.choice(countries)
if(choice==3):

    print("you have chosen sports as your category")
    word=random.choice(sports)


   


time.sleep(1)
print ("Start guessing the word below")
time.sleep(1)




#creates a variable with an empty value
guesses = ''
#set the number of attempts
attempts = 15
# Create a while loop
while attempts > 0:        

    # make a counter that starts with zero
    failed = 0            

    # for every character in the word    
    for char in word:
    #for every character the player guesses

        if char in guesses:

            print (char)
        else:
            time.sleep(0.2)
            print("____")
            failed += 1    

   
    #if coubt is still 0 then win
    if failed == 0:        
        print ("You won..WELL DONE!!" )
        print("The word is ", word)
        break              
    #end of while script


    #let the player guess a character
    guess = input("guess a character:")

    #initislize guess to a variable to have a new count for guess
    guesses = guesses + guess                    

    #ifcharacter not found then decrement the number of attempts
    if guess not in word:  
 
   
        attempts -= 1
        time.sleep(1)      
        print ("Wrong guess" )  
        time.sleep(2)
        print( "You have", + attempts, 'more chances' )
        time.sleep(1)

 
   
        if attempts == 0:          
   
       
            print ("OOPS...you lost/n betterluck next time")
            print("The word is ", word)