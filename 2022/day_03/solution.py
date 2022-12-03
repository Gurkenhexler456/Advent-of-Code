def getItem(sack):
    length = len(sack)
    compA = sack[:(length >> 1)]
    compB = sack[(length >> 1):length]
    for itemA in compA:
        for itemB in compB:
            if itemA == itemB:
                return itemA

def getBadge(group):
    for a in group[0]:
        for b in group[1]:
            if a != b:
                continue
            for c in group[2]:
                if a == c:
                    return a

def getItemPriority(item):
    if item.islower(): 
        return (ord(item) - ord('a') + 1)
    elif item.isupper():
        return (ord(item) - ord('A') + 27)
    

content = ''
with open('input.txt') as file:
    content = file.read().strip()

rucksacks = content.split('\n')
item_sum = 0
badge_sum = 0
group_sack = 0
group = [''] * 3
for sack in rucksacks:
    common_item = getItem(sack)
    item_sum += getItemPriority(common_item)

    group[group_sack] = sack
    group_sack += 1
    if group_sack == 3:
        group_sack = 0
        badge = getBadge(group)
        badge_sum += getItemPriority(badge)
        
print('Item Priority: ', item_sum)
print('Badge Priority: ', badge_sum)
