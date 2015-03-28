import falcon

import template
from parser import get_paragraphs


class BooksResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        paragraphs = get_paragraphs('/home/sanchopanca/Documents/thunder.txt')
        resp.body = template.render_template('book.html', paragraphs=paragraphs)


app = falcon.API()

books = BooksResource()

app.add_route('/books', books)