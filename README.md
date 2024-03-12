# pythonSSLSelfSignedCert

SSL/TLS provide a way for clients and servers to establish a shared secret to secure their communications over the internet.
An important part of SSL/TLS are certificates that authenticate the server's public key. Certificates are usually issued by a
trusted certificate authority, but you can also use a self-signed certificate.

This is a simple echo client and server that communicate over a TLS channel. To make this work we generate a self-signed certificate for the server. We can use the openssl command to generate a self-signed certificate.


`openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem`

openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=AB/L=YYC/O=UofC/OU=CPSC/CN=localhost"
