import http.server
import json

class HttpServer(http.server.BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        from socket_server.Server import Server

        try:
            data = json.loads(post_data.decode('utf-8'))

            method = data.get('method')
            print(method)
            params = data.get('params')
            print(params)

            if method == 'READ_TABLE_USER':
                response_data = Server().read_table_user(*params)
                
            elif method == 'CREATE_USER':
                response_data = Server().create_user(*params)
            else:
                response_data = {'status': 'error', 'message': 'Méthode non supportée'}

        except json.JSONDecodeError:
            response_data = {'status': 'error', 'message': 'Erreur de décodage JSON'}

        response_json = json.dumps(response_data).encode('utf-8')

        self._set_response()
        self.wfile.write(response_json)

