import OpenSSL.crypto

cert = OpenSSL.crypto.load_certificate(
      OpenSSL.crypto.FILETYPE_PEM,
      open('workingcert.crt').read()
)

plaincert = open('workingcert.crt').read()
#print(plaincert)

decrypted = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_TEXT, cert)
#print (decrypted)

certificate = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, plaincert)
#print(certificate)
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, plaincert)
x509.get_notAfter()
print (x509.get_notAfter())
