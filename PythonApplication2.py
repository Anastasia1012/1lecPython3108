#���� ������ � ����������
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



print(s) # ����� ������

print(a, '-',b, '-', s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print(f)
list = ['1', '2', '3', 'hello']
print(list)

#���� � ����� ������
#print input

print('input a'); #������ 12
a = float(input()) #������������ ��������, int  - ������� ����� �����, ���� ������ input, �� ��� ����� ����������(e.g. 1223)
print('input b'); #������ 23
b = float(input())
print(a, ' + ' , b, ' = ', a+b)
print('{} {}'.format(a, b))
print(f'{a}, {b}')

#�������������� ��������
#+,-,*,/,%,//,**
#**,+,-,*,/,//,%,+,-
#(), ����������� ��������
a = 123
b = -321
c = a+b
print(c)

a = 3
b = 5
a+=5
print(a)

#���������� ��������
#>,>=, <, <=, ==, !=
#not, and, or - �� ������ � &, |, ^
 #is, is not, in, not in
 #gen

f = 1 > 2 or 4 < 6

print(f)

#����������� �����������
#if, if-else

a = int(input('a = ')) #������ 1
b = int(input('b = ')) #������ 2
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
    #print('Hi,', username ) #������ ��� �����
    #print('hi,{0}',username)

#����������� ����������� while
     #��������    
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

#����������� ����������� while-else
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Perhaps')
    print('enough')
print(inverted)

#����������� ����������� for
list = [1,2,3,4,10,5]
for i in list: #������������
    print(i)
print(range(10))
#list=range(10)
i=6
while i<20:
    print(i)
    i+=2

for i in range(6,20,2): #��� �� � ����� �� �������
    print(i)

    #������

    #text = '����� ��� ���� ������ �����' 
    #print(len(text)) ����� �������� ���������� ��������
    #print('���' in text) true ������� ��������� � ������
    #print(text.isdigit()) false ������� �� ������ �� ����
    #print(text.islower()) True ������ �������
    #print(text.replace('���', ���')) ��������
    #for c in text
    #print(c)

    # ���� ����� ���������, �� ������ ctrl ������ ��� �����
    #help �������� ������ ��� ��������� �������

    #   text = '����� ��� ���� ������ ����������� �����' 
    #print(text[0]) c
    #print(text[1]) �
    #print(text[len(text)]) IndexError ����� ������, ��� ��� ���������� � ��� � ����
    #print(text[len(text)-1]) k � ����� ������
    #print(text[-5]) � � ����� ������
    #print(text[:]) print(text) �� ������� �� ���������� �������
    #print(text[:]) �� - ������ � ��������� �����
    #print(text[len(text)-2:]) ��
    #print(text[2:9]) ��� ���
    #print(text[6:-18]) ��� ��� ������
    #print(text[0:len(text):6]) �������
    #print(text[::6]) �������
    #text = text[2:9] + text[-5] + text[:2]
    
    #Lists

    #List - ���������������, ���������� ��������� �������� *������������* �����

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
