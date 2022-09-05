#типы данных и переменна€
#int, float, boolen, str, list, None
#print('hello world')

from sre_constants import RANGE


a = 123
b = 1.23
value = None
value = 12334
print(type(value))
print(type(a))
print(type(b))
s = 'hello world'



print(s) # вывод строки

print(a, '-',b, '-', s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print(f)
list = ['1', '2', '3', 'hello']
print(list)

#¬вод и вывод данных
#print input

print('input a'); #ввести 12
a = float(input()) #вещественные значени€, int  - получим целое число, если просто input, то оно будет стороковым(e.g. 1223)
print('input b'); #ввести 23
b = float(input())
print(a, ' + ' , b, ' = ', a+b)
print('{} {}'.format(a, b))
print(f'{a}, {b}')

#јрифметические операции
#+,-,*,/,%,//,**
#**,+,-,*,/,//,%,+,-
#(), —окращенные операции
a = 123
b = -321
c = a+b
print(c)

a = 3
b = 5
a+=5
print(a)

#Ћогические операции
#>,>=, <, <=, ==, !=
#not, and, or - не путать с &, |, ^
 #is, is not, in, not in
 #gen

f = 1 > 2 or 4 < 6

print(f)

#”правл€ющие конструкции
#if, if-else

a = int(input('a = ')) #ввести 1
b = int(input('b = ')) #ввести 2
if a > b:
    print(a)

else:
    print(b)
         
username  = input('input name: ')
if username == 'Maria':
    print('Yeah, it\'s MARIA!')
elif username == 'Marina':
    print('I was waiting for you Marina so much!')
elif username == 'Ilnar':
    print('Ilnar is top)')
else:
    print(f'Hi,', username)
    #print('Hi,', username ) #ввести им€ ћари€
    #print('hi,{0}',username)

#”правл€ющие конструкции while
     #инверси€    
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

#”правл€ющие конструкции while-else
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Perhaps')
    print('enough')
print(inverted)

#”правл€юща€ конструкци€ for
list = [1,2,3,4,10,5]
for i in list: #перечисление
    print(i)
print(range(10))
#list=range(10)
i=6
while i<20:
    print(i)
    i+=2

for i in range(6,20,2): #так же и можно со словами
    print(i)

    #—троки

    #text = 'сьешь еще этих м€гких булок' 
    #print(len(text)) чтобы получить количество символов
    #print('еще' in text) true наличие подстроки в строке
    #print(text.isdigit()) false состоит ли строка из цифр
    #print(text.islower()) True нижний регистр
    #print(text.replace('еще', ≈ў≈')) заменить
    #for c in text
    #print(c)

    # если нужна подсказка, то ставим ctrl пробел или точку
    #help помогает пон€ть что выполн€ет функци€

    #   text = 'сьешь еще этих м€гких французских булок' 
    #print(text[0]) c
    #print(text[1]) ъ
    #print(text[len(text)]) IndexError будет ошибка, так как индексаци€ у нас с нул€
    #print(text[len(text)-1]) k с конца отсчет
    #print(text[-5]) б с конца отсчет
    #print(text[:]) print(text) от первого до последнего символа
    #print(text[:]) съ - перва€ и последн€€ буквы
    #print(text[len(text)-2:]) ок
    #print(text[2:9]) ешь еще
    #print(text[6:-18]) ешь еще м€гких
    #print(text[0:len(text):6]) сеикакл
    #print(text[::6]) сеикакл
    #text = text[2:9] + text[-5] + text[:2]
    
    #Lists

    #List - пронумерованна€, измен€ема€ коллекци€ обьектов *произвольных* типов

    #numbers = [1,2,3,4,5]
    #print(numbers) [1,2,3,4,5]
    #numbers = list(range(1,6))
    #print(numbers) [1,2,3,4,5]
    #numbers[0] = 10
    #for in numbers:
    #    i*=2
    #    print(i) [20,4,6,8,10]
    #    print(numbers) [10,2,3,4,5]
    
numbers = [1, 2, 3, 4, 5]
print(numbers) #[1,2,3,4,5]
ran = range(1, 6)
print(type(ran))
numbers = list(ran)
print(type(numbers))

#print(numbers)
#numbers[0] = 10
#print(f'{len(numbers)} len')
#print(numbers)
#for i in numbers:
#    i *= 2
#    print(i) 
#print(numbers)

#colours = ['red', 'green', 'blue']
#for e in colours:
#    print(e) #red green blue

#for e in colours:
#    print(e*2) #redred greengreen blueblue

#colours.append('gray') #to add in the end
#print(colours == ['red', 'green', 'blue', 'gray']) #True
#colours.remove('red') #del colours[0] to delete

##Functions

#def f(x):
#    if x == 1:
#        return 
#    elif x == 2.3:
#        return 23
#    else:
#        return

#arg = 1
#print(f(arg))
#print(type(f(arg)))
