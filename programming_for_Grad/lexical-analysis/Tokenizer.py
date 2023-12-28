
import ply.lex as lex

class Tokenizer:
    # List of token names
    tokens = [
        'KEYWORD',
        'IDENTIFIER',
        'CONSTANT',
        'LOGICAL_OPERATOR',
        'ARITHMETIC_OPERATOR',
        'SEPARATOR',
        'COMMENT'
    ]
    def __init__(self):
       self.tokensFound=""
    # Regular expression rules for tokens
    t_KEYWORD = r'int|float|if|else|exit|while|read|write|return'
    t_IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9]*'
    t_CONSTANT = r'\d+(\.\d+)?'
    t_LOGICAL_OPERATOR = r'\|\||&&|<=|>=|!=|=='
    t_ARITHMETIC_OPERATOR = r'[\+\-\*\%\=]'
    t_SEPARATOR = r'[;,\(\)\[\]{}]'
    t_COMMENT=r'^/*(.|\n)*?\*/'
    
    # Ignored characters whitespace and newline
    t_ignore = r' \t|\n'

    # Error handling
    def t_error(self, t):
        #display illegal character
        print(f"Illegal character: {t.value[0]}")
        # t.lexer.skip(1)
        
    #ignore tab and newline while doing analysis
    def t_IGNORE(self,t):
        r' \t|\n'
        pass
    
    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test the lexer
    def test(self, data):
        #input source code for analysis
        self.lexer.input(data)
        #get the tokens and info(type,vale) from lexer and process it 
        while True:
            token = self.lexer.token()
            if not token:
                break
            if token.type!="COMMENT": 
             self.tokensFound+=f'( {token.type},{token.value} )'
            else:
               self.tokensFound+=f'( {token.type}, ... )'
        #display all lexems
        print("["+self.tokensFound+"]")


