# import yacc to do the parsing which generates ast tree
import ply.yacc as yacc

# abstract syntax treeNode
class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children if children is not None else []
        self.value = value
        
class Parser:

    def __init__(self,tokens,source_code,lexer):
        #store tokens,code to execute,build lexer
        self.tokens=tokens
        #get lexer output
        self.lexer=lexer.input(source_code)
        self.input=source_code
        self.parser=yacc
        self.AstLevels={}
        # give precedence for operators
        self.precedence = (
            ('left', 'LOGICAL_EET', 'LOGICAL_NE', 'LOGICAL_LE', 'LESSER_THEN', 'LOGICAL_GE', 'GREATER_THEN'),
            ('left', 'PLUS', 'MINUS'),
            ('left', 'MULTIPLE', 'DIVIDE'),
            ('right', 'NOT'),
        )

    # define context free grammar using p_{rulename} i.e.(ruleName - non terminal, tokens - terminals)
    def p_Program(self,p):
        '''Program : DeclList Procedures
                   | Procedures'''
        # create node in AST tree after each production based on the string encountered
        if len(p) == 3:
            p[0] = ASTNode("Program", [p[1], p[2]])
        else:
            p[0] = ASTNode("Program", [p[1]])
                   
    def p_Procedures(self,p):
        '''Procedures : ProcedureDecl Procedures
		              | ProcedureDecl'''
        if len(p) == 3:
            p[0] = ASTNode("Procedures", [p[1], p[2]])
        else:
            p[0] = ASTNode("Procedures", [p[1]])

    def p_ProcedureDecl(self,p): 
        '''ProcedureDecl : ProcedureHead ProcedureBody'''
        p[0] = ASTNode("ProcedureDecl", [p[1], p[2]])

    def p_ProcedureHead(self,p):
        '''ProcedureHead : FunctionDecl DeclList 
                         | FunctionDecl'''
        if len(p) == 3:
            p[0] = ASTNode("ProcedureHead", [p[1], p[2]])
        else:
            p[0] = ASTNode("ProcedureHead", [p[1]])

    def p_FunctionDecl(self,p):
        '''FunctionDecl : Type IDENTIFIER LPAR RPAR LBRA'''
        
        p[0] = ASTNode("FunctionDecl", [p[1], ASTNode('IDENTIFIER',value=p[2]),ASTNode('LPAR',value=p[3]),ASTNode('RPAR',value=p[4]),ASTNode('LBAR',value=p[5])])
        

    def p_ProcedureBody(self,p):
        '''ProcedureBody : StatementList RBRA'''
        p[0] = ASTNode("ProcedureBody", [p[1], ASTNode('RBRA',value=p[2])])

    def p_DeclList(self,p):
        '''DeclList : Type IdentifierList SEMI_COLON
                    |  DeclList Type IdentifierList SEMI_COLON'''
        if len(p) == 4:
            p[0] = ASTNode("DeclList", [p[1], p[2],ASTNode('SEMI_COLON',value=p[3])])
        else:
            p[0] = ASTNode("DeclList", [p[1], p[2],p[3],ASTNode('SEMI_COLON',value=p[4])])
            
    def p_Type(self,p):
        '''Type : INT 
                | FLOAT'''
        p[0]=ASTNode('Type',value=p[1])
                
    def p_IdentifierList(self,p):
        '''IdentifierList : VarDecl
                          | IdentifierList COMMA VarDecl'''
        if len(p) == 4:
            p[0] = ASTNode("IdentifierList", [p[1], ASTNode('COMMA',value=p[2]),p[3]])
        else:
            p[0] = ASTNode("IdentifierList", [p[1]])

    def p_VarDecl(self,p):
        '''VarDecl : IDENTIFIER
                   | IDENTIFIER LBK NUMBER RBK''' 
        if len(p) == 5:
            p[0] = ASTNode("VarDecl", [ASTNode('IDENTIFIER',value=p[1]), ASTNode('LBK',value=p[2]),ASTNode('Constant',value=p[3]),ASTNode('RBK',value=p[4])])
        else:
            p[0] = ASTNode("VarDecl", [ASTNode('IDENTIFIER',value=p[1])])           
    
    def p_StatementList(self,p):
        '''StatementList : Statement 
    		             | StatementList Statement''' 
        if len(p) == 3:
            p[0] = ASTNode("StatementList", [p[1], p[2]])
        else:
            p[0] = ASTNode("StatementList", [p[1]])  

    def p_Statement(self,p):
        '''Statement : Assignment 
    	             | IfStatement
    	             | WhileStatement 
    	             | IOStatement
    	             | ReturnStatement 
    	             | ExitStatement
    	             | CompoundStatement'''
        p[0]=ASTNode('Statement',[p[1]])

    def p_Assignment(self,p):
        '''Assignment : Variable ASSIGNMENT Expr SEMI_COLON'''
        p[0] = ASTNode("Assignment", [p[1], ASTNode('ASSIGNMENT',value=p[2]),p[3],ASTNode('SEMI_COLON',value=p[4])])

    def p_IfStatement(self,p):
        '''IfStatement : IF TestAndThen ELSE CompoundStatement 
                    | IF TestAndThen'''
        if len(p) == 5:
            p[0] = ASTNode("IfStatement", [ASTNode('IF',value=p[1]), p[2],ASTNode('ELSE',value=p[3]), p[4]])
        else:
            p[0] = ASTNode("IfStatement", [ASTNode('IF',value=p[1]),p[2]])  

    def p_TestAndThen(self,p):
        '''TestAndThen : Test CompoundStatement''' 
        p[0]=ASTNode('TestAndThen',[p[1],p[2]])

    def p_Test(self,p):
        '''Test : LPAR Expr RPAR''' 
        p[0]=ASTNode('Test',[ASTNode('LPAR',value=p[1]),p[2],ASTNode('RPAR',value=p[3])])

    def p_WhileStatement(self,p):
        '''WhileStatement : WhileToken WhileExpr Statement''' 
        p[0]=ASTNode('WhileStatement',[p[1],p[2],p[3]])

    def p_WhileToken(self,p):
        '''WhileToken : WHILE''' 
        p[0]=ASTNode('WhileToken',[ASTNode('WHILE',value=p[1])])

    def p_WhileExpr(self,p):
        '''WhileExpr : LPAR Expr RPAR''' 
        p[0]=ASTNode('WhileExpr',[ASTNode('LPAR',value=p[1]),p[2],ASTNode('RPAR',value=p[3])])

    def p_IOStatement(self,p):
        '''IOStatement : READ LPAR Variable RPAR SEMI_COLON 
                    | WRITE LPAR Expr RPAR SEMI_COLON 
                    | WRITE LPAR StringConstant RPAR SEMI_COLON'''
        if p[1]=='read':
           p[0]=ASTNode('IOStatement',[ASTNode('READ',value=p[1]),ASTNode('LPAR',value=p[2]),p[3],ASTNode('RPAR',value=[4]),ASTNode('SEMI_COLON',value=[5])])
        else:
            p[0]=ASTNode('IOStatement',[ASTNode('WRITE',value=p[1]),ASTNode('LPAR',value=p[2]),p[3],ASTNode('RPAR',value=[4]),ASTNode('SEMI_COLON',value=[5])])

    def p_ReturnStatement(self,p):
        '''ReturnStatement : RETURN Expr SEMI_COLON''' 
        p[0]=ASTNode('ReturnStatement',[ASTNode('RETURN',value=p[1]),p[2],ASTNode('SEMI_COLON',value=p[3])])

    def p_ExitStatement(self,p):
        '''ExitStatement : EXIT SEMI_COLON'''
        p[0]=ASTNode('ExitStatement',[ASTNode('EXIT',value=p[1]),ASTNode('SEMI_COLON',value=p[2])])

    def p_CompoundStatement(self,p):
        '''CompoundStatement : LBRA StatementList RBRA'''
        p[0]=ASTNode('CompoundStatement',[ASTNode('LBRA',value=p[1]),p[2],ASTNode('RBRA',value=p[3])])
    
    def p_Expr(self,p):
        '''Expr : Expr LOGICAL_AND SimpleExpr 
                | Expr LOGICAL_OR SimpleExpr 
                | SimpleExpr 
                | NOT SimpleExpr''' 
        if len(p)==2:
            p[0]=ASTNode(p[0],[p[1]])
        elif len(p)==3:
            p[0]=ASTNode(p[0],[p[1],p[2]])
        else:
            p[0]=ASTNode(p[0],[p[1],p[2],p[3]])
            

    def p_SimpleExpr(self,p):
        '''SimpleExpr : SimpleExpr LOGICAL_EET AddExpr 
                    | SimpleExpr LOGICAL_NE AddExpr 
                    | SimpleExpr LOGICAL_LE AddExpr 
                    | SimpleExpr LESSER_THEN AddExpr 
                    | SimpleExpr LOGICAL_GE AddExpr 
                    | SimpleExpr GREATER_THEN AddExpr 
                    | AddExpr''' 
        if len(p)==2:
            p[0]=ASTNode(p[0],[p[1]])
        elif p[2]=="==":
            p[0]=ASTNode(p[0],[p[1],ASTNode('LOGICAL_EET',value=p[2]),p[3]])
        elif p[2]=="!=":
            p[0]=ASTNode(p[0],[p[1],ASTNode('LOGICAL_NE',value=p[2]),p[3]])
        elif p[2]=="<=":
            p[0]=ASTNode(p[0],[p[1],ASTNode('LOGICAL_LE',value=p[2]),p[3]])
        elif p[2]=="<":
            p[0]=ASTNode(p[0],[p[1],ASTNode('LESSER_THEN',value=p[2]),p[3]])
        elif p[2]==">=":
            p[0]=ASTNode(p[0],[p[1],ASTNode('LOGICAL_GE',value=p[2]),p[3]])
        elif p[2]==">":
            p[0]=ASTNode(p[0],[p[1],ASTNode('GREATER_THEN',value=p[2]),p[3]])
            
    def p_AddExpr(self,p):
        '''AddExpr : AddExpr PLUS MulExpr 
                | AddExpr MINUS MulExpr 
                | MulExpr''' 
        if len(p)==2:
            p[0]=ASTNode(p[0],[p[1]])
        elif p[2]=='-':
            p[0]=ASTNode(p[0],[p[1],ASTNode('MINUS',value=p[2]),p[3]])
        elif p[2]=='+':
            p[0]=ASTNode(p[0],[p[1],ASTNode('PLUS',value=p[2]),p[3]])

    def p_MulExpr(self,p):
        '''MulExpr : MulExpr MULTIPLE Factor 
                | MulExpr DIVIDE Factor 
                | Factor'''
        if len(p)==2:
            p[0]=ASTNode(p[0],[p[1]])
        elif p[2]=="*":
            p[0]=ASTNode(p[0],[p[1],ASTNode('MULTIPLE',value=p[2]),p[3]])
        else:
            p[0]=ASTNode(p[0],[p[1],ASTNode('DIVIDE',value=p[2]),p[3]])

    def p_Factor(self,p):
        '''Factor : Variable 
            | Constant 
            | IDENTIFIER LPAR RPAR 
            | LPAR Expr RPAR''' 
        if len(p)==2:
            p[0]=ASTNode('Factor',[p[1]])
        elif p[2]=='(':
            p[0]=ASTNode('Factor',[ASTNode('IDENTIFIER',value=p[1]),ASTNode('LPAR',value=p[2]),ASTNode('RPAR',value=p[3])])             
        else:
            p[0]=ASTNode('Factor',[ASTNode('LPAR',value=p[1]),p[2],ASTNode('RPAR',value=p[3])]) 

    def p_Variable(self,p):
        '''Variable : IDENTIFIER 
                    | IDENTIFIER LBK Expr RBK'''
        if len(p)==2:
            p[0]=ASTNode('Variable',[ASTNode('IDENTIFIER',value=p[1])])
        else:
            p[0]=ASTNode('Variable',[ASTNode('IDENTIFIER',value=p[1]),ASTNode('LBK',value=p[2]),p[3],ASTNode('RBK',value=p[4])])

    def p_StringConstant(self,p):
        '''StringConstant : STRING_LITRAL''' 
        p[0]=ASTNode('StringConstant',[ASTNode('STRING_LITRAL',value=p[1])])

    def p_Constant(self,p):
        '''Constant : NUMBER'''
        p[0]=ASTNode('Constant',[ASTNode('NUMBER',value=p[1])])
    # Empty production
    def p_empty(self,p):
        '''empty : EMPTY'''
        p[0]=ASTNode('empty',value=p[1])
        
    def p_error(self,p):
     print(p)
        # print if any error occurs
     print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token {p.value}")
    
    def print_ast(self, node, level):
            # print(node)
            if node is not None:
                # print(node.value)
                if  node.type is not None:
                    if level not in self.AstLevels:
                        # If not, initialize it with an empty string
                        self.AstLevels[level] = node.type
                    else:
                        self.AstLevels[level] = self.AstLevels[level] + " " + node.type 
                for child in node.children:
                    self.print_ast(child, level + 1)
                            
    def build_parser(self):
        tokens=self.tokens
        try:
            # for debugging add debug=True,
            self.parser.yacc(module=self, start='Program',debug=True)
            #get parser tree from parser
            parse_tree=self.parser.parse(self.input,lexer=self.lexer,debug=True)
            #print AST tree
            self.print_ast(parse_tree, 0)
            #dictonary
            print("AST PARSE TREE:")
            for item in sorted(list(self.AstLevels.keys())):
                print(f"level {item}: ",self.AstLevels[item])
            # print("print AST levels for each shift and reduce \n",type(parse_tree))
        except Exception as e:
            print(f"An unexpected error occurred: {e}")