def extract_metrics(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()

    # Lines of Code
    loc = len(code.splitlines())

    # Complexity
    complexity = (
        code.count("if")
        + code.count("for")
        + code.count("while")
        + code.count("try")
        + code.count("except")
    )

    # Coupling
    coupling = (
        code.count("import")
        + code.count("from")
    )

    return {
        "loc": loc,
        "complexity": complexity,
        "coupling": coupling
    }