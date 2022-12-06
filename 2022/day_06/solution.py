def check(buff):
    counter = {}
    for b in buff:
        if b in counter.keys():
            return False
        counter[b] = 1
    return True


content = ''

with open('input.txt', 'r') as file:
    content = file.read().strip()

buff = []
marker_length = 14 # put 4 for start-of-packet marker

for i in range(len(content)):

    if len(buff) == marker_length:
        if check(buff):
            print(i)
            break;
        buff.pop()

    buff.insert(0, content[i])
