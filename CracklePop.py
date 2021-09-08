import time

for x in range(1, 101, 1):
    time.sleep(0.25)
    if ((x % 3 == 0) and (x % 5 != 0)):
        print("Crackle")
        print("\n")
        
    elif ((x % 5 == 0) and (x % 3 != 0)):
        print("Pop")
        print("\n")
        
    elif ((x % 5 == 0) and (x % 3 == 0)):
        print("CracklePop")
        print("\n")

    else:
        print(x)
        print("\n")
