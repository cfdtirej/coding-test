import os
import csv


def next_value(sample_csv: str):
    with open(sample_csv) as f:
        fields = [_ for _ in csv.reader(f)]
        len_fields = len(fields)
    next1, next2, next3 = 1, 2, 3
    flag = True
    while flag:
        for idx in range(len_fields):
            if next1 >= 48:
                next1 = 1
            if next2 >= 48:
                next2 = 1
            if next3 >= 48:
                next3 = 1
            print(
                [
                    fields[idx][0].replace(' ', 'T'), 
                    fields[idx][1],
                    fields[next1][1], 
                    fields[next2][1], 
                    fields[next3][1]
                ]
            )
            next1 += 1
            next2 += 1
            next3 += 1
            if idx == len_fields - 1:
                flag = False


if __name__ == '__main__':
    sample_csv = os.path.join(os.path.dirname(__file__), 'next_value_of_list.csv')
    next_value(sample_csv)