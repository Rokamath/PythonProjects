while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

#Iteration with continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')