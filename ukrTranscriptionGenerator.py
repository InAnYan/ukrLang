ukr_temp = {
    'hardV': ['б', 'д', 'з', 'ж', 'дз', 'дж', 'г', 'ґ', ] ,
    'softV': ['д\'', 'з\'', 'дз\''],

    'hardD': ['п', 'т', 'с', 'ш', 'ц', 'ч', 'х', 'к', 'ф'],
    'softD': ['т\'', 'с\'', 'ц\''],

    'hardS': ['м', 'в', 'н', 'л', 'р'],
    'softS': ['н\'', 'л\'', 'р\'', 'й']
}

ukr = {
    'vowel': ['а', 'о', 'у', 'и', 'і', 'е']
}

ukr['voiced']    = ukr_temp['hardV'] + ukr_temp['softV']
ukr['deaf']      = ukr_temp['hardD'] + ukr_temp['softD']
ukr['sonar']     = ukr_temp['hardS'] + ukr_temp['softS']
ukr['hard']      = ukr_temp['hardV'] + ukr_temp['hardD'] + ukr_temp['hardS']
ukr['soft']      = ukr_temp['softV'] + ukr_temp['softD'] + ukr_temp['softS']

ukr['consonant'] = ukr['hard'] + ukr['soft']

ukr['softSpecial'] = ['д', 'т', 'з', 'с', 'ц', 'л', 'н', 'р']

class Phone:
    def __init__(self, letter):
        self.letter = letter
        self.soft = False
        self.semiSoft = False

    def print(self):
        return self.letter

    def isVowel(self):
        return self.letter in ukr['vowel']

    def isConsonant(self):
        return self.letter in ukr['consonant']
    
    def isHard(self):
        return not self.soft and not self.semiSoft

    def isDeaf(self):
        return self.letter in ukr['deaf']

    def isVoiced(self):
        return self.letter in ukr['voiced']

    def isSonar(self):
        return self.letter in ukr['sonar']

    def setSoft(self):
        self.soft = True
        if self.letter in ukr['softSpecial']:
            self.semiSoft = False
        else:
            self.semiSoft = True

    def unsetSoft(self):
        self.soft = False
        self.soft = False
        
    def isSoft(self):
        return self.soft

    def isSemiSoft(self):
        return self.semiSoft

    def isSoftSpecial(self):
        return self.letter in ukr['softSpecial']

def main():
    word = input('Слово: ')
    word = list(word)
    word.append(' ')
    word.append(' ')
    word.append(' ')
    word.append(' ')
    word.append(' ')
    word.insert(0, ' ')
    word.insert(0, ' ')
    word.insert(0, ' ')
    word.insert(0, ' ')
    
    trans = []

    i = 0
    while i < len(word):
        l = word[i]
        
        if l == ' ':
            i += 1
            continue
        elif l == 'ь':
            trans[-1].setSoft()
        elif l == 'і' or l == 'я' or l == 'ю' or l == 'є':
            trans[-1].setSoft()
            trans.append(Phone(l))
        elif l == 'д':
            # TODO: Если разные морфемы
            if word[i + 1] == 'ж':
                trans.append(Phone('дж'))
                i += 1
            elif word[i + 1] == 'з':
                trans.append(Phone('дз'))
                i += 1
        else:
            trans.append(Phone(l))

        i += 1
    
    print('Транскрипція: [ ', end='')
    for e in trans:
        if e.isSoft():
            if e.isSemiSoft():
                print(e.letter+'\'',  end=' ')
            else:
                print(e.letter+'`', end=' ')
        else:
            print(e.letter, end=' ')
    print(']')
    
if __name__ == "__main__":
    main()
