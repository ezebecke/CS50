import sys

#must be only 2 command lines
if len(sys.argv) != 2:
    print ("Error")
    sys.exit(1)

#continue only if the command line has alphabetic characters
if sys.argv[1].isalpha() is True:
    
    #take input from user
    userInput = str(input("plaintext: "))
    
    keyIndex = 0
    
    for c in userInput:
        
        #if character is a letter
        if c.isalpha() == True:
        
            #keynumber depends is argv1 is upper or lower case
            if ord(sys.argv[1][keyIndex]) > 90:
                keynumber = 97
            if ord(sys.argv[1][keyIndex]) <= 90:
                keynumber = 65
            
            #if the char from the user input is uppercase:
            if c.isupper() == True:
                
                pr = ((ord(c) - 65) + ord(sys.argv[1][keyIndex]) - keynumber) % 26
                print(chr(pr + 65), end="")
        
                #keep track of what char we are on the cipher command line
                keyIndex += 1
            
            else:
            
                #if is lowercase
                pr = ((ord(c) - 97) + ord(sys.argv[1][keyIndex]) - keynumber) % 26
                print(chr(pr + 97), end="")
        
                keyIndex += 1

            #go to the first char of the key to wrap around, if the plaintext is longer than the command line cipher 
            # we need to start again.
            if keyIndex == len(sys.argv[1]):
                keyIndex = 0
                
        else:
            #print spaces or other chars non alpha
            print(c, end="")
                
    print("")
    


    