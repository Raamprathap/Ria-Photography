from Films.app import app as films_app
from gallery.app import gallery_app

def application(environ, start_response):
    path = environ.get('PATH_INFO', '')
    
    if path.startswith('/films'):
        environ['PATH_INFO'] = path[6:]  # Remove /films prefix
        return films_app(environ, start_response)
    elif path.startswith('/gallery'):
        environ['PATH_INFO'] = path[8:]  # Remove /gallery prefix
        return gallery_app(environ, start_response)
    else:
        # Serve static files
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']
