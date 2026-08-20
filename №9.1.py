import re
from collections import Counter

def popular_words (text, words):
    """Рахує, скільки разів кожне слово зі списку words зустрічається в text (без урахування регістру)."""
    all_words = re.findall(r'\b\w+\b', text.lower())
    counts = Counter(all_words)
    return {word: counts.get(word, 0)for word in words}

text = '''When I was One I had just begun When I was Two I was nearly new '''
words = ['i', 'was', 'three', 'near']

result = popular_words(text, words)

assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new ''',
['i', 'was', 'three', 'near']
    ) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

for word, count in result.items():
    print(f'{word}: {count}')

    radius = (2.5, 10, 5)
    