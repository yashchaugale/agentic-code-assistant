class RepositoryInsights:

    def analyze(self, data):

        strengths = []
        improvements = []

        files = data["files"]
        directories = data["directories"]

        # README
        if "README.md" in files:
            strengths.append("README documentation found.")
        else:
            improvements.append("Add a README.md file.")

        # License
        if any(f.startswith("LICENSE") for f in files):
            strengths.append("License file found.")
        else:
            improvements.append("Add a LICENSE file.")

        # Build File
        build_files = [
            "CMakeLists.txt",
            "package.json",
            "requirements.txt",
            "pom.xml",
            "Cargo.toml",
            "go.mod"
        ]

        if any(f in files for f in build_files):
            strengths.append("Build configuration detected.")
        else:
            improvements.append("No build configuration detected.")

        # Entry Point
        if data["entry_point"]:
            strengths.append(f"Entry point detected: {data['entry_point']}")
        else:
            improvements.append("Unable to determine entry point.")

        # Source Folder
        if "src" in directories:
            strengths.append("Source folder detected.")
        else:
            improvements.append("No src folder found.")

        # Tests
        if any("test" in f.lower() for f in files):
            strengths.append("Tests detected.")
        else:
            improvements.append("No tests detected.")

        return {
            "strengths": strengths,
            "improvements": improvements
        }