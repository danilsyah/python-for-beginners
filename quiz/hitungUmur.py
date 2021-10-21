from datetime import date


def ask_for_date(name):
    data = input('Enter ' + name + ' (yyyy-mm-dd) :').split('-')
    try:
        return date(int(data[0]), int(data[1]), int(data[2]))
    except Exception as e:
        print(e)
        print('Invalid input, follow the given format')
        ask_for_date(name)


def calculate_age():
    born = ask_for_date('your date of birth ')
    today = date.today()
    extra_year = 1 if ((today.month, today.day) <
                       (born.month, born.day)) else 0
    return today.year - born.year - extra_year


print(f'Umur Anda Sekarang adalah {calculate_age()} tahun')
