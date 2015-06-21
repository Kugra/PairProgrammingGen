#!/usr/bin/env python3
#-*-coding: utf-8 -*-

__author__ = "Johan"

"""#!/usr/bin/python3"""

def pairGenerator():

    timeAceleradora=["Amanda", "Eduardo", "Guilherme",
                 "Johan", "Juliana", "Lucas",
                 "Marcus", "Rafael", "Raphael",
                 "Thiago", "Yasser"];

    mantidoHistoria=[]

    import random
    for manter in range(0,5):

        print("Escolha um integrante para manter na historia", timeAceleradora)
        nome = input()

        try:
            if nome in timeAceleradora:
                mantidoHistoria.append(nome)
                timeAceleradora.remove(nome)
            else:
                print("Opção inválida\nReiniciado: ")
                pairGenerator()

        except ValueError:
            print("Opção inválida\nReiniciado: ")
            pairGenerator()

    random.shuffle(mantidoHistoria)
    random.shuffle(timeAceleradora)

    print("Pares do pareamento: ")
    print(mantidoHistoria[:5], "<= Mantidos")
    print(timeAceleradora[:5], "<= Sorteados")
    print("Coringa: ", timeAceleradora[-1])

pairGenerator()