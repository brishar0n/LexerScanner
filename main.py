import re

# Definitions
token_specification = [
    ('NUMBER',    r'\d+(\.\d*)?'),      
    ('ASSIGN',    r':='),               
    ('PLUS',      r'\+'),               
    ('TIMES',     r'\*'),               
    ('DIV',       r'/'),               
    ('LPAREN',    r'\('),               
    ('RPAREN',    r'\)'),               
    ('ID',        r'[A-Za-z_]\w*'),     
    ('SKIP',      r'[ \t]+'),           
    ('MISMATCH',  r'.'),                
]

# Regular expressions
token_re = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
get_token = re.compile(token_re).match

def tokenize(code):
    line = 1
    pos = 0
    match = get_token(code)
    tokens = []
    
    while match is not None:
        type_ = match.lastgroup
        value = match.group(type_)
        if type_ == 'NUMBER':
            tokens.append(('number', value))
        elif type_ == 'ID':
            tokens.append(('id', value))
        elif type_ == 'ASSIGN':
            tokens.append(('assign', value))
        elif type_ == 'PLUS':
            tokens.append(('plus', value))
        elif type_ == 'TIMES':
            tokens.append(('times', value))
        elif type_ == 'DIV':
            tokens.append(('div', value))
        elif type_ == 'LPAREN':
            tokens.append(('lparen', value))
        elif type_ == 'RPAREN':
            tokens.append(('rparen', value))
        elif type_ == 'SKIP':
            pass
        else:
            raise RuntimeError(f'{value} unexpected on line {line}')
        
        pos = match.end()
        match = get_token(code, pos)
    
    return tokens

code = '''Celsius := 100.0
Farenheit := (9/5)*Celsius+32'''

tokens = tokenize(code)

for token in tokens:
    print(f'{token[0]}: {token[1]}')
