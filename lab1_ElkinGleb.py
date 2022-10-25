import csv, random
flag = 0

with open('books.csv', 'r') as csvfile:
    numline = len(csvfile.readlines()) - 1
    print ('кол-во записей: ', numline) #кол-во строк

with open('books.csv', 'r') as csvfile:
    str30 = 0
    table = list(csv.reader(csvfile, delimiter = ';'))[1:]
    for row in table:
        if len(row[1]) > 30:
            str30 += 1 #кол-во строк длиннее 30 символов
print('кол-во записей, где название длиннее 30 символов: ', str30)

with open('books.csv', 'r') as csvfile:
    search = input('Search for :').lower()
    book = list(csv.reader(csvfile, delimiter = ';'))[1:]
    for row in book:
        auth = row[4].lower()
        if search in auth:
            for x in range(1900, 2017):
                if str(x) in row[6]:
                    flag = 1
                    print(row[4]+'.', row[1], '-', row[6][0:4])
    if flag == 0:
        print('Nothing found') #поиск по автору (до 2016 года)

f = open('result.txt', 'w')
with open('books.csv', 'r') as csvfile:
    book = list(csv.reader(csvfile, delimiter = ';'))[1:]
    for count in range(1,21):
        numb = random.randrange(1,len(book))
        ran = book[numb]
        f.write(f'{count} {ran[4]}. {ran[1]} - {ran[6][0:4]} \n') #20 книг
f.close()














