import OpenSSL.crypto
import ssl,socket

pem_cert = open('workingcert.crt').read()
#print(plaincert)

certificate = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, pem_cert)
#print(certificate)
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, pem_cert)
x509.get_notAfter()
print(f'expiry from file: {x509.get_notAfter()}')
print (x509.get_notAfter())
############################## end of expiry from file


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
print(f'expiry date fetched online: {x509online.get_notAfter()}')
print (x509online.get_notAfter())


if x509online.get_notAfter() == x509.get_notAfter():
      print('cert is the same')
else:
      print('cert is different than existing, proceeding')