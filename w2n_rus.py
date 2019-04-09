#!/usr/bin/python3


# Скрипт преобразет строчные целые числа в цыфровые, работает с числами до 999 999
# Скрипт понимает русскаий язык
# TODO
# 1 - работа с не целыми числами
# 2 - нормальная работа с числами более 1 000 000



russian_number_system = {
    'ноль': 0,
    '0': 0,
    'один': 1,
    'одна': 1,
    '1': 1,
    'два': 2,
    'две': 2,
    '2': 2,
    'три': 3,
    '3': 3,
    'четыре': 4,
    '4': 4,
    'пять': 5,
    '5': 5,
    'шесть': 6,
    '6': 6,
    'семь': 7,
    '7': 7,
    'восемь': 8,
    '8': 8,
    'девять': 9,
    '9': 9,
    'десять': 10,
    '10': 10,
    'одиннадцать': 11,
    '11': 11,
    'двенадцать': 12,
    '12': 12,
    'тринадцать': 13,
    '13': 13,
    'четырнадцать': 14,
    '14': 14,
    'пятнадцать': 15,
    '15': 15,
    'шестнадцать': 16,
    '16': 16,
    'семьнадцать': 17,
    '17': 17,
    'весемьнадцать': 18,
    '18': 18,
    'девятнадцать': 19,
    '19': 19,
    'двадцать': 20,
    '20': 20,
    'тридцать': 30,
    '30': 30,
    'сорок': 40,
    '40': 40,
    'пятьдесят': 50,
    'полтинник': 50,
    '50': 50,
    'шестьдесят': 60,
    '60': 60,
    'семьдесят': 70,
    '70': 70,
    'восемьдесят': 80,
    '80': 80,
    'девяносто': 90,
    '90': 90,
    'сто': 100,
    'сотен': 100,
    'сотня': 100,
    'сотни': 100,
    '100': 100,
    'двести': 200,
    '200': 200,
    'триста': 300,
    '300': 300,
    'четыреста': 400,
    '400': 400,
    'пятьсот': 500,
    '500': 500,
    'шестьсот': 600,
    '600': 600,
    'семьсот': 700,
    '700': 700,
    'восемьсот': 800,
    '800': 800,
    'девятьсот': 900,
    '900': 900,
    'тысяча': 1000,
    'тысячи': 1000,
    'тысяч': 1000,
    '1000': 1000,
    'миллион': 1000000,
    'миллиона': 1000000,
    'миллионов': 1000000,
    '1000000': 1000000,
    'миллиард': 1000000000,
    '1000000000': 1000000000,
    'точка': '.',
    '.': '.'
}

decimal_words = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']


def number_formation(number_words):
    numbers = []
    #print(number_words)
    for number_word in number_words:
        numbers.append(russian_number_system[number_word])

    if len(numbers) == 7:
        #print('len number_words ==>> ', len(numbers))
        if numbers[3] == 1000:
              #print('четвертое слово ==>> 1000')
              sum_thousand = numbers[0] + numbers[1] + numbers[2]
              return sum_thousand * numbers[3] + numbers[4] + numbers[5] + numbers[6]   



    if len(numbers) == 6:
        #print('len number_words ==>> ', len(numbers))
        if numbers[2] == 1000:
              #print('третье слово ==>> 1000')
              sum_thousand = numbers[0] + numbers[1]
              return sum_thousand * numbers[2] + numbers[3] + numbers[4] + numbers[5]
        if numbers[3] == 1000:
              #print('четвертое слово ==>> 1000')
              sum_thousand = numbers[0] + numbers[1] + numbers[2]
              return sum_thousand * numbers[3] + numbers[4] + numbers[5]    


    if len(numbers) == 5:
        #print('len number_words ==>> ', len(numbers))
        if numbers[0] == 1000:
              #print('первое слово ==>> 1000')
              return numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
        if numbers[2] == 1000:
              #print('третье слово ==>> 1000')
              sum_thousand = numbers[0] + numbers[1]
              return sum_thousand * numbers[2] + numbers[3] + numbers[4]
        if numbers[3] == 1000:
              #print('четвертое слово ==>> 1000')
              sum_thousand = numbers[0] + numbers[1] + numbers[2]
              return sum_thousand * numbers[3] + numbers[4]    
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3] + numbers[4]

    if len(numbers) == 4:
        #print('len number_words ==>> ', len(numbers))
        if numbers[0] == 1000:
              #print('первое слово ==>> 1000')
              return numbers[0] + numbers[1] + numbers[2] + numbers[3]
        if numbers[2] == 1000:
              #print('третье слово ==>> 1000')
              sum_thousand = numbers[0] + numbers[1]
              return sum_thousand * numbers[2] + numbers[3]
        if numbers[3] == 1000:
              #print('четвертое слово ==>> 1000')
              sum_thousand = numbers[0] + numbers[1] + numbers[2]
              return sum_thousand * numbers[3]      
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]

    elif len(numbers) == 3:
        #print('len number_words ==>> ', len(numbers))
        #Если первое число X00
        if numbers[0] in [100,200,300,400,500,600,700,800,900]:
            #print(' X00 есть')
            if numbers[1] == 1000:
                #print('второе слово ==>> 1000')
                return numbers[0] * numbers[1] + numbers[2] 
            if numbers[2] == 1000:
                #print('третье слово ==>> 1000')
                sum_thousand = numbers[0] + numbers[1]
                return sum_thousand * numbers[2] 
            return numbers[0] + numbers[1] + numbers[2]
        #если первое число тысяча
        if numbers[0] == 1000:
              #print('первое слово ==>> 1000')
              return numbers[0] + numbers[1] + numbers[2]  
        return numbers[0] * numbers[1] + numbers[2]
    
    elif len(numbers) == 2:
        #print('len number_words ==>> ', len(numbers))
        
        if 1000 in numbers:
            #print(' 1000 есть')
            #print(numbers)
            if numbers[0] == 1000:
              #print('первое слово ==>> 1000')
              return numbers[0] + numbers[1]
            #print('умножаем ')
            res=numbers[0] * numbers[1]
            #print('res == ', res)
            return numbers[0] * numbers[1]

        if 100 in numbers:
            #print(' 1000 есть')
            #print(numbers)
            if numbers[0] == 100:
              #print('первое слово ==>> 1000')
              return numbers[0] + numbers[1]
            #print('умножаем ')
            res=numbers[0] * numbers[1]
            #print('res == ', res)
            return numbers[0] * numbers[1]

        elif 1000000 in numbers:
            #print(' 1000000 есть')
            return numbers[0] * numbers[1]
            
        else:
            return numbers[0] + numbers[1]
    
    else:
        return numbers[0]



