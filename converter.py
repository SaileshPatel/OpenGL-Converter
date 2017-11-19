rgbCode = input("Enter the RGB code you want to convert here: \n" )
completeCode = rgbCode.split()

for code in completeCode:
	intCode = float(code)
	print(float(intCode) / 255)