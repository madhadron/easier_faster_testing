from unittest.mock import patch, call
import unittest
import http.server
from threading import Thread
import fetch

class TestHandler(http.server.BaseHTTPRequestHandler):
    calls = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if TestHandler.calls < 2:
            self.send_response(500, 'ERROR')
            self.end_headers()
        else:
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Test')
        TestHandler.calls += 1

class TestFetch(unittest.TestCase):
    @patch('time.sleep')
    def test_fetch(self, mock_sleep):
        # Start an HTTP server to query
        PORT = 9095
        httpd = http.server.HTTPServer(("127.0.0.1", PORT), TestHandler)
        def serve():
            httpd.serve_forever(0.1)
        t = Thread(target=serve)
        t.start()

        # Try fetching
        try:
            url = f'http://{httpd.server_address[0]}:{httpd.server_address[1]}'
            found = fetch.fetch(url)
        finally:
            httpd.shutdown()
            t.join()

        self.assertEqual(b'Test', found)
        mock_sleep.assert_has_calls([call(5), call(5)])