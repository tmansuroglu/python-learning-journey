while True:
    try:
        num = int(input('Enter a number: '))
        print(f'entered number is {num}')
    except ValueError:
        print('Invalid value')
    except KeyboardInterrupt:
        print('Byeee')
        break
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise # The most common pattern for handling Exception is to 
              # print or log the exception and then re-raise it (allowing a caller to handle the exception as well):
    else: 
        print('try block is finished and there is no exception')
        break
    finally:
        print('na na na na BATMAN!')
        # If an exception occurs during execution of the try clause, the exception may be handled by an except clause. 
        # If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed.
        # An exception could occur during execution of an except or else clause. 
        # Again, the exception is re-raised after the finally clause has been executed.
        # If the finally clause executes a break, continue or return statement, exceptions are not re-raised.
        # If the try statement reaches a break, continue or return statement, 
        # the finally clause will execute just prior to the break, continue or return statement’s execution.
        # If a finally clause includes a return statement, 
        # the returned value will be the one from the finally clause’s return statement, not the value from the try clause’s return statement.
    
def func():
    raise ExceptionGroup('random Errs',[OSError('error 1'), SystemError('error 2')])

try:
    func()
except ConnectionError as err:
    raise ExceptionGroup('random Errs',[OSError('error 1'), SystemError('error 2')]) from err # redefine the error

try:
    raise NameError('WTF')
except NameError as err:
    err.add_note('Error note is hereee')
    print(f'the error is {err}')
    raise
    
# To indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause:

# except* to handle only the mentioned error