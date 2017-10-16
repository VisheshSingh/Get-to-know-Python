from random import randint

ninja_words = [
    'Aiki', 'Buyu', 'Chimonjutsu', 'Cho sen', 'Dojo', 'Gakusei', 'Haiboku',
    'Jin', 'Kenshi', 'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko'
]

def ninjarize(word):
    random_pos = randint(0, len(ninja_words) - 1)
    return f'{word} {ninja_words[random_pos]}'

paragraphs = int(input('enter the number of paragraphs...'))

with open('files/ipsumtext.txt') as original_ipsum:
    items = original_ipsum.read().split()

    for n in range(paragraphs):
        ninja_text = list(map(ninjarize, items))

        with open('files/ninja_ipsum.txt', 'a') as ninja_ipsum:
            ninja_ipsum.write(' '.join(ninja_text) + "\n\n")

