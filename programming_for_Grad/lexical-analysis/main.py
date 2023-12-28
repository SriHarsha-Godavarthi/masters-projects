from Tokenizer import Tokenizer


def main():
    # call tokenizer class which has lexer 
    lexical_analyzer=Tokenizer()
    #build lexer
    lexical_analyzer.build()
    #open text file in read mode
    file_data = open("./input.txt", "r")
    #read source code file content
    source_code=file_data.read()
    #close file
    file_data.close()
    #pass the source_code and analyze it and display tokens in source code
    lexical_analyzer.test(source_code)
main()