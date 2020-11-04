import sys

SYMBOLS_REVERSE = {
    '(': ')',
    '[': ']',
    '{': '}'
}
CLOSURE_SYMBOLS = SYMBOLS_REVERSE.values()

def is_a_closure_symbol(symbol):
    value = False
    if symbol in CLOSURE_SYMBOLS:
        value = True

    return value

def check_symbols_string(symbols):
    lifo_symbols = []
    for symbol in symbols:
        if is_a_closure_symbol(symbol):
            prev_symbol = lifo_symbols.pop()
            valid_string = symbol == SYMBOLS_REVERSE.get(prev_symbol)
            if not valid_string:
                break
        else:
            lifo_symbols.append(symbol)
    else:
        valid_string = True

    return valid_string

if __name__ == '__main__':
    symbol_string_to_check = sys.argv[1]

    # correct_string = '[()]{}{[()()]()}'
    # wrong_string = '[(])'

    print(
        f'Is {symbol_string_to_check} a correct string?: '
        f'{check_symbols_string(symbol_string_to_check)}',
    )
