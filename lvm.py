x = int(input()) 

instructions = []
for _ in range(x):
    instructions.append(input().strip())

stack = []
register = 0
x = 0  

while x < len(instructions):
    parts = instructions[x].split()
    cmd = parts[0]

    if cmd == "PUSH":
        num = int(parts[1])
        stack.insert(0, num)  
        x += 1

    elif cmd == "STORE":
        register = stack.pop(0)
        x += 1

    elif cmd == "LOAD":
        stack.insert(0, register)
        x += 1

    elif cmd == "PLUS":
        a = stack.pop(0)
        b = stack.pop(0)
        stack.insert(0, a + b)
        x += 1

    elif cmd == "TIMES":
        a = stack.pop(0)
        b = stack.pop(0)
        stack.insert(0, a * b)
        x += 1

    elif cmd == "IFZERO":
        jump = int(parts[1])
        val = stack.pop(0)
        if val == 0:
            x = jump
        else:
            x += 1

    elif cmd == "DONE":
        print(stack[0])
        break
