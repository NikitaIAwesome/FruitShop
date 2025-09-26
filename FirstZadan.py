from http.server import HTTPServer, BaseHTTPRequestHandler

products = [
    ['Yabloko', '50', '🍎'],
    ['Apelsin', '70', '🍊'],
    ['Pomidor', '60', '🍅'],
    ['Ogurec', '40', '🥒'],
    ['Malina', '120', '🍓']
]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        if self.path == '/':
            html = '<h1>Produkty</h1>'
            for i, product in enumerate(products):
                html += f'<div><a href="/{i}">{product[2]} {product[0]}</a></div>'
        else:
            i = int(self.path[1:])
            product = products[i]
            html = f'<h1>{product[2]} {product[0]}</h1>'
            html += f'<p>Cena: {product[1]} rub.</p>' 
        self.wfile.write(html.encode('utf-8'))

HTTPServer(('', 8000), Handler).serve_forever()