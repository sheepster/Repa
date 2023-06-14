# Generated from G:/Progect/Compilator/Compile/grammar\fear.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fearParser import fearParser
else:
    from fearParser import fearParser

# This class defines a complete listener for a parse tree produced by fearParser.
class fearListener(ParseTreeListener):

    # Enter a parse tree produced by fearParser#program.
    def enterProgram(self, ctx:fearParser.ProgramContext):
        pass

    # Exit a parse tree produced by fearParser#program.
    def exitProgram(self, ctx:fearParser.ProgramContext):
        pass


    # Enter a parse tree produced by fearParser#function.
    def enterFunction(self, ctx:fearParser.FunctionContext):
        pass

    # Exit a parse tree produced by fearParser#function.
    def exitFunction(self, ctx:fearParser.FunctionContext):
        pass


    # Enter a parse tree produced by fearParser#functionHead.
    def enterFunctionHead(self, ctx:fearParser.FunctionHeadContext):
        pass

    # Exit a parse tree produced by fearParser#functionHead.
    def exitFunctionHead(self, ctx:fearParser.FunctionHeadContext):
        pass


    # Enter a parse tree produced by fearParser#arg.
    def enterArg(self, ctx:fearParser.ArgContext):
        pass

    # Exit a parse tree produced by fearParser#arg.
    def exitArg(self, ctx:fearParser.ArgContext):
        pass


    # Enter a parse tree produced by fearParser#arguments.
    def enterArguments(self, ctx:fearParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by fearParser#arguments.
    def exitArguments(self, ctx:fearParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by fearParser#functionBody.
    def enterFunctionBody(self, ctx:fearParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by fearParser#functionBody.
    def exitFunctionBody(self, ctx:fearParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by fearParser#statement.
    def enterStatement(self, ctx:fearParser.StatementContext):
        pass

    # Exit a parse tree produced by fearParser#statement.
    def exitStatement(self, ctx:fearParser.StatementContext):
        pass


    # Enter a parse tree produced by fearParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:fearParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by fearParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:fearParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by fearParser#returnStatement.
    def enterReturnStatement(self, ctx:fearParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by fearParser#returnStatement.
    def exitReturnStatement(self, ctx:fearParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by fearParser#whileStatement.
    def enterWhileStatement(self, ctx:fearParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by fearParser#whileStatement.
    def exitWhileStatement(self, ctx:fearParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by fearParser#convert_type.
    def enterConvert_type(self, ctx:fearParser.Convert_typeContext):
        pass

    # Exit a parse tree produced by fearParser#convert_type.
    def exitConvert_type(self, ctx:fearParser.Convert_typeContext):
        pass


    # Enter a parse tree produced by fearParser#moveValueVariable.
    def enterMoveValueVariable(self, ctx:fearParser.MoveValueVariableContext):
        pass

    # Exit a parse tree produced by fearParser#moveValueVariable.
    def exitMoveValueVariable(self, ctx:fearParser.MoveValueVariableContext):
        pass


    # Enter a parse tree produced by fearParser#printStatement.
    def enterPrintStatement(self, ctx:fearParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by fearParser#printStatement.
    def exitPrintStatement(self, ctx:fearParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by fearParser#ifStatement.
    def enterIfStatement(self, ctx:fearParser.IfStatementContext):
        pass

    # Exit a parse tree produced by fearParser#ifStatement.
    def exitIfStatement(self, ctx:fearParser.IfStatementContext):
        pass


    # Enter a parse tree produced by fearParser#expressionAdd.
    def enterExpressionAdd(self, ctx:fearParser.ExpressionAddContext):
        pass

    # Exit a parse tree produced by fearParser#expressionAdd.
    def exitExpressionAdd(self, ctx:fearParser.ExpressionAddContext):
        pass


    # Enter a parse tree produced by fearParser#expressionMul.
    def enterExpressionMul(self, ctx:fearParser.ExpressionMulContext):
        pass

    # Exit a parse tree produced by fearParser#expressionMul.
    def exitExpressionMul(self, ctx:fearParser.ExpressionMulContext):
        pass


    # Enter a parse tree produced by fearParser#expressionNumber.
    def enterExpressionNumber(self, ctx:fearParser.ExpressionNumberContext):
        pass

    # Exit a parse tree produced by fearParser#expressionNumber.
    def exitExpressionNumber(self, ctx:fearParser.ExpressionNumberContext):
        pass


    # Enter a parse tree produced by fearParser#expressionFunctionCall.
    def enterExpressionFunctionCall(self, ctx:fearParser.ExpressionFunctionCallContext):
        pass

    # Exit a parse tree produced by fearParser#expressionFunctionCall.
    def exitExpressionFunctionCall(self, ctx:fearParser.ExpressionFunctionCallContext):
        pass


    # Enter a parse tree produced by fearParser#expressionNested.
    def enterExpressionNested(self, ctx:fearParser.ExpressionNestedContext):
        pass

    # Exit a parse tree produced by fearParser#expressionNested.
    def exitExpressionNested(self, ctx:fearParser.ExpressionNestedContext):
        pass


    # Enter a parse tree produced by fearParser#expressionToType.
    def enterExpressionToType(self, ctx:fearParser.ExpressionToTypeContext):
        pass

    # Exit a parse tree produced by fearParser#expressionToType.
    def exitExpressionToType(self, ctx:fearParser.ExpressionToTypeContext):
        pass


    # Enter a parse tree produced by fearParser#expressionPow.
    def enterExpressionPow(self, ctx:fearParser.ExpressionPowContext):
        pass

    # Exit a parse tree produced by fearParser#expressionPow.
    def exitExpressionPow(self, ctx:fearParser.ExpressionPowContext):
        pass


    # Enter a parse tree produced by fearParser#expressionString.
    def enterExpressionString(self, ctx:fearParser.ExpressionStringContext):
        pass

    # Exit a parse tree produced by fearParser#expressionString.
    def exitExpressionString(self, ctx:fearParser.ExpressionStringContext):
        pass


    # Enter a parse tree produced by fearParser#equation.
    def enterEquation(self, ctx:fearParser.EquationContext):
        pass

    # Exit a parse tree produced by fearParser#equation.
    def exitEquation(self, ctx:fearParser.EquationContext):
        pass


    # Enter a parse tree produced by fearParser#relop.
    def enterRelop(self, ctx:fearParser.RelopContext):
        pass

    # Exit a parse tree produced by fearParser#relop.
    def exitRelop(self, ctx:fearParser.RelopContext):
        pass


    # Enter a parse tree produced by fearParser#param.
    def enterParam(self, ctx:fearParser.ParamContext):
        pass

    # Exit a parse tree produced by fearParser#param.
    def exitParam(self, ctx:fearParser.ParamContext):
        pass


    # Enter a parse tree produced by fearParser#params.
    def enterParams(self, ctx:fearParser.ParamsContext):
        pass

    # Exit a parse tree produced by fearParser#params.
    def exitParams(self, ctx:fearParser.ParamsContext):
        pass


    # Enter a parse tree produced by fearParser#functionCall.
    def enterFunctionCall(self, ctx:fearParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by fearParser#functionCall.
    def exitFunctionCall(self, ctx:fearParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by fearParser#atom.
    def enterAtom(self, ctx:fearParser.AtomContext):
        pass

    # Exit a parse tree produced by fearParser#atom.
    def exitAtom(self, ctx:fearParser.AtomContext):
        pass


    # Enter a parse tree produced by fearParser#type.
    def enterType(self, ctx:fearParser.TypeContext):
        pass

    # Exit a parse tree produced by fearParser#type.
    def exitType(self, ctx:fearParser.TypeContext):
        pass



del fearParser