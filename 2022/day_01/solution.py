with open('input.txt', 'r') as file:
    text = file.read()
    values = text.split('\n\n')
    calories = []
    index = 0
    for elfNumber in range(len(values)):
        numbers = values[elfNumber].split('\n')
        calorie_sum = 0
        for n in numbers:
            calorie_sum += int(n)
        calories.append(calorie_sum)
        calories.sort(reverse=True)

    print('1st  : ', calories[0])
    print('Top 3: ', sum(calories[0:3]))
