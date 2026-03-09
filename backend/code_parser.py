import ast
from nlp_model import nlp

def parse_and_comment(code: str) -> str:
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return f"# Syntax Error in supplied code: {e}\n" + code

    lines = code.split('\n')
    insertions = {}  # {line_number (0-indexed): [list of comment strings]}

    class CommentVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            start_line = node.lineno - 1
            # Handle decorators
            if node.decorator_list:
                start_line = node.decorator_list[0].lineno - 1
                
            end_line = getattr(node, 'end_lineno', start_line + 1)
            snippet = '\n'.join(lines[start_line:end_line])
            
            # Generate comment
            comment = nlp.generate_comment(snippet)
            insertions.setdefault(start_line, []).append(f"    # Function: {comment}")
            
            self.generic_visit(node)
            
        def visit_For(self, node):
            start_line = node.lineno - 1
            end_line = getattr(node, 'end_lineno', start_line + 1)
            snippet = '\n'.join(lines[start_line:end_line])
            
            comment = nlp.generate_comment(snippet)
            insertions.setdefault(start_line, []).append(f"    # Loop: {comment}")
            
            self.generic_visit(node)

        def visit_While(self, node):
            start_line = node.lineno - 1
            end_line = getattr(node, 'end_lineno', start_line + 1)
            snippet = '\n'.join(lines[start_line:end_line])
            
            comment = nlp.generate_comment(snippet)
            insertions.setdefault(start_line, []).append(f"    # While Loop: {comment}")
            
            self.generic_visit(node)

        def visit_If(self, node):
            start_line = node.lineno - 1
            end_line = getattr(node, 'end_lineno', start_line + 1)
            snippet = '\n'.join(lines[start_line:end_line])
            
            comment = nlp.generate_comment(snippet)
            insertions.setdefault(start_line, []).append(f"    # Condition: {comment}")
            
            self.generic_visit(node)

        def visit_Assign(self, node):
            start_line = node.lineno - 1
            # Extract variable names
            targets = []
            for t in node.targets:
                if isinstance(t, ast.Name):
                    targets.append(t.id)
                elif isinstance(t, ast.Tuple) or isinstance(t, ast.List):
                    for elt in t.elts:
                        if isinstance(elt, ast.Name):
                            targets.append(elt.id)
                            
            if targets:
                vars_str = ', '.join(targets)
                insertions.setdefault(start_line, []).append(f"    # Variable assignment: {vars_str}")
                
            self.generic_visit(node)

    visitor = CommentVisitor()
    visitor.visit(tree)

    # Reconstruct the code with inserted comments
    output_lines = []
    for i, line in enumerate(lines):
        if i in insertions:
            # Match the indentation of the original line
            indent = len(line) - len(line.lstrip())
            indent_str = ' ' * indent
            for c in insertions[i]:
                output_lines.append(indent_str + c.strip())
        output_lines.append(line)

    return '\n'.join(output_lines)
