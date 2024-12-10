#Balanced parenthesis

#receiving input

evaluation_string = input("Enter your string:")

def count_parentheses(s):
    open_count = 0  # Counter for opening parentheses
    close_count = 0  # Counter for closing parentheses
    
    for char in s:
        if char == '(':  
            open_count += 1
        elif char == ')':  
            close_count += 1
        else:
            continue
    
    return open_count, close_count

def is_balanced(s):

  open_count, close_count = count_parentheses(evaluation_string)

  if open_count != close_count:
        return(False)

  balance = 0  # Counter for checking the order of parentheses
  for char in evaluation_string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        else:
            continue

        if balance < 0:
            return(False)  # A closing parenthesis before an opening parenthesis

  return(True)

if is_balanced(evaluation_string):
    print(True)
else:
    print(False)
 