import http.server
import json
import psycopg2


# Database connection details
db_host = 'localhost'
db_name = 'postgres'
db_user = 'postgres'
db_password = 'pasword'

# Define the request handler
class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Convert the JSON data into a Python dict
        request_data = json.loads(post_data)

        # Store the request data in PostgreSQL
        try:
            conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
            cursor = conn.cursor()

            # Convert the request_data dict to JSON string
            json_data = json.dumps(request_data)

            # Insert the JSON data into the database
            cursor.execute("INSERT INTO public.your_table_name (data) VALUES (%s)", (json_data,))

            # Commit the transaction
            conn.commit()

            # Send a response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Success')

        except psycopg2.Error as e:
            print("Error storing data in PostgreSQL:", e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

# Start the server
server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, RequestHandler)
print('Server running on http://localhost:8000')
httpd.serve_forever()
