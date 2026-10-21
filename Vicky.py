from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title> DEVICE PROPERTIES</title>
    </head>
    <body bgcolor="white">
        <i><h3> NAME = KEERTHIKA</h3></i>
        <i><h3> REF NO=26013618</h3></i>
        <table border="1"
        cellspacing="10" cellpadding="10">
        <caption>DEVICE PROPERTIES</caption>
        <tr bgcolor="pink">
        <th> S.no</th>
        <th>Device Info</th>
        <th>Device properties</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Device name</td>
            <td>TL15-53M-G2</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Installed ram</td>
            <td>16.0 GB </td>
        </tr>
         <tr>
            <td>3</td>
            <td>Storage</td>
            <td>135 GB of 477 GB used</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Product ID</td>
            <td>00342-42954-1164-AAOEM</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Graphics Card</td>
            <td>Intel(R) Graphics(128 MB)
        </tr>
    </table>
    </body>
    </html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()