content = ''
with open('input.txt', 'r') as file:
    content = file.read().strip()


def containsRange(limitsA, limitsB):
    if limitsA[0] <= limitsB[0] and limitsA[1] >= limitsB[1]:
        return True
    elif limitsA[0] >= limitsB[0] and limitsA[1] <= limitsB[1]:
        return True
    return False

def overlaps(limitsA, limitsB):
    if limitsA[1] >= limitsB[0] and limitsA[0] <= limitsB[0]:
        return True
    elif limitsA[1] >= limitsB[1] and limitsA[0] <= limitsB[1]:
        return True
    return False
        
    
pairs = content.split('\n')
containing = 0
overlapping = 0

for pair in pairs:
    ranges = pair.split(',')
    limitA = ranges[0].split('-')
    limitB = ranges[1].split('-')
    
    minA = int(limitA[0])
    maxA = int(limitA[1])
    minB = int(limitB[0])
    maxB = int(limitB[1])

    if containsRange([minA, maxA], [minB, maxB]):
        containing += 1
    elif overlaps([minA, maxA], [minB, maxB]):
        overlapping += 1

print('Pairs fully containing the other: ', containing)
print('Pairs fulle overlapping with the other: ', overlapping)
print('Sum: ', containing + overlapping)
