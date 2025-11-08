def extract_title(markdown):

    for line in markdown.splitlines():
        line = line.lstrip()
        if "# " in line:
            return line[2:].strip()
    return None