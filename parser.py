def get_paragraphs(pathname: str) -> list:
    result = []
    with open(pathname) as f:
        for line in f.readlines():
            if line != '\n':
                result.append(line[:-1])
    return result