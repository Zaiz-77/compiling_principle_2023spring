keywords = ['program', 'begin', 'end', 'var', 'integer', 'if', 'then', 'else', 'do', 'while']
operators = ['+', '-', '=', '>', '<']
boarders = [';', ',', ':']
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
    print(f'(3, {out}) const')
    return ch


def alpha_processor(ch: chr) -> chr:
    out = ""
    while ch.isdigit() or ch.isalpha():
        out += ch
        ch = f.read(1)
    print(f'(1, {out}) keyword' if is_keywords(out) else f'(2, {out}) identifier')
    return ch


def other_processor(ch: chr) -> chr:
    if is_operator(ch):
        print(f'(4, {ch}) operator')
    elif is_board(ch):
        print(f'(5, {ch}) boarder')
    ch = f.read(1)
    return ch


if __name__ == '__main__':
    p = f.read(1)
    while p:
        if p.isalpha():
            p = alpha_processor(p)
        elif p.isdigit():
            p = const_processor(p)
        else:
            p = other_processor(p)

