#!/usr/bin/python
import sys
import socket
import traceback

#################################################################################################
#To run this script type at a command line 
#
# > python http_request.py [host] [port]
#
# host is the website you're tring to send a request to
# port is always 80 (the port for HTTP)
#
# example:
# > python http_request.py engineeringtheinternet.nfshost.com 80
#
# Modify the req variable to change what you are sending
#
# Credit where credit is due:  this script was modified from one provided by the 
# course staff of MIT's 6.858 (Computer Security) class in fall 2012.
# course staff: Nicolai Zeldovich (prof), with David Benjamin, Frank Wang, and Taesoo Kim (TAs)
#################################################################################################

#Only modify this part!!!!
#Type your request here:

req = """GET / HTTP/1.0


"""

#########################################################################
# Don't modify this part!  If you modify it, it might not work anymore
######################################################################

def send_req(host, port, req):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to %s:%d..." % (host, port))
    sock.connect((host, port))

    print("Connected, sending request...")
    sock.send(req)

    print("Request sent, waiting for reply...")
    rbuf = sock.recv(1024)
    resp = ""
    while len(rbuf):
	resp = resp + rbuf
	rbuf = sock.recv(1024)

    print("Received reply.")
    sock.close()
    return resp

####

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " host port")
    exit()

try:
    print("HTTP request:")
    print(req)

    resp = send_req(sys.argv[1], int(sys.argv[2]), req)
    print("HTTP response:")
    print(resp)
except:
    print("Exception:")
    print(traceback.format_exc())
