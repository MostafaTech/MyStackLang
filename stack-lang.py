import sys

stack = []

def parse_value(command):
    input = command[5:-1]
    if input[0:2] == 'S\'':
        return input[2:-1]
    if input[0:2] == 'N\'':
        return int(input[2:-1])
    if input == 'ARG0': return sys.argv[1]
    if input == 'ARG1': return sys.argv[2]
    if input == 'ARG2': return sys.argv[3]
    if input == 'ARG3': return sys.argv[4]
    if input == 'ARG4': return sys.argv[5]
    return input

def execute(command):
    # check for comments
    if command[0] == '#': return
    # parse operation
    op = command[:4]
    if op == 'PUSH':
        value = parse_value(command)
        stack.append(value)
    if op == 'ADDS':
        v1 = stack.pop()
        v2 = stack.pop()
        res = int(v1) + int(v2)
        stack.append(res)
    if op == 'STRJ':
        item1 = stack.pop()
        item2 = stack.pop()
        res = str(item2) + str(item1)
        stack.append(res)
    if op == 'PRNT':
        last_item = stack.pop()
        print(last_item)
    if op == 'DBUG':
        for i in range(len(stack)):
            print(f'STACK[{i}]\t{stack[i]}')

def run(program_lines):
    for l in program_lines:
        execute(l)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('program file missing.')
    else:
        program_file = sys.argv[1]
        program_lines = []
        with open(program_file, 'r') as f:
            program_lines = f.readlines()
        run(program_lines)
