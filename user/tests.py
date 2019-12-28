from django.test import TestCase

# Create your tests here.
class LoginTest(TestCase):

	def test_login(self):
		t = self.client.get("/user/")
		# print(t)
		self.assertRedirects(t,'/user/login/?next=/user/')


class ContractTest(TestCase):

	def contract_create(self):
		login = self.client.login(username='jothamclient',password='jookoye@?')
		cnt = self.client.post("/user/contracts/create/",{})
		print (cnt)
