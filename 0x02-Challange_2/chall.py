#funcion
#SMMLV ($908.526)
#salarios por cargos
# 3 SMMLV - ingenieros , 2 SMMLV tecnologo
# PS - 6% retencion , 2% salud, 6% pension, 0% arl
# TF- 10 % , 8% , 2%, 4%
# Ti - 5%, 4%, 4%, 4%
# AP - 0%, 0% ,0%, 4%

def calcularSalario (nombre , tipoContrato, cargo): 
    nombre = nombre.upper()
    tipoContrato = tipoContrato.upper()
    SMMLV = 908526
    if cargo == 1:
        salario_base = SMMLV * 2
        if tipoContrato == "PRESTACIONSERVICIOS":
            salario_total = (salario_base)-(salario_base * 0.06+ salario_base * 0.02 + salario_base * 0.06 + salario_base * 0 )
            dict = {"nombre":nombre,
                    "tipo contrataci�n": tipoContrato, 
                    "cargo": cargo,
                    "salario base": salario_base,
                    "retefuente" : salario_base * 0.06,
                    "salud" : salario_base * 0.02,
                    "pension": salario_base * 0.06,
                    "arl": salario_base * 0,
                    "salario total": salario_total
                    }
        elif tipoContrato == "TERMINOFIJO":
            salario_total = (salario_base)-(salario_base * 0.1+ salario_base * 0.08 + salario_base * 0.02 + salario_base * 0.04 )
            dict = {"nombre":nombre, 
                    "tipo contrataci�n": tipoContrato, 
                    "cargo": cargo,
                    "salario base": salario_base,
                    "retefuente" : salario_base * 0.1,
                    "salud" : salario_base * 0.08,
                    "pension": salario_base * 0.02,
                    "arl": salario_base * 0.04,
                    "salario total": salario_total
                    }
        elif tipoContrato == "TERMINOINDEFINIDO":
            salario_total = (salario_base)-(salario_base * 0.05+ salario_base * 0.04 + salario_base * 0.04 + salario_base * 0.04 )
            dict = {"nombre":nombre, 
                    "tipo contrataci�n": tipoContrato, 
                    "cargo": cargo,
                    "salario base": salario_base,
                    "retefuente" : salario_base * 0.05,
                    "salud" : salario_base * 0.04,
                    "pension": salario_base * 0.04,
                    "arl": salario_base * 0.04,
                    "salario total": salario_total
                    }
        elif tipoContrato == "APRENDIZAJE":
            salario_total = (salario_base)-(salario_base * 0 + salario_base * 0 + salario_base * 0 + salario_base * 0.04 )
            dict = {"nombre":nombre, 
                    "tipo contrataci�n": tipoContrato, 
                    "cargo": cargo,
                    "salario base": salario_base,
                    "retefuente" : salario_base * 0,
                    "salud" : salario_base * 0,
                    "pension": salario_base * 0,
                    "arl": salario_base * 0.04,
                    "salario total": salario_total
                    }
        else:
            return TypeError

    elif cargo == 2:
        salario_base = SMMLV * 3
        if tipoContrato == "PRESTACIONSERVICIOS":
            salario_total = (salario_base)-(salario_base * 0.06+ salario_base * 0.02 + salario_base * 0.06 + salario_base * 0 )
            dict = {"nombre":nombre, 
                    "tipo contrataci�n": tipoContrato, 
                    "cargo": cargo,
                    "salario base": salario_base,
                    "retefuente" : salario_base * 0.06,
                    "salud" : salario_base * 0.02,
                    "pension": salario_base * 0.06,
                    "arl": salario_base * 0,
                    "salario total": salario_total
                    }
        elif tipoContrato == "TERMINOFIJO":
            salario_total = (salario_base)-(salario_base * 0.1+ salario_base * 0.08 + salario_base * 0.02 + salario_base * 0.04 )
            dict = {"nombre":nombre, 
                    "tipo contrataci�n": tipoContrato, 
                    "cargo": cargo,
                    "salario base": salario_base,
                    "retefuente" : salario_base * 0.1,
                    "salud" : salario_base * 0.08,
                    "pension": salario_base * 0.02,
                    "arl": salario_base * 0.04,
                    "salario total": salario_total
                    }
        elif tipoContrato == "TERMINOINDEFINIDO":
            salario_total = (salario_base)-(salario_base * 0.05+ salario_base * 0.04 + salario_base * 0.04 + salario_base * 0.04 )
            dict = {"nombre":nombre, 
                    "tipo contrataci�n": tipoContrato, 
                    "cargo": cargo,
                    "salario base": salario_base,
                    "retefuente" : salario_base * 0.05,
                    "salud" : salario_base * 0.04,
                    "pension": salario_base * 0.04,
                    "arl": salario_base * 0.04,
                    "salario total": salario_total
                    }
        elif tipoContrato == "APRENDIZAJE":
            salario_total = (salario_base)-(salario_base * 0 + salario_base * 0 + salario_base * 0 + salario_base * 0.04 )
            dict = {"nombre":nombre, 
                    "tipo contrataci�n": tipoContrato, 
                    "cargo": cargo,
                    "salario base": salario_base,
                    "retefuente" : salario_base * 0,
                    "salud" : salario_base * 0,
                    "pension": salario_base * 0,
                    "arl": salario_base * 0.04,
                    "salario total": salario_total
                    }
        else:
            return TypeError
    else:
        return TypeError
    return(dict)