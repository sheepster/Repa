# Generated from G:/Progect/Compilator/Compile/grammar\fear.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,32,216,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,5,9,116,8,9,10,9,12,9,119,9,9,1,9,1,9,1,10,1,10,1,10,1,11,
        4,11,127,8,11,11,11,12,11,128,1,11,5,11,132,8,11,10,11,12,11,135,
        9,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,
        1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,23,
        1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,4,28,172,8,28,
        11,28,12,28,173,1,29,1,29,1,29,1,29,1,30,1,30,1,31,3,31,183,8,31,
        1,32,4,32,186,8,32,11,32,12,32,187,1,32,1,32,1,33,1,33,1,33,1,33,
        5,33,196,8,33,10,33,12,33,199,9,33,1,33,1,33,1,33,1,33,1,33,1,34,
        1,34,1,34,1,34,5,34,210,8,34,10,34,12,34,213,9,34,1,34,1,34,1,197,
        0,35,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,0,23,11,25,
        12,27,13,29,14,31,15,33,16,35,17,37,18,39,19,41,20,43,21,45,22,47,
        23,49,24,51,25,53,26,55,27,57,28,59,29,61,0,63,0,65,30,67,31,69,
        32,1,0,5,2,0,34,34,92,92,2,0,65,90,97,122,1,0,48,57,3,0,9,10,13,
        13,32,32,2,0,10,10,13,13,221,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,
        29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,
        39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,
        49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,
        59,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,1,71,1,0,0,0,3,
        73,1,0,0,0,5,80,1,0,0,0,7,83,1,0,0,0,9,86,1,0,0,0,11,92,1,0,0,0,
        13,95,1,0,0,0,15,99,1,0,0,0,17,106,1,0,0,0,19,112,1,0,0,0,21,122,
        1,0,0,0,23,126,1,0,0,0,25,136,1,0,0,0,27,138,1,0,0,0,29,140,1,0,
        0,0,31,142,1,0,0,0,33,144,1,0,0,0,35,146,1,0,0,0,37,148,1,0,0,0,
        39,150,1,0,0,0,41,152,1,0,0,0,43,154,1,0,0,0,45,157,1,0,0,0,47,160,
        1,0,0,0,49,162,1,0,0,0,51,164,1,0,0,0,53,166,1,0,0,0,55,168,1,0,
        0,0,57,171,1,0,0,0,59,175,1,0,0,0,61,179,1,0,0,0,63,182,1,0,0,0,
        65,185,1,0,0,0,67,191,1,0,0,0,69,205,1,0,0,0,71,72,5,44,0,0,72,2,
        1,0,0,0,73,74,5,114,0,0,74,75,5,101,0,0,75,76,5,116,0,0,76,77,5,
        117,0,0,77,78,5,114,0,0,78,79,5,110,0,0,79,4,1,0,0,0,80,81,5,60,
        0,0,81,82,5,60,0,0,82,6,1,0,0,0,83,84,5,62,0,0,84,85,5,62,0,0,85,
        8,1,0,0,0,86,87,5,112,0,0,87,88,5,114,0,0,88,89,5,105,0,0,89,90,
        5,110,0,0,90,91,5,116,0,0,91,10,1,0,0,0,92,93,5,105,0,0,93,94,5,
        102,0,0,94,12,1,0,0,0,95,96,5,105,0,0,96,97,5,110,0,0,97,98,5,116,
        0,0,98,14,1,0,0,0,99,100,5,100,0,0,100,101,5,111,0,0,101,102,5,117,
        0,0,102,103,5,98,0,0,103,104,5,108,0,0,104,105,5,101,0,0,105,16,
        1,0,0,0,106,107,5,119,0,0,107,108,5,104,0,0,108,109,5,105,0,0,109,
        110,5,108,0,0,110,111,5,101,0,0,111,18,1,0,0,0,112,117,5,34,0,0,
        113,116,3,21,10,0,114,116,8,0,0,0,115,113,1,0,0,0,115,114,1,0,0,
        0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,1,0,0,
        0,119,117,1,0,0,0,120,121,5,34,0,0,121,20,1,0,0,0,122,123,5,92,0,
        0,123,124,9,0,0,0,124,22,1,0,0,0,125,127,7,1,0,0,126,125,1,0,0,0,
        127,128,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,133,1,0,0,0,
        130,132,3,61,30,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,
        0,133,134,1,0,0,0,134,24,1,0,0,0,135,133,1,0,0,0,136,137,5,42,0,
        0,137,26,1,0,0,0,138,139,5,37,0,0,139,28,1,0,0,0,140,141,5,47,0,
        0,141,30,1,0,0,0,142,143,5,43,0,0,143,32,1,0,0,0,144,145,5,45,0,
        0,145,34,1,0,0,0,146,147,5,40,0,0,147,36,1,0,0,0,148,149,5,41,0,
        0,149,38,1,0,0,0,150,151,5,94,0,0,151,40,1,0,0,0,152,153,5,61,0,
        0,153,42,1,0,0,0,154,155,5,61,0,0,155,156,5,61,0,0,156,44,1,0,0,
        0,157,158,5,33,0,0,158,159,5,61,0,0,159,46,1,0,0,0,160,161,5,123,
        0,0,161,48,1,0,0,0,162,163,5,125,0,0,163,50,1,0,0,0,164,165,5,59,
        0,0,165,52,1,0,0,0,166,167,5,62,0,0,167,54,1,0,0,0,168,169,5,60,
        0,0,169,56,1,0,0,0,170,172,3,61,30,0,171,170,1,0,0,0,172,173,1,0,
        0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,58,1,0,0,0,175,176,3,57,
        28,0,176,177,5,46,0,0,177,178,3,57,28,0,178,60,1,0,0,0,179,180,7,
        2,0,0,180,62,1,0,0,0,181,183,3,33,16,0,182,181,1,0,0,0,182,183,1,
        0,0,0,183,64,1,0,0,0,184,186,7,3,0,0,185,184,1,0,0,0,186,187,1,0,
        0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,190,6,32,
        0,0,190,66,1,0,0,0,191,192,5,47,0,0,192,193,5,42,0,0,193,197,1,0,
        0,0,194,196,9,0,0,0,195,194,1,0,0,0,196,199,1,0,0,0,197,198,1,0,
        0,0,197,195,1,0,0,0,198,200,1,0,0,0,199,197,1,0,0,0,200,201,5,42,
        0,0,201,202,5,47,0,0,202,203,1,0,0,0,203,204,6,33,0,0,204,68,1,0,
        0,0,205,206,5,47,0,0,206,207,5,47,0,0,207,211,1,0,0,0,208,210,8,
        4,0,0,209,208,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,
        0,0,0,212,214,1,0,0,0,213,211,1,0,0,0,214,215,6,34,0,0,215,70,1,
        0,0,0,10,0,115,117,128,133,173,182,187,197,211,1,6,0,0
    ]

class fearLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    WHILE = 9
    STRING = 10
    ID = 11
    TIMES = 12
    REM = 13
    DIV = 14
    PLUS = 15
    MINUS = 16
    LPAREN = 17
    RPAREN = 18
    POW = 19
    EQ = 20
    EQ_EQ = 21
    NOT_EQ = 22
    LBRACE = 23
    RBRACE = 24
    END_STATE = 25
    GT = 26
    LT = 27
    INT = 28
    DECIMAL = 29
    WS = 30
    COMMENT = 31
    LINE_COMMENT = 32

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'return'", "'<<'", "'>>'", "'print'", "'if'", "'int'", 
            "'double'", "'while'", "'*'", "'%'", "'/'", "'+'", "'-'", "'('", 
            "')'", "'^'", "'='", "'=='", "'!='", "'{'", "'}'", "';'", "'>'", 
            "'<'" ]

    symbolicNames = [ "<INVALID>",
            "WHILE", "STRING", "ID", "TIMES", "REM", "DIV", "PLUS", "MINUS", 
            "LPAREN", "RPAREN", "POW", "EQ", "EQ_EQ", "NOT_EQ", "LBRACE", 
            "RBRACE", "END_STATE", "GT", "LT", "INT", "DECIMAL", "WS", "COMMENT", 
            "LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "WHILE", "STRING", "ESC", "ID", "TIMES", "REM", 
                  "DIV", "PLUS", "MINUS", "LPAREN", "RPAREN", "POW", "EQ", 
                  "EQ_EQ", "NOT_EQ", "LBRACE", "RBRACE", "END_STATE", "GT", 
                  "LT", "INT", "DECIMAL", "DIGIT", "SIGN", "WS", "COMMENT", 
                  "LINE_COMMENT" ]

    grammarFileName = "fear.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

