print("\nBasic Calculator")

while True:

	print("\nMain Menu")
	print("\n1 ) Addition ")
	print("2 ) Substraction ")
	print("3 ) Multiplication ")
	print("4 ) Division ")
	print("5 ) Floor Divison ")
	print("6 ) Modulus ")
	print("7 ) Exponent ")
	print("8 ) Square ")
	print("9 ) Cube ")
	print("10 ) Square Root")
	print("11 ) Cube Root")
	print("0 ) Exit")

	choice = int(input("\n _ > : "))
	
	match choice:
		case 1:
			print("\nAddition")

			num1 = float(input("\nEnter Number 1 : "))
			num2 = float(input("Enter Number 2 : "))
			
			print(f"\nAddition : {num1} + {num2} = {num1+num2}")

		case 2:
			print("\nSubstraction")

			num1 = float(input("\nEnter Number 1 : "))
			num2 = float(input("Enter Number 2 : "))
			
			print(f"\nAddition : {num1} - {num2} = {num1-num2}")

		case 3:
			print("\nMultiplication")

			num1 = float(input("\nEnter Number 1 : "))
			num2 = float(input("Enter Number 2 : "))

			print(f"\nAddition : {num1} * {num2} = {num1*num2}")
		case 4:
			print("\nDivision")

			num1 = float(input("\nEnter Number 1 : "))
			num2 = float(input("Enter Number 2 : "))

			print(f"\nAddition : {num1} / {num2} = {num1/num2}")

		case 5:
			print("\n Floor Division")

			num1 = float(input("\nEnter Number 1 : "))
			num2 = float(input("Enter Number 2 : "))

			print(f"\nFloor Division : {num1} // {num2} = {num1//num2}")

		case 6:
			print("\nModulus")

			num1 = float(input("\nEnter Number 1 : "))
			num2 = float(input("Enter Number 2 : "))

			print(f"\nModulus : {num1} % {num2} = {num1%num2}")

		case 7:
			print("\nMultiplication")

			num1 = float(input("\nEnter Base Number : "))
			num2 = float(input("Enter Power Number : "))

			print(f"\nMultiplication : {num1} ^ {num2} = {num1**num2}")
		
		case 8:
			print("\nSquare")

			num = float(input("\nEnter Number "))

			print(f"\nSquare : {num} * {num} = {num*num}")

		case 9:
			print("\nCube")

			num = float(input("\nEnter Number "))

			print(f"\nCube : {num} * {num} * {num} = {num*num*num}")

		case 10:
			print("\nSquare Root")

			num = float(input("\nEnter Number "))

			print(f"\nSquare Root = {num*(1/2)}")

		case 11:
			print("\nCube Root")

			num = float(input("\nEnter Number "))

			print(f"\nCube Root = {num*(1/3)}")

		case 0:
			print("\nProgram Exited")
			break

		case _ :
			print("\nInvalid Input")