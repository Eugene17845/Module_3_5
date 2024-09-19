def get_multiplied_digits(number):
    str_number = str(number)
    first  = int(str_number[:1])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

number = input('Ведите числа для умножения:',)
result = get_multiplied_digits(number)
print(result)
