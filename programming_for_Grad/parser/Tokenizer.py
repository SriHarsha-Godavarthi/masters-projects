
import ply.lex as lex

class Tokenizer:
    # List of token names
  
    def __init__(self,tokens):
       self.tokensFound=[]
       self.reserved={
        'if': 'IF',
        'else': 'ELSE',
        'while': 'WHILE',
        'int': 'INT',
        'return': 'RETURN',
        'exit': 'EXIT',
        'float': 'FLOAT',
        'write': 'WRITE',
        'read': 'READ'
        }
       self.tokens=tokens+list(self.reserved.values())
    def get_tokens(self):
        return self.tokens
        
    # Regular expression rules for tokens
    # t_KEYWORD = r'int|float|if|else|exit|while|read|write|return'
    t_NUMBER=r'\d+(\.\d+)?'
    # Ignored characters whitespace and newline
    t_ignore = r' \t|\n'
    t_STRING_LITRAL=r'\"(\\.|[^"])*\"'
    # t_IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9]*'
    # t_LOGICAL_OPERATOR = r'\|\||&&|<=|>=|!=|=='
    # t_ARITHMETIC_OPERATOR = r'[\+\-\*\%\=]'
    # t_SEPARATOR = r'[;,\(\)\[\]{}]'
    t_COMMENT=r'^/*(.|\n)*?\*/'
    t_LOGICAL_LE = r'<=' 
    t_LOGICAL_GE=r'>='
    t_LOGICAL_EET=r'=='
    t_LOGICAL_NE=r'!='
    t_LOGICAL_AND=r'&&'
    t_NOT=r'!'
    t_PLUS=r'\+'
    t_MINUS=r'\-'
    t_MULTIPLE=r'\*'
    t_DIVIDE=r'\%'
    t_SEMI_COLON=r';'
    t_ASSIGNMENT=r'\='
    t_COMMA=r','
    t_RPAR=r'\)'
    t_LPAR=r'\('
    t_LBRA=r'\{'
    t_RBRA=r'\}'
    t_LBK=r'\['
    t_RBK=r'\]'
    t_LOGICAL_OR=r'\|\|'
    t_GREATER_THEN=r'>'
    t_LESSER_THEN=r'<'
    
    # Error handling
    def t_error(self, t):
        #display illegal character
        print(f"Illegal character: {t.value[0]}")
        # t.lexer.skip(1)
        
    #ignore tab and newline while doing analysis
    def t_IGNORE(self,t):
        r' \t|\n'
        pass
    
    def t_IDENTIFIER(self,t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        t.type = self.reserved.get(t.value, 'IDENTIFIER')
        return t
            

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

    # Test the lexer
    def test(self, data):
        #input source code for analysis
        self.lexer.input(data)
        #get the tokens and info(type,vale) from lexer and process it 
        while True:
            token = self.lexer.token()
            if not token:
                break
            self.tokensFound.append(token.type)
        #display all lexems
        # print(self.tokensFound)
        return self.tokensFound


