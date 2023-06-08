calc = input('Expression: ')

variable = calc.split()
variable[0] = float(variable[0])
variable[2] = float(variable[2])

if variable[1] == '+':
    print(round(variable[0],1) + round(variable[2],1))
if variable[1] == '-':
    print(round(variable[0],1) - round(variable[2],1))
if variable[1] == '/':
    print(round(variable[0],1) / round(variable[2],1))
if variable[1] == '*':
    print(round(variable[0],1) * round(variable[2],1))

