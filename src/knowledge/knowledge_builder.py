from llm import summarize_file


class KnowledgeBuilder:

    def summarize_module(
        self,
        file_content
    ):

        return summarize_file(file_content)