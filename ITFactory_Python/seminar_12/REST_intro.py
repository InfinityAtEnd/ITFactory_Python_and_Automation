"""
REST - REpresentational State Transfer -> is an architectural style for providing standards between computer systems on
  			the web making it easier for systems to communicate with each other

REST-compliant systems, also called RESTful systems are caracterized by how they are stateless and separate the concerns of client and server
For an API to be considered RESTful it must have the following constrains:
	- client-server architecture
	- statelessness: the server does not store any client context between context, so each request contains all the information needed to complete it
	- cache ability: clients can cache response data, reducing the number of requests to the server and improving performance
					cache = zona mica de memorie care stocheaza pentru o perioada foarte scurta date
	- use of http methods: GET, POST, PUT, DELETE
	- use of http status codes: success(200), failure(400), not found(404)
"""
