'''
PROXY - is a structural design pattern that lets you provide a substitute or a placeholder for another object.
A proxy controls access to the original object allowing you to perform something either before or after
 	the request gets through to the original object
'''

from abc import ABC, abstractmethod


class Subject(ABC):
	@abstractmethod
	def request(self):
		pass


class RealSubject(Subject):
	def request(self):
		print('RealSubject: handling request!')


class Proxy(Subject):
	def request(self):
		if self.check_access():
			self._real_subject.request()
			self.log_access()

	def __init__(self, real_subject):
		self._real_subject = real_subject

	def check_access(self):
		print('Proxy: checking access!')
		return True

	def log_access(self):
		print('Proxy: logging the time of the request!')


real_subject = RealSubject()
real_subject.request()
print('*' * 80)
proxy = Proxy(real_subject)
proxy.request()

'''
PROS:
	- you can control the subject object without anyone knowing about it
	- you can manage the live cycle of the subject object 
	- the proxy works even if the subject isn't ready or is not available 
CONS:
	- the code may become more complicated since you need to introduce a lot of new classes
	- the response from the subject might get delayed 
'''