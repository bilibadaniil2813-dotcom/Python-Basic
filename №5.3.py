import string

text = input("Введіть рядок: ")

# замінюємо пунктуацію на пробіли і розбиваємо на слова
translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
words = text.translate(translator).split()

# кожне слово з великої літери, без пробілів
hashtag = "#" + "".join(word.capitalize() for word in words)

# обрізаємо до 140 символів, якщо потрібно
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
