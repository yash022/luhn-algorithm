def luhn_algorithm(credit_card_number):
    every_second_number = list(str(credit_card_number)[1::2])
    multiplied_every_number = []

    for i in every_second_number:
        multiplied_every_number.append(int(i) * 2)

    def count_digits(number):
        number_divide_in_digits = list(str(number))
        num_length = len(number_divide_in_digits)
        return int(num_length)

    def sum_digits(number):
        return sum([int(digit) for digit in str(number)])

    for i in multiplied_every_number:
        if count_digits(i) > 1:
            multiplied_every_number.append(sum_digits(i))
            multiplied_every_number.remove(i)

    def numberatoddplace(number):
        numberatevenplace = list(str(number)[1::2])
        number_divide_in_digits = list(str(number))
        for i in numberatevenplace:
            if i in number_divide_in_digits:
                number_divide_in_digits.remove(i)
        return list(number_divide_in_digits)

    for i in numberatoddplace(credit_card_number):
        multiplied_every_number.append(i)

    final_list = []

    for i in multiplied_every_number:
        final_list.append(int(i))

    sum_sum= sum(final_list)

    if sum_sum % 10 == 0:
        print("credit card number is valid")
    else:
        print("credit card number is not valid")



