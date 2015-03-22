import falcon


class BooksResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = open('/home/sanchopanca/Documents/thunder.txt').read()


app = falcon.API()

books = BooksResource()

app.add_route('/books', books)
