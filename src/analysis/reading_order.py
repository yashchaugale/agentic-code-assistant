class ReadingOrder:

    def generate(self, knowledge):

        order = []

        # Always start with README
        if "README.md" in knowledge["important_files"]:
            order.append("README.md")

        # Entry point
        if knowledge["entry_point"]:
            order.append(knowledge["entry_point"])

        # Remaining important files
        for file in knowledge["important_files"]:

            if file not in order:
                order.append(file)

        # Other source files
        for file in knowledge["source_files"]:

            path = file["path"]

            if path not in order:
                order.append(path)

        return order