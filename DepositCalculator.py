import argparse
import sys


def calculate_with_cap(init_sum, interest, period_years, period_months) -> int:
    result = init_sum
    for i in range(period_years * 12 + period_months):
        result += (result / 100 * interest) / 12
    return round(result)


def calculate_without_cap(init_sum, interest, period_years, period_months) -> int:
    result = init_sum + (init_sum / 100 * interest) * (period_years + period_months / 12)
    return round(result)


def month_ending(period_months) -> str:
    ending = ''
    if period_months % 10 == 1:
        ending = 'месяц'
    elif 2 <= period_months % 10 <= 4:
        ending = 'месяца'
    else:
        ending = 'месяцев'
    return ending


def year_ending(period_years) -> str:
    ending = ''
    if period_years % 10 == 1:
        ending = 'год'
    elif 2 <= period_years % 10 <= 4:
        ending = 'года'
    else:
        ending = 'лет'
    return ending


def money_ending(money) -> str:
    if money % 10 == 1:
        ending = 'рубль'
    elif 2 <= money % 10 <= 4:
        ending = 'рубля'
    else:
        ending = 'рублей'
    return ending


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process values')

    parser.add_argument('-init_sum', type=int, metavar='изначальная сумма которую кладем на депозит')
    parser.add_argument('-interest', type=int, metavar='процентная ставка')
    parser.add_argument('-capitalization', type=int, choices=(0, 1))
    parser.add_argument('-period_years', type=int, default=0, metavar='период депозита в годах')
    parser.add_argument('-period_months', type=int, default=0, metavar='период депозита в месяцах')

    args = parser.parse_args()

    init_sum = args.init_sum
    interest = args.interest
    capitalization = args.capitalization
    period_years = args.period_years
    period_months = args.period_months

    if period_years == 0 and period_months == 0:
        print('Укажите значение Периода депозита в годах и/или Периода депозита в месяцах больше 0')
        sys.exit()

    if 0 >= init_sum >= 1000000:
        print('Сумма первоначального взноса должна быть от 1 рубля до 1000000 рублей')
        sys.exit()

    if 0 >= interest >= 100:
        print('Процентная ставка дожна быть от 1 до 100 процентов')
        sys.exit()

    if capitalization not in (0, 1):
        print('Признак капитализации должен быть 1 или 0')
        sys.exit()

    if capitalization == 1:
        print(f'Вы положили {init_sum} {money_ending(init_sum)} в банк под {interest}% на период {period_years} \
{year_ending(period_years)} и {period_months} {month_ending(period_months)} с капитализацией. \
По окончании срока депозита у вас будет {calculate_with_cap(init_sum, interest, period_years, period_months)} \
{money_ending(calculate_with_cap(init_sum, interest, period_years, period_months))}.')
    else:
        print(f'Вы положили {init_sum} {money_ending(init_sum)} в банк под {interest}% на период {period_years} \
{year_ending(period_years)} и {period_months} {month_ending(period_months)} без капитализации. \
По окончании срока депозита у вас будет {calculate_without_cap(init_sum, interest, period_years, period_months)} \
{money_ending(calculate_without_cap(init_sum, interest, period_years, period_months))}.')
