def getParent(path):
    pos = path.rfind('/', 0, len(path) - 1)
    if pos == 0:
        return '/'
    else:
        return path[0:pos + 1]

content = ''

with open('ex.txt', 'r') as file:
    content = file.read().strip()

lines = content.split('\n')
cwd = '/'
dirs = {}
for line in lines:
    tokens = line.split(' ')
    if tokens[0] == '$':
        ps1 = tokens[0]
        cmd = tokens[1]

        if cmd == 'cd':
            newDir = tokens[2]
            if newDir == '/':
                cwd = '/'
            elif newDir == '..':
                cwd = getParent(cwd)
            else:
                cwd += newDir + '/'
    elif tokens[0] != 'dir':
        if cwd not in dirs.keys():
            dirs[cwd] = 0
        dirs[cwd] += int(tokens[0])

for dirA in dirs.keys():
    if dirA == '/':
        continue
    else:
        parent = getParent(dirA)
        dirs[parent] += dirs[dirA]

print(dirs)
