# pythonSSLSelfSignedCert

SSL/TLS provide a way for clients and servers to establish a shared secret to secure their communications over the internet.
An important part of SSL/TLS are certificates that authenticate the server's public key. Certificates are usually issued by a
trusted certificate authority, but you can also use a self-signed certificate.

This is a simple echo client and server that communicate over a TLS channel. To make this work we generate a self-signed certificate for the server. We can use the openssl command to generate a self-signed certificate:


`openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem`

executing the command this way will activate an interactive prompt where you are asked some questions about the subject of the certificate. The Common Name (CN) should be the same as the hostname of the server. In this example CN is "localhost" because the server runs on your own machine. 
You can also explicitly specify the algorithms used to generate the certificate and provide the identity information as part of the command as in the example below:

`openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=AB/L=YYC/O=UofC/OU=CPSC/CN=localhost"`
