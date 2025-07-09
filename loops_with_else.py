for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else: # in a for loop else clause is executed after the loop finishes its final iteration, that is, if no break occurred.
        print(n, 'is a prime number')
        
        
a = 0

print('-----------------------')

while a < 10:
    a = a + 1
    print(a)
else: # in a while loop, it’s executed after the loop’s condition becomes false.
    print('while ended')