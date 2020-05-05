from cryptography import x509
from cryptography.hazmat.backends import default_backend
pem_data = 'workingcert.crt'
cert = x509.load_pem_x509_certificate(pem_data, default_backend())
cert.serial_number
