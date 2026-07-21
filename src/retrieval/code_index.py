class CodeIndex:

    def __init__(self):
        self.chunks = []

    def add_chunks(self, chunks):
        self.chunks.extend(chunks)

    def get_all_chunks(self):
        return self.chunks

    def clear(self):
        self.chunks.clear()