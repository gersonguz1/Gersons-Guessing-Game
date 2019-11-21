guessCorrect = False
while guessCorrect == False:
    a = int(input("whats my number?"))
    if (a == 10) :
        print("correct!")
        guessCorrect = True
    elif (a < 10) :
        print("its too lowww my friend try higher")
        
    elif (a > 10) :
        print("its too high my friend try lower")
    
    

