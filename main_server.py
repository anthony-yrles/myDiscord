from socket_server.Server import *

host = "127.0.0.1"
user = "root"
password = "Vcassis13*"  
database = "mydiscord"

server = Server('10.10.107.118', 8080, 5, host, user, password, database)

try:
    Server.run()
    while True:
        client_socket, client_address = server.accept_client()        

except Exception as e:
    print(f"Error: {e}")
finally:
    server.close()
