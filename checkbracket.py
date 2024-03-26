def checkBrackets(str):
    stack = []
    check=True
    for i in str:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
            check=False
            break
            stack.pop()
    if stack:
    check=False
   
    if check:
     print("it is balanced.")
    else:
     print("it is  not balanced.")

str= input("enter the string")
checkBrackets(str)
       