from typing import Union

def divide(str_with_ints: str) -> Union[float, str]:
    try:
        a, b = map(int, str_with_ints.split())
        return a / b
    except ZeroDivisionError:
        return "Error code: divide by zero"
    except ValueError as v:
        return f"Error code: {str(v)}"
    
print(divide('4 2'))
print(divide('4 0'))
print(divide('* 1'))