from django.test import TestCase

# Create your tests here.
class EstoqueTest(TestCase):

	def test_equals_quantidade(self):
		string1 = 'a'
		string2 = 'A'
		self.assetEquals(string1, string2)
