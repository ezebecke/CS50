#print a piramid base on the input namber

#get the input and save it in var height
height = int(input("insert height: "))

#make a loop n(height) number of times
for row in range(height):
    #make loop and print spaces
    for space in range(height, row, -1):
        print(" ", end="")
    #make loop and print simbol "#"
    for simbol in range(row + 2):
        print("#", end="")
    #print a new line, go to next row
    print("")
    
    #Another implementation (might be better)
    #for row in range(height):
    #print(" " * (height-row-1), end="")
    #print("#" * (row+2), end="")
    #print()