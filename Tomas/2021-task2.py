print ('Kengura 2021 Task 2')

kids_facing = 'FBFFFBF'
number_of_kids = len(kids_facing)
i = 0
answer = 0

for kid in kids_facing:
    if number_of_kids > i+1:
        current = kids_facing[i]
        next = kids_facing[i+1]
        if current == 'F' and next == 'B':
            answer += 1
    i += 1
print (answer)