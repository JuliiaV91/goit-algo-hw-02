
def func_symmetr (s):
    stack =[]
    brackets = {"(": ")", "{": "}", "[": "]"}
    for i in s:
        if i in brackets.keys():
            stack.append(i)
        elif i in brackets.values():
            if not stack or brackets[stack.pop()] != i:
                return "Несиметрично"
    if stack:
            return "Несиметрично"
    else:
        return "Симетрично"
            

print (func_symmetr("( 11 }"))
print (func_symmetr("( 23 ( 2 - 3);"))
print (func_symmetr("( ){[ 1 ]( 1 + 3 )( ){ }}"))