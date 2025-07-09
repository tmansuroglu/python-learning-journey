from function_keyword_arguements import test as print_smth
import function_lambda as lambda_fn
from function_definition import *
from package.fn import print_text

print(print_smth("Tarkan", fields=["birthplace", "surname", "address"], value=75))

print(lambda_fn.make_incrementor(1)(2))

fibo(2000)

print_text("textooo")


# relative imports

# from . import echo
# from .. import formats
# from ..filters import equalizer
