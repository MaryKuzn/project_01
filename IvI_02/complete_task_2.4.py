# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

s_1 = ("Hi! Hello!")
s_2 = ("Oh, no!!!")
def remove_exclamation_marks(s):
    str = s.split('!')
    print("".join(str))

#remove_exclamation_marks(s_1)


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

s_1 = ("Hi!")
s_2 = ("Hi!!!")
s_3 = ("!Hi")
def remove_last_em(s):
    if s[-1] == '!':
        str = s.replace('!', '', 1)
        print(str)
    else: 
       print(s)    
        
#remove_last_em(s_1)

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"
s_1 = ("Hi!")
s_2 = ("Hi! Hi!")
s_3 = ("Hi! Hi! Hi!")
s_4 = ("Hi Hi! Hi!")

def remove_word_with_one_em(s, char):
    pass