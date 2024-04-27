
from collections import deque

def if_string_palindrome ():
    d = deque()
    user_string = input ("Ввід -->")
    symbol_line = user_string.strip().lower() 
    d.extend (symbol_line)
    if d.popleft() == d.pop():
            return f"{symbol_line} - паліндром."
    else: 
         return f"{symbol_line} - не паліндром."
    
print (if_string_palindrome ())
