# and or not

operador_and_true = True and True
operador_and_falso = False and False

#COM AND SE UM DOS LADOS FOR FALSO SEŔA FALSO

operador_or_true = True or True
operador_or_falso = False or False

#COM OR SE UM DOS LADOS FOR VERDADEIRO SERÁ VERDADEIRO

operador_not_true = not True
operador_not_false = not False

#COM O NOT SE O OPERADOR FOR TRUE VAI SER FALSO, SE OPERADOR FOR FALSO VAI SER TRUE

operadores = 7 == 7 and 7 < 6 #false
operadores = 7 == 7 and 7 > 6 #True
operadores = (5 == 7 or 3 >= 3)#True
operadores = (5 == 7 or 3 >= 3)#True
operadores = not (5 == 7 or 3 >= 3)#False


print(operadores)