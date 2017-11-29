
#return how many coins to give for the change.

def main():
            
    change = 0.0
    while True:
        print("O hai! How much change is owed?")
        #user input the amount of change
        change = float(input())
        if change > 0:
            break
    
    cents = round (change * 100)
    #new value to keep track of coins
    coinuse = 0
    
    coinuse += cents // 25
    #get the remainder
    cents %= 25 
    
    coinuse += cents // 10
    cents %= 10

    coinuse += cents // 5
    cents %= 5
            
    coinuse += cents // 1
    cents %= 1
    #print number of coins
    print(coinuse)
    
            
if __name__ == "__main__":
    main()
    
    