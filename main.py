# EXO 1:
def tableau():
    tab = [1, 2, 3, 4, 5]
    tab.reverse()
    print(tab)
tableau()

# EXO 2:

def chaine_caractere():
    chaie1 = "alpha"
    chaie2 = "mamadou"
    m = ""
    for x in chaie1:
        for y in chaie2:
            while x == y:
                m = y
                break
    print(m)

chaine_caractere()

def chaie_carac(chaie1 = "klbc", chaie2 = "kaba"):
    pecos = []
    for a in chaie1 :
        for b in chaie2 :
            if a == b :
                if a not in pecos:
                    pecos.append(a)
    print(pecos)
    return pecos
chaie_carac()

# EXO 3:

def table_retour(valeur1, valeur2):
    table_retour = []

    for ama in valeur1 :
        if ama not in valeur2 :
            table_retour.append(ama)

        for ama in valeur2 :
            if ama not in valeur1 :
                table_retour.append(ama)

        return table_retour

result = table_retour([2, 4, 7, 8, 2], [1, 3, 9, 4, 6, 7])
print(result)