numbers = open('liczby.txt').read().split('\n')
numbers = list(map(int, numbers))
print(numbers)
# for number in numbers:
#    if int(number) % 2 == 0:
#        print(f"{number} parzysta")
#    else:
#        print(f"{number} nieparzysta")
numbers.sort()
sum = 0
for number in numbers:
    sum += number
avg = sum / len(numbers)
print(f"Srednia:  {avg}, Minimum:  {numbers[0]}, Maksimum:  {numbers[-1]}")
