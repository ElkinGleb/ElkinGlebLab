def esc(code):
    return f'\u001b[{code}m'


# Флаг Бангладеш
def flag():
    for i in range(3):
        print(GREEN + '  ' * 35 + END)
    for i in range(1):
        print(GREEN + '  ' * 15 + RED + '  ' * 4 + GREEN + '  ' * 16 + END)
        print(GREEN + '  ' * 14 + RED + '  ' * 6 + GREEN + '  ' * 15 + END)
        print(GREEN + '  ' * 13 + RED + '  ' * 8 + GREEN + '  ' * 14 + END)
        print(GREEN + '  ' * 12 + RED + '  ' * 10 + GREEN + '  ' * 13 + END)
    for i in range(3):
        print(GREEN + '  ' * 11 + RED + '  ' * 12 + GREEN + '  ' * 12 + END)
    for i in range(1):
        print(GREEN + '  ' * 12 + RED + '  ' * 10 + GREEN + '  ' * 13 + END)
        print(GREEN + '  ' * 13 + RED + '  ' * 8 + GREEN + '  ' * 14 + END)
        print(GREEN + '  ' * 14 + RED + '  ' * 6 + GREEN + '  ' * 15 + END)
        print(GREEN + '  ' * 15 + RED + '  ' * 4 + GREEN + '  ' * 16 + END)
    for i in range(3):
        print(GREEN + '  ' * 35 + END)

RED = esc(41)
GREEN = esc(42)
BLUE = esc(44)
WHITE = esc(47)
PURPLE = esc(45)
END = esc(0)
flag()


def uzor():
    n = 5
    for i in range(1):
        print(WHITE + ' ' * 3 + n * (RED + ' ' * 15 + WHITE + ' ' * 6) + END)
    for i in range(1):
        print(WHITE + ' ' * 3 + n * (RED + ' ' * 3 + WHITE + ' ' * 9 + RED + ' ' * 3 + WHITE + ' ' * 6) + END)
    for i in range(1):
        print(WHITE + ' ' * 3 + n * (RED + ' ' * 3 + WHITE + ' ' * 3 + RED + ' ' * 9 + WHITE + ' ' * 6) + END)
    for i in range(1):
        print(WHITE + ' ' * 3 + n * (RED + ' ' * 3 + WHITE + ' ' * 3 + RED + ' ' * 3 + WHITE + ' ' * 12) + END)
    for i in range(1):
        print(WHITE + ' ' * 3 + n * (RED + ' ' * 3 + WHITE + ' ' * 3 + RED + ' ' * 15) + END)


uzor()


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9 ' + END)


array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = 2*i + 3
print(result)

step = round(abs((result[9] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)

# 4
import csv

cnt1 = 0  # кол-во книг до 2015 года
cnt2 = 0  # кол-во книг после 2015 года
with open('bookslab.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    cnt = 0
    for row in list(table):

        if (cnt != 0 and int(row[6][6:10]) <= 2015):
            cnt1 += 1
        else:
            cnt2 += 1
        cnt += 1

b_before2015 = round((cnt1 / cnt * 100))
b_after2015 = round((cnt2 / cnt * 100))


def diagr():
    for i in range(1):
        print(PURPLE + ' ' * int(b_before2015) + END + ' ' + str(b_before2015) + '%')
        print(GREEN + ' ' * int(b_after2015) + END + ' ' + str(b_after2015) + '%')
        print(' ')
        print(PURPLE + ' ' + END + 'Книги до 2015 года' + ' ' + GREEN + ' ' + END + 'Книги после 2015 года')


print('')
diagr()