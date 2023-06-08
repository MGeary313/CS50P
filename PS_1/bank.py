greeting = input('Greeting: ')
greeting = greeting.lower().strip()


if greeting[0:5] == 'hello':
    print('$0')
if greeting[0] == 'h':
    if greeting[1:5] != 'ello':
        print('$20')
else:
    print ('$100')
