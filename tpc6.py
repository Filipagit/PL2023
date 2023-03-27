import ply.lex as lex

# Define os tokens e suas expressões regulares
tokens = [
    'INT',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'ASSIGN',
    'EQ',
    'NEQ',
    'LT',
    'LEQ',
    'GT',
    'GEQ',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'PRINT',
    'PROGRAM',
    'FUNCTION',
]

# Expressões regulares para cada token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_ASSIGN = r'='
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LEQ = r'<='
t_GT = r'>'
t_GEQ = r'>='
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_PRINT = r'print'
t_PROGRAM = r'program'
t_FUNCTION = r'function'

# Expressão regular para identificadores (IDs) e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'int':
        t.type = 'INT'
    elif t.value == 'if':
        t.type = 'IF'
    elif t.value == 'else':
        t.type = 'ELSE'
    elif t.value == 'while':
        t.type = 'WHILE'
    elif t.value == 'for':
        t.type = 'FOR'
    elif t.value == 'print':
        t.type = 'PRINT'
    elif t.value == 'program':
        t.type = 'PROGRAM'
    elif t.value == 'function':
        t.type = 'FUNCTION'
    return t

# Expressão regular para números inteiros
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignora espaços em branco e tabulações
t_ignore = ' \t'

# Expressão regular para quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Cria o lexer
lexer = lex.lex()

# Test it out
data = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/
int i;
// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}
// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
'''

# Give the lexer some input
lexer.input(data)
for tok in lexer:
    print(tok)
    