elves_calories = []
with open('input.txt','r') as file:
    calorie_count = 0
    
    while True:    
        line = file.readline()

        if line == '\n':
            elves_calories.append(calorie_count)
            calorie_count = 0
            continue
                
        if not line:
            break

        calorie_count += int(line[:-1]) 


elves_calories.sort()
print(f'Top Calorie Count: {elves_calories[-1]}')
print(f'Sum of Top Three: {elves_calories[-1]+elves_calories[-2]+elves_calories[-3]}')


