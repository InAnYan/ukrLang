import os
import json
from random import randrange
import os

try:
    from colorama import Fore, Back, Style
except:
    print("напиши: pip install colorama")

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

clearScreen()

print(Fore.YELLOW + "Тренування український наголосів")
input("Натисніть ENTER для продовження...")

clearScreen()

ukrDictFile = """
{
	"агрономія": 4,
	"алфавіт": [4, 6],
	"асиметрія": 8,
	"багаторазовий": 12,
	"бешкет": 2,
	"благовіст": 3,
	"близький": 7,
	"болотистий": 6,
	"бородавка": 4,
	"босоніж": 4
}

"""
ukrDict = json.loads(ukrDictFile)
ukrDict = list(ukrDict.items())

wordsCount = 10
wordsList = []
appendedIndexes = []

def appendToWordsList():
    toAppend = randrange(0, len(ukrDict))
    if not (toAppend in appendedIndexes):
        appendedIndexes.append(toAppend)
        wordsList.append(ukrDict[toAppend])
    else:
        appendToWordsList()

for i in range(wordsCount):
    appendToWordsList()

for i in range(wordsCount):
    print(Fore.YELLOW + str(i + 1) + '. ', end='')
    print(wordsList[i][0] + '\n')

    print(Fore.WHITE, end='')
    for j in range(len(wordsList[i][0])):
        print(wordsList[i][0][j], end='  ' if len(wordsList[i][0]) >= 10 else ' ')
    print('')

    print(Fore.GREEN, end='')
    for j in range(len(wordsList[i][0])):
        print(str(j + 1), end='  ' if len(wordsList[i][0]) >= 10 and not ((j + 1) >= 10) else ' ')
    print('')

    while True:
        num = input(Fore.YELLOW + 'Відповідь: ' + Fore.WHITE)
        try:
            num = int(num)
        except ValueError:
            print(Fore.RED + 'Ваша відповідь не є числом. Спробуйте ще раз')
            continue

        if num > len(wordsList[i][0]) or num <= 0:
            print(Fore.RED + 'Неправильна позиція. Спробуйте ще раз')
            continue
        
        wordsList[i] = (wordsList[i][0], wordsList[i][1], num)
        clearScreen()
        break

print(Fore.YELLOW + 'Результати:\n')

rightCount = 0

maxToPrint = '  '

for i in range(wordsCount):
    if type(wordsList[i][1]) is list:
        toPrint = '['
        for j in range(len(wordsList[i][1])):
            toPrint += str(wordsList[i][1][j])
            if j != len(wordsList[i][1]) - 1:
                toPrint += ','
        toPrint += ']'
        if len(toPrint) > len(maxToPrint):
            maxToPrint = toPrint
            
for i in range(wordsCount):
    print(Fore.YELLOW + '{:2n}. '.format(i + 1) + Fore.WHITE + '{:<15s}'.format(wordsList[i][0]), end=' ')
    
    if type(wordsList[i][1]) is list:
        toPrint = Fore.GREEN + '['
        for j in range(len(wordsList[i][1])):
            toPrint += str(wordsList[i][1][j])
            if j != len(wordsList[i][1]) - 1:
                toPrint += ','
        toPrint += ']'

        print('{0:<{1}}'.format(toPrint, len(maxToPrint)), end=' ')
        
        isNumRight = False
        for num in wordsList[i][1]:
            if wordsList[i][2] == num:
                isNumRight = True
                break

        if isNumRight:
            print(Fore.GREEN + '{:<2d}  Правильно'.format(wordsList[i][2]))
            rightCount += 1
        else:
            print(Fore.RED + '{:<2d}  Неправильно'.format(wordsList[i][2]))
    else:
        print(Fore.GREEN + '{0:<{1}}'.format(str(wordsList[i][1]), len(maxToPrint)), end=' ')
        
        if wordsList[i][1] == wordsList[i][2]:
            print(Fore.GREEN + '{:<2d}  Правильно'.format(wordsList[i][2]))
            rightCount += 1
        else:
            print(Fore.RED + '{:<2d}  Неправильно'.format(wordsList[i][2]))

print(' ')
print(str(rightCount) + ' з ' + str(wordsCount) + ' = ' + str(rightCount/wordsCount))
print(Fore.YELLOW + 'Оцінка: ' + str(int(round((rightCount/wordsCount)*12))) + ' балів')
print(Fore.WHITE + '')
