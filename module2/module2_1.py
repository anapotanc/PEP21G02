name = 'jhon'
age = 26

print('name: ', name, 'age= ', age)

# print='print'
# print('name: ', name, 'age= ', age)

# type function
result = type(age)
print(result)

print(5 * name)
result1 = 5 * name
result2 = type(result1)
print(result2)

result = id(name)
print(result)

print(8 + 8)
print((8).__add__(8))

print(8 * 'text')

print((' text').__mul__(8))
print((8).__sub__(8))
print((8).__truediv__(8))

var = (8).__truediv__(8)
result = type(var)
print(result)

print((8).__pow__(8))
print(pow(8, 8))

a = 3
b = 4
c = 5
x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(x)
y = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(y)

bsqr = b.__pow__(2)
multi = (4).__mul__(a.__mul__(c))
dif = bsqr.__sub__(multi)
dif = float(dif)
var = (1).__truediv__(2)
rad = dif.__pow__(var)
b = complex(b)
dif2 = (-b).__sub__(rad)
mul1 = (2).__mul__(a)
ec = dif2.__truediv__(mul1)
print(ec)

nr1 = 1.0 + 1.0j
print(type(nr1))

nr2 = 3 + 5j
print(nr1 + nr2)

my_string = 'my string'
my_str1 = '''
this
is
a
multi
line
text
'''
print(my_str1)

my_str2 = f"""My string {my_str1}"""
print(my_str2)

info = dir(my_str2)
print(info)

var1 = 'this is my text'
cap = var1.capitalize()
print(cap)
format1 = var1.format('Sparta')
print(format1)

# split
# phone = '0747.655.444'
# split1 = phone.split("4")
# print(split1)
# split2 = phone.split(sep=".", maxsplit=1)
# print(split2)

# print(var1, input('give me your name'))

# slice
text = "my text"
first_letter = "my text"[0]
print(first_letter)
slice1 = text[0:7:2]
print(slice1)

# text = input('enter ten characters here: ')
slice1 = text[0:6]
slice2 = text[6:11]
print(slice2 + slice1)

# negative step
text = 'my text'
reverse = text[::-1]
print(reverse)

reverse1 = slice1[::-1]
reverse2 = slice2[::-1]
print(reverse2 + reverse1)

my_bool = True
print(type(my_bool))

print(id(True))
print(id(False))
print(id(2))

print(True + False)
print(dir(True))
x = True.__add__(False)
print(x)

# none

my_none = None

x = print('')
print(x)

# truth
# 0->false
# 'a'->true
# ''->false
# none->false

print(bool(0+0j))
