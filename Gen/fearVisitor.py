# Generated from G:/Progect/Compilator/Compile/grammar\fear.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .fearParser import fearParser
else:
    from fearParser import fearParser

# This class defines a complete generic visitor for a parse tree produced by fearParser.

class fearVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fearParser#program.
    def visitProgram(self, ctx:fearParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#function.
    def visitFunction(self, ctx:fearParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#functionHead.
    def visitFunctionHead(self, ctx:fearParser.FunctionHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#arg.
    def visitArg(self, ctx:fearParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#arguments.
    def visitArguments(self, ctx:fearParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#functionBody.
    def visitFunctionBody(self, ctx:fearParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#statement.
    def visitStatement(self, ctx:fearParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:fearParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#returnStatement.
    def visitReturnStatement(self, ctx:fearParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#whileStatement.
    def visitWhileStatement(self, ctx:fearParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#convert_type.
    def visitConvert_type(self, ctx:fearParser.Convert_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#moveValueVariable.
    def visitMoveValueVariable(self, ctx:fearParser.MoveValueVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#printStatement.
    def visitPrintStatement(self, ctx:fearParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#ifStatement.
    def visitIfStatement(self, ctx:fearParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#expressionAdd.
    def visitExpressionAdd(self, ctx:fearParser.ExpressionAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#expressionMul.
    def visitExpressionMul(self, ctx:fearParser.ExpressionMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#expressionNumber.
    def visitExpressionNumber(self, ctx:fearParser.ExpressionNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#expressionFunctionCall.
    def visitExpressionFunctionCall(self, ctx:fearParser.ExpressionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#expressionNested.
    def visitExpressionNested(self, ctx:fearParser.ExpressionNestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#expressionToType.
    def visitExpressionToType(self, ctx:fearParser.ExpressionToTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#expressionPow.
    def visitExpressionPow(self, ctx:fearParser.ExpressionPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#expressionString.
    def visitExpressionString(self, ctx:fearParser.ExpressionStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#equation.
    def visitEquation(self, ctx:fearParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#relop.
    def visitRelop(self, ctx:fearParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#param.
    def visitParam(self, ctx:fearParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#params.
    def visitParams(self, ctx:fearParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#functionCall.
    def visitFunctionCall(self, ctx:fearParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#atom.
    def visitAtom(self, ctx:fearParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fearParser#type.
    def visitType(self, ctx:fearParser.TypeContext):
        return self.visitChildren(ctx)



del fearParser