import re

STOP_WORDS = {
    "how",
    "does",
    "what",
    "where",
    "when",
    "why",
    "is",
    "are",
    "the",
    "a",
    "an",
    "of",
    "to",
    "in",
    "on",
    "for",
    "and",
    "or",
    "work",
    "works"
}


class Retriever:

    def __init__(self, code_index):
        self.code_index = code_index

    def retrieve(self, question, top_k=5):

        keywords = [
            word
            for word in re.findall(r"\w+", question.lower())
            if word not in STOP_WORDS
        ]

        scored = []

        for chunk in self.code_index.get_all_chunks():

            score = 0

            content = chunk["content"].lower()
            filename = chunk["file"].lower()

            for word in keywords:

                if word in filename:
                    score += 5

                score += content.count(word)

            if score > 0:
                scored.append((score, chunk))

        scored.sort(reverse=True, key=lambda x: x[0])

        return [chunk for _, chunk in scored[:top_k]]