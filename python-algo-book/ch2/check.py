def leap_year():
    for year in range(1950, 2050 + 1):
        if (year % 100 == 0) and (year % 400 != 0):
            print(f'{year}: Not Leap Year')
        elif year % 4 == 0:
            print(f'{year}: Leap Year')
        else:
            print(f'{year}: Not Leap Year')


if __name__ == '__main__':
    leap_year()