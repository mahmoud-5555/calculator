"""..."""

class opratetion:
	op = ''

	def add(self, char):
		self.op += char

	def pop_last(self):
		if self.op != '':
			self.op = self.op[:-1]
	
	def evalution(self):
		res = ''
		print ('the res befor calcluted: {}'.format(res))
		if self.op == '':
			return ''

		try:
			res = str(eval(self.op))
		except Exception:
			print ('Error')
			return 'Error'
		print ('the res after calcluted: {}'.format(res))
		return res
 
	def delet_all(self):
		self.op = ''

