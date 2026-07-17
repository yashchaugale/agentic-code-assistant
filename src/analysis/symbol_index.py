from collections import defaultdict


class SymbolIndex:

    def build(self, knowledge):

        class_index = {}
        function_index = defaultdict(list)

        for file in knowledge.get("source_files", []):

            path = file["path"]

            # Index classes
            for cls in file.get("classes", []):
                class_index[cls] = path

            # Index functions
            for func in file.get("functions", []):
                function_index[func].append(path)

        return {
            "classes": class_index,
            "functions": dict(function_index)
        }