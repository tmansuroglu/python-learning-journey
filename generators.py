# kind of fuction that uses
# yield instead of return
# can be paused and resumed
# produces lazy sequence (values one at a time)
# Generators are exhaustible — once used, they're done.


def count_up_to(num):
    i = 1

    while i <= num:
        yield i
        i += 1


iterable = count_up_to(3)

for i in iterable:
    print(i)

# this wont work. because generators are exahustable
for i in iterable:
    print(i)
# print(next(iterable))  # raises StopIteration
