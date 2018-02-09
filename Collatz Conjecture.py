#Nicholas Salazar
#Collatz Conjecture
#Lab 4

def main():

    user = int(input("Please enter a positive integer: \n"))
    while user !=1:
    
        if user % 2 == 0:
            user = user/2

        elif user % 2 > 0:
            user = user*3+1
        print(user)







main()
