class QueryRouter:

    def route(self, question: str):

        q = question.lower()

        if "where is" in q:
            return "class_lookup"

        if "show all classes" in q:
            return "list_classes"

        if "show all functions" in q:
            return "list_functions"

        return "llm"