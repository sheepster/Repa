import os
import sys
import time

import llvmlite.binding as llvm
from antlr4 import *
from Gen.fearLexer import fearLexer
from Gen.fearParser import fearParser
from codegen.fearListener import FearlessListener
from codegen.Optimization import Optimization
from codegen.ErrorListener import MyErrorListener


class Compiler:
    def __init__(self, input_file):
        self.input_file = FileStream(input_file)
        print(input_file)
        self.lexer = fearLexer(self.input_file)
        self.stream = CommonTokenStream(self.lexer)

        self.parser = fearParser(self.stream)
        self.parser.removeErrorListeners()
        self.errorListener = MyErrorListener()
        self.parser.addErrorListener(self.errorListener)

        self.tree = self.parser.program()

        if not self.errorListener.check:
            printer = FearlessListener()
            walker = ParseTreeWalker()
            walker.walk(printer, self.tree)

            self.compile(printer)

    def compile(self, gen_module):
        module_ref = llvm.parse_assembly(str(gen_module.module))
        module_ref.verify()

        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine(codemodel="small")

        gen_module.module.triple = llvm.get_default_triple()
        gen_module.module.data_layout = target_machine.target_data

        print(str(gen_module.module))
        check = input("you want to optimize this code [Y/N]: ").lower()
        if check == "y":
            print("---Optimization is enable----")
            Optimization(module_ref)
            print(module_ref)
        elif check == "n":
            print("---Optimization is disable----")
        print(f"{'Assembler':=^70}")
        asm = target_machine.emit_assembly(module_ref)
        print(asm)
        open('fear.s','w').write(asm)

        obj = target_machine.emit_object(module_ref)
        open('fear.o', 'wb').write(obj)
        # open('codegen/fear.str', 'w').write(str(module_ref))
        print("=" * 25, "execute", "=" * 25)
        os.system(f"clang fear.o -o fear.exe")

        start_time = time.time()
        os.system("fear.exe")
        end_time = time.time()

        print("=" * 27, "end", "=" * 27)
        print('Program fear - Execution time:', (end_time - start_time) * 1000, 'milliseconds')




if __name__ == '__main__':
    Compiler = Compiler("./test.fear")
