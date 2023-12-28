from Tokenizer import Tokenizer
from Parser import Parser

def main():
    tokens = [
        # 'INTCON', # integer constant
        # 'FLOATCON',# float constant
        # 'INT',
        # 'FLOAT',
        # 'IF',
        # 'ELSE',
        # 'EXIT',
        # 'WHILE',
        # 'READ',
        # 'WRITE',
        # 'RETURN',
        'STRING_LITRAL',
        # 'KEYWORD', # int|float|if|else|exit|while|read|write|return
        'IDENTIFIER', # any letter (letter | number)*
        # 'NUMBER',   # for numbers digit+ (.digit+)*
        'LOGICAL_LE', # <= 
        'LOGICAL_GE', # >=
        'LOGICAL_EET', # ==
        'LOGICAL_NE',  # !=
        'LOGICAL_AND', # &&
        'LOGICAL_OR', # ||
        'GREATER_THEN', # >
        'LESSER_THEN', # <
        'PLUS', # +
        'MINUS', # -
        'MULTIPLE', # *
        'DIVIDE', # %
        'SEMI_COLON', # ;
        'COMMA', # ,
        'LPAR', # )
        'RPAR', # (
        'LBRA', # {
        'RBRA', # }
        'COMMENT', # /* ... */,
        'NOT', # !
        'ASSIGNMENT',
        'LBK', # [
        'RBK', # ]
        'NUMBER',
        'EMPTY'
    ]
    # call tokenizer class which has lexer 
    lexical_analyzer=Tokenizer(tokens)
    #build lexer
    tokens=lexical_analyzer.get_tokens()
    lexer=lexical_analyzer.build()
    #open text file in read mode
    file_data = open("./input.txt", "r")
    #read source code file content
    source_code=file_data.read()
    #close file
    file_data.close()
    #pass the source_code and analyze it and display tokens in source code
    tokens_rec=lexical_analyzer.test(source_code)
    # initialize parser and build it to generate parse tree 
    # which uses shif reduce parser
    parser_build=Parser(tokens,source_code,lexer)
    # check wheather written program is correct or not
    parser_build.build_parser()   

main()