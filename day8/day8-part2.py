with open('input.txt') as f:
    registers = {}
    greatest = 0
    for line in f:
        key, action, value, logic, key2, op, cond = line.split()
        if eval("registers.get('{}',0) {} {}".format(key2, op, cond)):
            if action == 'inc':
                registers[key] = registers.get(key, 0) + int(value)
            else:
                registers[key] = registers.get(key, 0) - int(value)
        if(registers.get(key, 0) > greatest):
            greatest = registers.get(key)

    print(greatest)
