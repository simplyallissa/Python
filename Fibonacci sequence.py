###Write a function th compoute the nth fibonacci number. Assume n is passed to the function as a parameter.

###1,1,2,3,5,8,13

###recursive function calls itself at least once


def fib(n):
    if n <= 1 :
        return 1
    return fib(n-1) + fib(n-2)

fib(6)
