userInput = input("Input:")

charRemove = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

for char in charRemove:
    userInput = userInput.replace(char, '')

print(userInput)

