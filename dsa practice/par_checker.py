from Stack import Stack

def par_checker (string):
    par_stack = Stack()
    balanced = True
    for c in string:
        if c == '(':
            par_stack.push(c)
        else:
            if not par_stack.is_empty():
                if c == ')':
                    par_stack.pop()
                else:
                    balanced = False
            else:
                balanced = False
    if not par_stack.is_empty():
        balanced= False
    return balanced

print(par_checker("("))
print(par_checker("((())"))
print(par_checker("((()))"))
print(par_checker("((())))))"))
print(par_checker("((())())"))