print("Գրիր ցանկացած թիվ։ ")
integer = input()

while not(integer.isdigit()):
    print("Ձեր ներմուծածը թիվ չի հանդիսանում։")
    print("Ներմուծեք թիվը։ ")
    integer = input()
    
ones = {'0':'','1':'մեկ ','2':'երկու ','3':'երեք ','4':'չորս ','5':'հինգ ',
        '6':'վեց','7':'յոթ','8':'ութ','9':'ինը',}

teens = {'0':'տաս ','1':'տասնմեկ ','2':'տասներկու ','3':'տասներեք ','4':'տասնչորս ',
        '5':'տասնհինգ ','6':'տասնվեց ','7':'տասնյոթ ','8':'տասնութ ','9':'տասնինը ',}

decades = {'0':'','2':'քսան ','3':'երեսուն ','4':'քառասուն ','5':'հիսուն ','6':'վաթսուն ',
            '7':'յոթանասուն ','8':'ութանասուն ','9':'իննսուն ',}

hundreds = {'0':'','1':'մեկ հարյուր ','2':'երկու հարյուր ','3':'երեք հարյուր ','4':'չորս հարյուր ',
            '5':'հինգ հարյուր ','6':'վեց հարյուր ','7':'յոթ հարյուր ','8':'ութ հարյուր ','9':'ինը հարյուր ',}

comma_word = {'3':'հազար ','6':'միլիոն ','9':'միլիարդ '}

word = ""
integer_side = integer
int_length = len(integer)
integer_change = len(integer)
change = 3

while integer_change > 0:
    if integer == '1':
        word = 'զրո'
        break
    if integer_side[integer_change -2] =='1':
        for digit in teens:
            if integer_side[integer_change -1] ==digit:
                word = teens[digit] + word
    else:
        for digit_1 in ones:
            if integer_side[integer_change - 1] == digit_1:
                word = ones[digit_1] + word
        if integer_change > 1:
            for digit_2 in decades:
                if integer_side[integer_change -2] == digit_2:
                    word = decades[digit_2] + word
    if integer_change > 2:
        for digit_3 in hundreds:
            if integer_side[integer_change - 3] == digit_3:
                word = hundreds[digit_3] + word
    if integer_change > 3:
        word = comma_word[str(change)] + word
    change = change + 3
    integer_change = integer_change - 3

print(F"({word})")
