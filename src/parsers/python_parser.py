import ast
from pathlib import Path


class PythonParser:

    def parse(self, file_path):

        path = Path(file_path)

        

        try:
            source = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            

        except Exception as e:
            
            return None

        try:
            tree = ast.parse(source)

            

        except Exception as e:
            
            return None

        imports = []
        classes = []
        functions = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:
                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    imports.append(node.module)

            elif isinstance(node, ast.ClassDef):

                method_names = []

                for item in node.body:

                    if isinstance(item, ast.FunctionDef):

                        method_names.append(item.name)

                classes.append({
                    "name": node.name,
                    "methods": method_names
                })

            elif isinstance(node, ast.FunctionDef):

                functions.append({
                    "name": node.name,
                    "start_line": node.lineno,
                    "end_line": node.end_lineno
                })

        return {
            "path": str(path),
            "imports": sorted(set(imports)),
            "classes": classes,
            "functions": functions
        }