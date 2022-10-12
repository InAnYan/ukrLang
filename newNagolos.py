import math
import sys
import os
import json
import random


right_comment         = None
wrong_comment         = None
no_such_index_comment = None
not_a_number_comment  = None
your_answer_comment   = None
dict_file             = None
number_of_questions   = None


def main():
    global right_comment        
    global wrong_comment        
    global no_such_index_comment
    global not_a_number_comment 
    global your_answer_comment      
    global dict_file                
    global number_of_questions      

    right_comment = 'Правильно'
    wrong_comment = 'Неправильно'
    no_such_index_comment = 'Такого індексу немає'
    not_a_number_comment = 'Ваша відповідь не є додатнім числом'
    your_answer_comment = 'Ваша відповідь: '
    dict_file = sys.argv[1]
    if not sys.argv[2].isdigit():
        print('Error: passed wrong number')
        exit(4)
    number_of_questions = int(sys.argv[2])
    
    cls()

    questions_list = create_questions(number_of_questions)
    
    print_hi()
    cls()

    for i in range(len(questions_list)):
        test_question(questions_list[i], i + 1)
        cls()

    print_results(questions_list)
    

class Question:
    def __init__(self, word: str, right: [int]):
        assert type(right) == list
        self.word = word
        self.right = right
        self.user_answer = None

    def print(self):
        separator = ' ' * get_digits_count(len(self.word))

        for letter in self.word:
            print(letter, end=separator)

        print('')

        for i in range(len(self.word)):
            print(i + 1, end=separator)

        print('')

    def is_answer_correct(self, answer: str) -> bool:
        if not answer.isdigit():
            print(not_a_number_comment)
            return False
        
        answer_int = int(answer)
        if answer_int > len(self.word) or answer_int <= 0:
            print(no_such_index_comment)
            return False

        return True

    def is_answer_right(self, answer: int) -> bool:
        return answer in self.right

    def is_saved_answer_right(self) -> bool:
        return self.is_answer_right(self.user_answer)
    
    def get_right_answer(self) -> int:
        return self.right

    def get_word(self) -> str:
        return self.word

    def set_user_answer(self, answer: str):
        assert self.is_answer_correct(answer)
        self.user_answer = int(answer)

    def get_user_answer(self) -> str:
        assert self.user_answer != None
        return self.user_answer

    def right_answer_to_str(self) -> str:
        right_str = ''
        if len(self.right) == 1:
            right_str = str(self.right[0])
        else:
            right_str = '['
            for i in range(len(self.right)):
                right_str += str(self.right[i])
                if i != len(self.right) - 1:
                    right_str += ','
            right_str += ']'

        return right_str
    
    def format_user_answer(self) -> [str]:
        res = [self.word,
               self.right_answer_to_str(),
               str(self.user_answer),
               right_comment if self.is_answer_right(self.user_answer) else wrong_comment]

        return res


def open_words_list(filename) -> [(str, [int])]:
    words_dict = None
    try:
        fin = open(filename, 'r', encoding='utf-8')
        words_dict = json.load(fin)
        fin.close()
    except Exception as e:
        print(e)
        print('Error: could not read file \'' + dict_file + '\'')
        exit(2)
    return list(map(lambda x: x if
                    type(x[1]) == list else
                    tuple([x[0], [x[1]]]),
                    list(words_dict.items())))


def choose_words(lst: [(str, [int])], number: int) -> [(str, [int])]:
    random.shuffle(lst)
    return lst[:number]


def form_questions(lst: [(str, [int])]):
    return list(map(lambda x: Question(x[0], x[1]), lst))


def create_questions(number) -> [Question]:
    words_list = open_words_list(dict_file)
    chosen_words = choose_words(words_list, number)
    return form_questions(chosen_words)


def get_digits_count(number: int) -> int:
    return math.floor(math.log(number, 10)) + 1


def test_question(question, number):
    print(str(number) + '. ' + question.get_word() + '\n')
    question.print()
    print('')
    
    while True:
        answer = input(your_answer_comment)
        if not question.is_answer_correct(answer):
            continue
        else:
            question.set_user_answer(answer)
            break


def print_results(questions_list):
    print('Результати: \n')
    
    numbers_space = get_digits_count(len(questions_list))
    word_space = max(map(lambda x: len(x.get_word()),
                         questions_list))
    right_space = max(map(lambda x: len(x.right_answer_to_str()),
                          questions_list))
    answer_space = max(map(lambda x: get_digits_count(x.get_user_answer()),
                           questions_list))
    comment_space = max([len(right_comment), len(wrong_comment)])

    questions_fmt = map(lambda x: x.format_user_answer(), questions_list)

    answers_count = 0
    right_count = 0
    for fmt in questions_fmt:
        print('{: >{}}. {: <{}} {: <{}} {: <{}} {: <{}}'.format(
            answers_count + 1, numbers_space,
            fmt[0], word_space,
            fmt[1], right_space,
            fmt[2], answer_space,
            fmt[3], comment_space))
        
        if questions_list[answers_count].is_saved_answer_right():
            right_count += 1

        answers_count += 1

    print('')
    print(str(right_count) + ' із ' + str(answers_count))
    print('Оцінка: ' + str(round(right_count/answers_count * 12)))

def cls():
    # TODO: Create better solution
    os.system('cls' if os.name=='nt' else 'clear')


def print_hi():
    print("Тренування український наголосів")
    input("Натисніть ENTER для продовження...")
    

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: newNagolos.py dictfile number')
        exit(1)
    main()
