# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $

from bluetooth import *
import os
import sys

os.system("sudo hciconfig hci0 piscan")
os.system("sudo hciconfig hci0 name 'Pet Box'")

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "PetBoxServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )
                   
print ("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print ("Accepted connection from ", client_info)

while True:

    try:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        # print ("received [%s]" % data)
        json_string = data.decode('utf8').replace("'", '"')
        print('received', json_string)

        with open('settings.json', 'w') as f:
            f.write(json_string)

        sys.exit()
    except IOError:
        pass

    except KeyboardInterrupt:
        print ("disconnected")

        client_sock.close()
        server_sock.close()
        break
