from pathlib import Path


class ReadingOrder:

    def generate(self, knowledge):

        order = []

        important_files = knowledge.get("important_files", [])
        source_files = knowledge.get("source_files", [])
        entry_point = knowledge.get("entry_point")

        # README
        if "README.md" in important_files:
            order.append({
                "file": "README.md",
                "reason": "Understand the project, installation and usage."
            })

        # Entry point
        if entry_point:
            order.append({
                "file": entry_point,
                "reason": "Application entry point."
            })

        # Important files
        for file in important_files:

            if file == "README.md":
                continue

            order.append({
                "file": file,
                "reason": "Important project file."
            })

        # Python source files
        for file in source_files:

            path = file["path"]

            if any(item["file"] == path for item in order):
                continue

            reason = "Python module."

            if file.get("classes"):
                reason = "Contains core classes."

            elif file.get("functions"):
                reason = "Contains reusable functions."

            order.append({
                "file": path,
                "reason": reason
            })

        return order