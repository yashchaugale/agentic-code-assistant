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

        except Exception:
            return None

        try:
            tree = ast.parse(source)

        except Exception:
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

                classes.append(node.name)

            elif isinstance(node, ast.FunctionDef):

                functions.append(node.name)

        return {
            "path": str(path),
            "imports": sorted(set(imports)),
            "classes": classes,
            "functions": functions
        }