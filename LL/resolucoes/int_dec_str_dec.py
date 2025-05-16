import decimal

string = '1,2,3,4,5,6,7,8,9,10'
decimal_list = [decimal.Decimal(i) for i in string.split(',')]
integer = 11

print(decimal_list)

print(decimal.Decimal(integer), type(integer))
print(type(decimal_list[0]))