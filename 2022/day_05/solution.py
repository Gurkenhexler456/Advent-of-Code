content = ''
with open('input.txt', 'r') as file:
    content = file.read()

def readCrates(crate_input):
    lines = crate_input.split('\n')
    seg_size = 4
    cols = round(len(lines[0]) / seg_size)
    crates = [[] for _ in range(cols)]
    for line in lines:
        if '1' in line:
            continue
        for i in range(cols):
            start = i * seg_size
            end = start + seg_size
            seg = line[start:end]
            if len(seg.strip()) > 0:
                crates[i].insert(0, seg[1])
    return crates

def crateMover9000(crates, count, src, dest):
    for i in range(count):
        crate = crates[src].pop()
        crates[dest].append(crate)

def crateMover9001(crates, count, src, dest):
    buf = []
    for i in range(count):
        crate = crates[src].pop()
        buf.insert(0, crate)
    crates[dest] += buf
    

lines = content.split('\n\n')
crates = readCrates(lines[0])
moves = lines[1].split('\n')

for move in moves:
    parts = move.split(' ')
    count = int(parts[1])
    src = int(parts[3]) - 1
    dest = int(parts[5]) - 1
    crateMover9001(crates, count, src, dest)
    
for c in crates:
    print(c[-1], end='')
    
