def favor(): # ask to define favor
    favor = int(input("Do you need any help from me? (reply with a positive number for yes and a negative number for no do not type zero).")) # says do you need help
     
    if favor < 0: # if the favor is less than zero
        print("Bye! More upgrades will come!") # say bye! more upgrades will come

        
    else: #if not
        print("The favor would be a fun shape") # says the favor would be a fun shape
        import turtle # first step on bringing the turtle
        import random
        fred = turtle.Pen()# second step on bringing the turtle
        colorlist = ["red","orange","yellow","green","blue","purple","pink"] # make a list called colorlist
        fred.shape("turtle") # Change the shape of the turtle to a turtle
        fred.speed(0) # sets speed to zero
        

        for i in range(456): # repeat 456 times
            col=random.choice (colorlist)# pick a random color from color list
            fred.color(col) # change color to col
            fred.left(78) # turns left 78 degrees
            fred.forward(90) # moves forward 90 pixels

            
    favor2 = int(input(" Do you want another favor? Type a negative number for no and a positive number for yes")) # asks if you want another favor
    if favor2 > 0: #if you asked for the favor
        print("Ok! The other favor is a game called Jerry Guesses") # print the message
        print (" The rules are simple. I will choose a number and all you need to do is guess a number which is greater than the number you can use the numbers from the range of 1-11")# print the message
        numberlist = [ "0","1","2","3","4","5","6","7","8","9","10"] # create list

        
        for i in range(3): # repeat 3 times
             number = random.choice(numberlist) # pick a number in number list
             guess = int(input(" Pick your number!")) # say pick your number
             print("Good Job! The number was...") # say the number was
             print(number) # say the number
       
                 
                 
    print("Bye! More upgrades will come!")   # says bye! more upgrades will come  
    


name = input ("What is your name?") # ask what is your name
print ( "Hello" , name) # says hello your name
print ("My name is Jerry!") # says his name is Jerry
welness = 0 # the variable wellness equals 0
wellness =  int (input ("How are you doing? (respond as a positive number for well and a negetive number for not well do not choose zero)")) # asks if you are doing well


if wellness > 0: # if the variable wellness is greater than zero
    print("Awesome!") # say awesome
    favor() # do the function favor

 
    
else: # if not
    print("Hope you get better!") # says hope you get better
    favor() # do the function favor
    

    


    