def get_decimal_sum(decimal_digit_words):
    decimal_number_str = []
    for dec_word in decimal_digit_words:
        if(dec_word not in decimal_words):
            return 0
        else:
            decimal_number_str.append(russian_number_system[dec_word])
    final_decimal_string = '0.' + ''.join(map(str,decimal_number_str))
    return float(final_decimal_string)



def word_to_num(number_sentence):
    if type(number_sentence) is not str:
        print("введенное значение не является строкой. введите строку")
        return

    number_sentence = number_sentence.replace('-', ' ')
    number_sentence = number_sentence.lower()

    if(number_sentence.isdigit()):
        return int(number_sentence)

    split_words = number_sentence.strip().split()

    clean_numbers = []
    clean_decimal_numbers = []

    # removing and, & etc.
    for word in split_words:
        if word in russian_number_system:
            clean_numbers.append(word)

    #print(clean_numbers)
    

    if len(clean_numbers) == 0:
        print("не корректное число! Введите правильно челое число")
        return

    # Error if user enters million,billion, thousand or decimal point twice
    if clean_numbers.count('тысяча') > 1 or clean_numbers.count('миллион') > 1 or clean_numbers.count('миллиард') > 1 or clean_numbers.count('точка')> 1:
        print("не корректное число! Введите правильно челое число")
        return

    # separate decimal part of number (if exists)
    if clean_numbers.count('точка') == 1:
        clean_decimal_numbers = clean_numbers[clean_numbers.index('point')+1:]
        clean_numbers = clean_numbers[:clean_numbers.index('point')]

    #Узнаем есть ли в строке миллиарды
    billion_index = clean_numbers.index('миллиард') if 'миллиард' in clean_numbers else -1
    #Узнаем есть ли в строке миллионы
    million_index = clean_numbers.index('миллион') if 'миллион' in clean_numbers else -1  
    #Узнаем есть ли в строке тысячи
    thousand_list=['тысяча', 'тысяч', 'тысячи']
    thousand_ind=0
    thousand_index=-1
    for thousand_i in thousand_list:
        if thousand_i in clean_numbers:	
          thousand_index=clean_numbers.index(thousand_i)
          break
        thousand_ind=thousand_ind+1


    
    #print('thousand_index == >> ', thousand_index)
    #print('million_index == >> ', million_index)
    #print('billion_index == >> ', billion_index)


    if (thousand_index > -1 and (thousand_index < million_index or thousand_index < billion_index)) or (million_index>-1 and million_index < billion_index):
        print("не корректное число! Введите правильно челое число")
        return

    total_sum = 0  # storing the number to be returned

    if len(clean_numbers) > 0:
        # hack for now, better way TODO
        if len(clean_numbers) == 1:
                total_sum += russian_number_system[clean_numbers[0]]

        else:
            if billion_index > -1:
                billion_multiplier = number_formation(clean_numbers[0:billion_index])
                total_sum += billion_multiplier * 1000000000

            if million_index > -1:
                if billion_index > -1:
                    million_multiplier = number_formation(clean_numbers[billion_index+1:million_index])
                else:
                    million_multiplier = number_formation(clean_numbers[0:million_index])
                total_sum += million_multiplier * 1000000

            if thousand_index > -1:
                if million_index > -1:
                    thousand_multiplier = number_formation(clean_numbers[million_index+1:thousand_index])
                elif billion_index > -1 and million_index == -1:
                    thousand_multiplier = number_formation(clean_numbers[billion_index+1:thousand_index])
                else:
                    #print(' 123123 === ', clean_numbers)
                    #thousand_multiplier = number_formation(clean_numbers[0:thousand_index])
                    thousand_multiplier = number_formation(clean_numbers)
                #total_sum += thousand_multiplier * 1000
                total_sum += thousand_multiplier

            if thousand_index == -1 and million_index == -1 and billion_index == -1:
                #print('9999999')
                hundreds = number_formation(clean_numbers)
                total_sum += hundreds

     # adding decimal part to total_sum (if exists)
    if len(clean_decimal_numbers) > 0:
        decimal_sum = get_decimal_sum(clean_decimal_numbers)
        total_sum += decimal_sum

    return total_sum




begin = 'y'

while begin != 'n':

 word = input("введите строку c цифрами: ")

 digit = word_to_num(word)
 print('В цифрах это: ',digit)

 begin = input("Продолжаем? (Оставить пустой-да, n-нет): ")