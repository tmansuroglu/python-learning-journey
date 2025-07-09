def test(name='', value=90, fields=['date', 'location']):
    print(f'name is {name}')
    print(f'value is {value}')
    print(f'fields are {fields}')
    
test(fields=['birthplace', 'surname'], value=50) # order can change

test('Tarkan',fields=['birthplace', 'surname', 'address'], value=75) # order can change

test(name='Peri',fields=['country'], value=99) # order can change



def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# while defining this function, argument order should be kind, *arguments, **keywords
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")