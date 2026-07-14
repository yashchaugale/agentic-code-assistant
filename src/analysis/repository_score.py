class RepositoryScore:

    def calculate(self, data):

        score = 0

        files = data["files"]
        directories = data["directories"]

        # README
        if "README.md" in files:
            score += 15

        # License
        if any(f.startswith("LICENSE") for f in files):
            score += 10

        # Build System
        build_files = [
            "CMakeLists.txt",
            "package.json",
            "requirements.txt",
            "pom.xml",
            "Cargo.toml",
            "go.mod"
        ]

        if any(f in files for f in build_files):
            score += 15

        # Entry Point
        if data["entry_point"] is not None:
            score += 15

        # src folder
        if "src" in directories:
            score += 10

        # Tests
        if any(
            "test" in f.lower()
            for f in files
        ):
            score += 15

        # Repository Size
        if len(files) < 500:
            score += 10

        # Git Ignore
        if ".gitignore" in files:
            score += 10

        return score