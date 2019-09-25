cadena = "   "
cadena = cadena.lstrip()
cadena = cadena.rstrip()

# Comprobar con la forma idiomática
if not cadena:
	print("La cadena está vacía")
else:
	print("La cadena NO está vacía")

# O contar sus caracteres
if len(cadena) is 0:
	print("La cadena está vacía")
else:
	print("La cadena NO está vacía")

# Lo contrario de hace un momento:
if cadena:
	print("Ok la cadena no está vacía")
else:
	print("La cadena está vacía")