
class Converter:

	def __init__(self, op1, amount, op2):
		self.op1 = op1
		self.amount = amount
		self.op2 = op2



	def sm_To_M(self):
		return self.amount / 100

	def sm_To_Km(self):
		return self.amount / 100000

	def sm_To_Ml(self):
		return self.amount / 16093.4

	def m_To_Sm(self):
		return self.amount * 100

	def m_To_Km(self):
		return self.amount / 1000

	def m_To_Ml(self):
		return self.amount / 1609.34

	def km_To_Sm(self):
		return self.amount * 100000

	def km_To_m(self):
		return self.amount * 1000

	def km_To_Ml(self):
		return self.amount / 1.60934

	def ml_To_Sm(self):
		return self.amount * 160934

	def ml_To_m(self):
		return self.amount * 1609.34

	def ml_To_Km(self):
		return self.amount * 1.60934


def checkAmountType(amount):
	while True:

		if not amount.isdigit():
			amount = input("please input a number: ")
			continue

		if  int(amount) < 0:
			amount = input("please input positive integer: ")
			continue

		amount = int(amount)
		break

	return amount


def checkOptionsType(op):

	while True:

		if op.isdigit():
			op = input("please input this options - (sm, m, km, ml): ")
			continue
		else:
			op = op.lower()



		if not (op == "sm" or op == "m" or op == "km" or op == "ml" or "exit"):
			op = input("please input right option - (sm, m, km, ml): ")
			continue

		break

	return op


def is_op1_equal_op2(op1, op2):
	while True:
		
		if op1 == op2:
			op2 = input("please input different  than first: ")
			continue

		break	

	return op2


		

def menu():

	while True:

		op1 = input("input the unit of measurement (sm, m, km, ml) or 'exit' : ")
		op1 = checkOptionsType(op1)

		if op1 == "exit":
			print("bye bye!")
			break
		

		amount = input("input quantity (number): ")
		amount = checkAmountType(amount);

		op2 = input("input in which unit you want to transfer (sm, m, km, ml) or 'exit' : ")
		op2 = checkOptionsType(op2)

		print("-" * 30)

		if op2 == "exit":
			print("bye bye!")
			break

		op2 = is_op1_equal_op2(op1, op2)
	 


		userInput = Converter(op1, amount, op2)

		if op1 == "sm":
			if op2 == "m":
				converted = userInput.sm_To_M()

			elif op2 == "km":
				converted = userInput.sm_To_Km()

			elif op2 == "ml":
				converted = userInput.sm_To_Ml()



		elif op1 == "m":
			if op2 == "sm":
				converted = userInput.m_To_Sm()

			elif op2 == "km":
				converted = userInput.m_To_Km()

			elif op2 == "ml":
				converted = userInput.m_To_Ml()



		elif op1 == "km":
			if op2 == "sm":
				converted = userInput.km_To_Sm()

			elif op2 == "m":
				converted = userInput.km_To_m()

			elif op2 == "ml":
				converted = userInput.km_To_Ml()



		elif op1 == "ml":
			if op2 == "sm":
				converted = userInput.ml_To_Sm()

			elif op2 == "m":
				converted = userInput.ml_To_m()

			elif op2 == "km":
				converted = userInput.ml_To_Km()

		print(f"{amount} {op1} = {converted} {op2} \n")

menu()


