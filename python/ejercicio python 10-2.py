def notaF ():
    nota1 = float(input("nota parcial"))
    nota2 = float(input("nota de los TPs"))
    nota3 = float(input("nota del examen"))

    notaP = (nota1 / 100) * 30
    notaTP = (nota2 / 100) * 20
    NotaE = (nota3 / 100) * 50
    notaFinal = (notaP + notaTP + NotaE)

    print ("La nota final va ser:" , notaFinal)

notaF ()
