import argparse
#--init-sum - изначальная сумма которую кладем на депозит
# --interest - процентная ставка
# --capitalization - предусмотрена ли капитализация (если не указать то не предусмотрена)
# --period-months - период депозита в месяцах
# --period-years - период депозита в годах

#Функции расчета по окончании срока депозита
def Calculate_with_cap():
    result = init_sum
    for i in range(period_years * 12 + period_months):
        result += (result / 100 * interest) / 12
    return round(result)


def Calculate_without_cap():
    result = init_sum + (init_sum / 100 * interest) * (period_years + period_months / 12)
    return round(result)

#Проверка окончаний для суммы и даты
def month_ending(n) -> int:
    ending = ''
    if n % 10 == 1:
        ending = 'месяц'
    elif 2 <= n % 10 <= 4:
        ending = 'месяца'
    else:
        ending = 'месяцев'
    return ending


def year_ending(n) -> int:
    ending = ''
    if n % 10 == 1:
        ending = 'год'
    elif 2 <= n % 10 <= 4:
        ending = 'года'
    else:
        ending = 'лет'
    return ending


def money_ending(n) -> int:
    if n % 10 == 1:
        ending = 'рубль'
    elif 2 <= n % 10 <= 4:
        ending = 'рубля'
    else:
        ending = 'рублей'
    return ending


class custom_error(Exception):
    pass


parser = argparse.ArgumentParser(description='Process values')

parser.add_argument('-init_sum', type=int, nargs=1, metavar='изначальная сумма которую кладем на депозит')
parser.add_argument('-interest', type=int, nargs=1, metavar='процентная ставка')
parser.add_argument('-capitalization', type=str)
parser.add_argument('-period_years', type=int, nargs=1, default=0, metavar='период депозита в годах')
parser.add_argument('-period_months', type=int, nargs=1, default=0, metavar='период депозита в месяцах')
args = parser.parse_args()


init_sum = args.init_sum[0]
interest = args.interest[0]
capitalization = args.capitalization
period_years = args.period_years[0]
period_months = args.period_months[0]


try:
    if period_years == 0 and period_months == 0:
        raise custom_error
except custom_error:
    print('Укажите значение Периода депозита в годах и/или Периода депозита в месяцах больше 0')
    exit()

try:
    if 0 <= init_sum or init_sum >= 1000000:
        raise custom_error
except custom_error:
    print('Сумма первоначального взноса должна быть от 1 рубля до 1000000 рублей')
    exit()

try:
    if 0 <= interest or interest >= 100:
        raise custom_error
except custom_error:
    print('Процентная ставка дожна быть от 1 до 100 процентов')
    exit()

try:
    if capitalization != 'No' and capitalization != 'Yes':
        raise custom_error
except custom_error:
    print('Признак капитализации должен быть Yes или No')
    exit()


#assert args.period_years[0] and assert args.period_months[0] == 0, 'Введите период депозита'

if capitalization == 'Yes':
    print('Вы положили', init_sum, money_ending(init_sum), 'в банк под', interest, '% на период', period_years, year_ending(period_years), 'и', period_months, month_ending(period_months), 'с капитализацией. По окончании срока депозита у вас будет', Calculate_with_cap(), money_ending(Calculate_with_cap()), '.')
else:
    print('Вы положили', init_sum, money_ending(init_sum), 'в банк под', interest, '% на период', period_years, year_ending(period_years), 'и', period_months, month_ending(period_months), 'без капитализации. По окончании срока депозита у вас будет', Calculate_without_cap(), money_ending(Calculate_without_cap()), '.')


print(' '.join([str(i) for i in (sorted([int(i) for i in list(set(input().split()) & set(input().split()))]))]))