from collections import defaultdict


class SymbolIndex:

    def build(self, knowledge):

        class_index = {}
        function_index = defaultdict(list)

        for file in knowledge.get("source_files", []):

            path = file["path"]

            print("=" * 50)
            print("FILE:", path)
            print("FUNCTIONS:", file.get("functions"))

            # Index classes
            for cls in file.get("classes", []):
                class_index[cls["name"]] = path

            # Index functions
            for func in file.get("functions", []):

                if isinstance(func, str):
                    print("❌ FOUND STRING FUNCTION!")
                    return

                function_index[func["name"]].append(path)

        return {
            "classes": class_index,
            "functions": dict(function_index)
        }