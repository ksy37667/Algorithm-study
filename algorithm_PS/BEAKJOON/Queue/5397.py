test_case = int(input())

for _ in range(test_case):
    password = list(input())

    stack1 = []
    stack2 = []

    for i in password:
        if i == '<':
            if stack1:
                stack2.append(stack1.pop())
        elif i == '>':
            if stack2:
                stack1.append(stack2.pop())
        elif i == '-':
            stack1.pop()
        else:
            stack1.append(i)
    
    stack1.extend(reversed(stack2))

    print(''.join(stack1))
