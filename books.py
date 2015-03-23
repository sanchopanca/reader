import falcon


def get_paragraphs(pathname):
    result = []
    with open(pathname) as f:
        for line in f.readlines():
            if line != '\n':
                result.append(line[:-1])
    return result


class BooksResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = open('/home/sanchopanca/Documents/thunder.txt').read()


app = falcon.API()

books = BooksResource()

app.add_route('/books', books)


if __name__ == '__main__':
    paragraphs = get_paragraphs('/home/sanchopanca/Documents/thunder.txt')
    print(paragraphs)