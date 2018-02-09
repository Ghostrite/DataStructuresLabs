#Nicholas Salazar
#PartB
#algorithms
import time


def main():
    n = int(input("Fibonacci sequence up to: \n"))
    p =0
    p1=1
    p2=0
    if n==0:
        print("0")

    elif n==1:
        print("0")
        print("1")
    else:
        for i in range(n-1):
            p2 = p+p1
            print(p2)
            p=p1
            p1=p2
    time.sleep(0.5)
    def fib(n):
        if n==0:
            return n
        elif n==1:
            return n
        else:
            return fib(n-1) + fib(n-2)
    print(fib(22))












main()
