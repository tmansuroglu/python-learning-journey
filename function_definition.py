def fibo(limit):
    'This where I document this function. Also called "docstring".'
    
    a,b = 0,1
    
    while a < limit:
        print(a)
        a,b = b, a+b
        
fibo(1000)