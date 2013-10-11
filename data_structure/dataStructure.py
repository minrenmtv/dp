class Stack():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


def parChecker(par):
	stack = Stack()
	for char in par:
		if char == "(":
			stack.push(char)
		elif char == ")":
			if stack.isEmpty():
				return False
			else:
				stack.pop()

	return stack.isEmpty()


def genParChecker(par):
	pass
