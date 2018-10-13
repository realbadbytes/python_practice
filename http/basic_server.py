# HTTPServer is a SocketServer.TCPServer subclass
# implements SocketServer.BaseServer interface
# creates and listens on HTTP socket, dispatches requests to handler

# create the server and initialize handler
def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', 80)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

# class HTTPServer is the bastion, dispatches to the following...
# class BaseHTTPRequestHandler is the request handler. (no shit!)
# HOWEVER, RequestHandler can't actually respond to HTTP requests (ok??)
# it needs to be subclassed to handle GET POST etc methods. i.e. do_GET()
# unforunately, this class' MessageClass defaults to mimetools.Message, which is deprecated.
# use SimpleHTTPServer to limit response to files in docroot




