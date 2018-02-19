#Nicholas Salazar
#PartB
#algorithms
import time


def main():
    
    n = int(input("Fibonacci sequence up to: \n"))
    p =0
    p1=1
    p2=0
    print("Nonrecursive:")
    st = time.time()
    if n==0:
        print("0")

    elif n==1:
        print("0")
        print("1")
    else:
        for i in range(n-1):
            p2 = p+p1
            p=p1
            p1=p2
        print(p2)
    et = time.time()
    ft1 = et - st
    st1 = time.time()
    def fib(n):
        if n<=1:
            return n
        else:
            return fib(n-1) + fib(n-2)

    print("Recursive:",fib(n))

    et1 = time.time()
    ft2 = et1-st1
    print("\nTime Took:\nNonrecursive:",ft1,"\nRecursive:",ft2,"\nThe difference"\
          " between them both:",ft2-ft1)
    if ft2>ft1:
        print("nonrecursive function was faster for calculating the",n\
              ,"fibonacci number")
    else:
        print("recursive function was faster for calculating the",n\
              ,"fibonacci number\n\n")
    st2 = time.time()
    def fib2(n):
        p1 = [0,1]
        for i in range(2,n+1):
            p1.append(p1[i-1]+p1[i-2])
        return p1[n]
    print("\nDynamic Programming:",fib2(n))
    et2 = time.time()
    ft3 = et2-st2
    print("Time took:",ft3)
    if ft3<ft1:
        print("Dynamic Programming was faster than nonrecursive by:",ft1-ft3\
              ,"seconds")
    if ft3<ft2:
        print("Dynamic Programming was faster than recursive by:",ft2-ft3\
              ,"seconds")
    
    else:
        print("Dyanamic Programming was slower than both nonrecursive and recursive\nRecursive:",\
              ft2-ft3,"seconds faster\nNonrecursive:",ft1-ft3,"seconds faster")











main()
