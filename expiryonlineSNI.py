#also useful
#https://serverlesscode.com/post/ssl-expiration-alerts-with-lambda/

import ssl,socket
import OpenSSL
hostname = "backup.cliocom.it"
port = 443

context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as sslsock:

        der_cert = sslsock.getpeercert(True)

        # from binary DER format to PEM
        pem_cert = ssl.DER_cert_to_PEM_cert(der_cert)          
        #print(pem_cert)

x509online = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, pem_cert)
x509online.get_notAfter()
print(f'expiry from file: {x509online.get_notAfter()}')
print (x509online.get_notAfter())