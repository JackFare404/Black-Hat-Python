import socket

target_host = "127.0.0.1"
target_port = 21

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"GET / HTTP/1.1\r\nHost: ***.com\r\n\r\n")

response = client.recv(4096)

print(response)
# client.close()
'''
#target_host = ***.com
HTTP/1.1 200 OK\r\n
Server: PAAS-WEB\r\n
Date: Tue, 12 Apr 2022 06:47:55 GMT\r\n
Content-Type: text/html\r\n
Content-Length: 473\r\n
Last-Modified: Sun, 09 Oct 2016 03:15:06 GMT\r\n
Connection: keep-alive\r\n
ETag: "57f9b63a-1d9"\r\n
processtime: 0.000\r\n
Accept-Ranges: bytes\r\n
\r\n
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n
<!-- (C) COPYRIGHT International Business Machines Corporation 1999 -->\n
<!-- All Rights Reserved -->\n
<!-- Licensed Materials - Property of IBM -->\n
<!-- -->\n
<!-- US Government Users Restricted Rights - Use, duplication or  -->\n
<!-- disclosure restricted by GSA ADP Schedule Contract with IBM Corp.-->\n
<!-- -->\n<html>\n
<body onload=\'document.location.href="http://***.com/next/index.html"\'>\n</body>\n</html>\n'
'''






# import socket
#
# target_host ='127.0.0.1'
# target_port = 9999
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# client.connect((target_host, target_port))
#
# #sd = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode()
#
# client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
#
# response = client.recv(4096)
#
# print(response)
