answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? \n')
answer = answer.replace("-"," ").lower().strip()

if answer == ('42'):
    print ('Yes')
elif answer == 'forty two':
    print ('Yes')
else:
    print ('No')