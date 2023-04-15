keywords = {'program', 'begin', 'end', 'var', 'integer', 'if', 'then', 'else', 'do', 'while'}
operators = {'+', '-', '=', '>', '<'}
boarders = {';', ',', ':', '(', ')'}
dual = {':', '<', '>'}
table = {
    'program': 1,
    'begin': 2,
    'end': 3,
    'var': 4,
    'integer': 5,
    'if': 6,
    'then': 7,
    'else': 8,
    'do': 9,
    'while': 10,
    'ID': 11,
    'CONST': 12,
    '+': 13,
    '-': 14,
    '=': 15,
    '>': 16,
    '<': 17,
    '>=': 18,
    '<=': 19,
    ':': 20,
    ';': 21,
    '(': 22,
    ')': 23,
    ',': 24,
    ':=': 25
}

path = "lib1in.txt"
f = open(path, encoding='utf-8')


def is_keywords(word: str) -> bool:
    return word in keywords


def is_operator(ch: chr) -> bool:
    return ch in operators


def is_board(ch: chr) -> bool:
    return ch in boarders


def const_processor(ch: chr) -> chr:
    out = ""
    while ch.isdigit():
        out += ch
        ch = f.read(1)
    print(f'({table["CONST"]}, {out}) const')
    return ch


def alpha_processor(ch: chr) -> chr:
    out = ""
    while ch.isdigit() or ch.isalpha():
        out += ch
        ch = f.read(1)
    print(f'({table[out]}, {out}) keyword' if is_keywords(out) else f'({table["ID"]}, {out}) identifier')
    return ch


def other_processor(ch: chr) -> chr:
    if is_operator(ch):
        print(f'({table[ch]}, {ch}) operator')
    elif is_board(ch):
        print(f'({table[ch]}, {ch}) boarder')
    ch = f.read(1)
    return ch


def dual_processor(ch: chr) -> chr:
    out = ch
    ch = f.read(1)
    if ch == '=':
        out += ch
        print(f'({table[out]}, {out}) operator')
        ch = f.read(1)
    else:
        print(f'({table[out]}, {out}) operator' if out in "<>" else f'({table[out]}, {out}) boarder')
        return ch
    return ch


if __name__ == '__main__':
    p = f.read(1)
    while p:
        if p.isalpha():
            p = alpha_processor(p)
        elif p.isdigit():
            p = const_processor(p)
        elif p in dual:
            p = dual_processor(p)
        else:
            p = other_processor(p)
