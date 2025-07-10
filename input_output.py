import json

s = 'Hello, world.'

# str function is meant to return representations of values which are fairly human-readable
print(str(s))

#repr() is meant to generate representations which can be read by the interpreter 
# (or will force a SyntaxError if there is no equivalent syntax). 
print(repr(s))

hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

print(str(hello))

# open(filename, mode, encoding)
# mode can be r(read), w(write), a(append to file's end), r+ ( read and write), if omitted assumed r,
# appending b to mode opens in binary mode
# by default encoding is utf-8
# it is a good practice to use with while dealing with objects. allows file to be closed. alternative is try{...} finally{...}

with open('sample.txt','r+') as file:
    print(file.read())
    file.write('tey')
    file.write(json.dumps([1,2,3,4]))

print(f'is file closed {file.closed}')

