'''
Convertir grados Celsius a Fahrenheit:
• Pedir los grados Celsius usando try – except y aceptar solo de -10 a 49
grados Celsius
• Procesar convirtiendo grados Celsius a Fahrenheit
• Mostrar en pantalla los grados Fahrenheit o el mensaje de error.
'''

# start try/exception in order to catch errors with value types
# except will handle if the value input is string 
try: 
    # this is where a function (if normal) starts
    # ask to provide input value
    gcel = float(input("Dame grados celsius... "))
    # the conditional execution starts
    # if value from input is greater thatn -10 and less or equal to 49
    if gcel >= -10 and gcel <= 49:
        # the following formula gets executed, to covert values from celsius to farenheit
        gfar = 32 + gcel*9/5
        print(gcel, "grados celsius son", gfar, "grados fahrenheit")
    else:
        # else will handle if the values are outside of the range
        print("Los valores deben ser entre -10 y 49 grados cels")
except:
    print("Dame solo un numero de punto flotante")
