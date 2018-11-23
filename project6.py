import sys
def credit(amount, years, rate):
    ''' Считаем полученную от вклада сумму '''
    return (amount * (1 + (rate / 100) * years))

def investment(amount, rate, invest):
    """ Считаем срок, за который вкладчик получит доход 'invest' """
    return (invest * 100 * 365)/ (amount * rate)


def main():
    amount = int(input('Введите сумму вклада по кредитам: '))
    years = int(input('Введите срок вклада: '))
    rate = input('Введите ставку в %: ')
    if "%" in rate:
        rate = rate[0:-1]
    rate = int(rate)
    try:
        (amount * (1 + (rate / 100) * years))
    except ZeroDivisionError:
        print('division by 0')
        sys.exit()
    print("Итоговая сумма по вкладу: ", credit(amount, years, rate))

    invest = int(input('Введите сумму, которую хотели бы получить: '))
    try:
        (invest * 100 * 365) / (amount * rate)
    except ZeroDivisionError:
        print('division by 0')
        sys.exit()
    print('Вклад необходимо внести сроком на: ', round(investment(amount, rate, invest), 0), 'дней')


if '__main__' == __name__:
