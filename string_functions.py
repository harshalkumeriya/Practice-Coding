
class check:

	def __init__(self,input_str):
		self.string = input_str
		print(f'user input is : {self.string}')

	def vowels(self):
		y = [i for i in self.string if i in ['a','e','i','o','u']]
		print(len(list(set(y))))

	def spaces(self):
		print(self.string.count(' '))

	def letters(self):
		'''without spaces'''
		print(len(self.string.replace(' ', '')))

	def words(self):
		m = self.string.split(' ')
		n = m.copy()
		print(n)
		for i in n:
			if i == '':
				m.remove(i)
		print(len(m))

if __name__ == "__main__":
	x = check("    Tata   Consultancy     Services ltd")
	x.vowels()
	x.spaces()
	x.letters()
	x.words()