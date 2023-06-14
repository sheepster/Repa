from llvmlite import ir
from Gen.fearParser import fearParser
from codegen.AST import MainAST


class CoolFunc:

    @staticmethod
    def get_type(my_type: fearParser.TypeContext):
        value = my_type.getText()

        if value == "int":
            return ir.IntType(32)
        elif value == "double":
            return ir.DoubleType()
        else:
            raise Exception("Unknown type: " + value)

    @staticmethod
    def check_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
