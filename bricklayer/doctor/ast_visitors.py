import ast


class UserDefinedFunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        super(UserDefinedFunctionVisitor, self).__init__()
        self.functions = []

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)


class ImportedModuleVisitor(ast.NodeVisitor):
    def __init__(self):
        super(ImportedModuleVisitor, self).__init__()
        self.imports = []

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append((alias.name, None))

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.imports.append((alias.name, node.module))


class CalledFunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        super(CalledFunctionVisitor, self).__init__()
        self.functions = []

    def visit_Call(self, node):
        self.functions.append(node.func.id)
