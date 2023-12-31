# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def count_vowels(word):
    vowels = 'а'
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count

text = input("Введите стихотворение Винни-Пух: ")

phrases = text.split(" ")
syllables_count = None

for phrase in phrases:
    phrase = phrase.replace("-", "")
    phrase_del = count_vowels(phrase)
    if syllables_count is None:
        syllables_count = phrase_del
    elif phrase_del != syllables_count:
        print("Пам парам")
        break

else:
    print("Парам пам-пам")