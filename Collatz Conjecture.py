#Nicholas Salazar
#Collatz Conjecture
#Lab 4

def main():
    global counter
    counter =0
    user = int(input("Please enter a positive integer: \n"))
    def CC(user):
        global counter
        print(user)
        if user !=1:
            if user % 2 == 0:
                counter = counter+1
                return CC(user/2)
            elif user % 2 > 0:
                counter = counter+1
                return CC(user*3+1)
        elif user ==1:
            print("Number of steps:",counter)
    print(CC(user))


main()
