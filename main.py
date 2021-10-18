from math import sqrt

def is_patrat(n):
    """is_patrat verifica daca un numar este patrat perfect

    Args:
        n (int): numarul ce urmeaza a fi verificat

    Returns:
        bool: Valoarea de adevar a verificarii
    """
    sq_root = int(sqrt(n))
    if (sq_root*sq_root) == n:
        return True
    return False


def lista_patrat_perfect(list):
    """lista_patrat_perfect Afișarea listei obținute din lista inițială în care numerele pătrat perfect sunt înlocuite cu 
radicalul acestora. În cazul numerelor care nu sunt pătrat perfect, acestea sunt înlocuite cu o listă 
cu numerele pătrat perfect mai mici decât numărul inițial.

    Args:
        list (int): lista ce urmeaza a fi folosita

    Returns:
        int: lista ceruta
    """
    l = []
    for x in range(len(list)):
        if list[x] < 0:
            l.append(list[x])
        elif is_patrat(list[x]) == True:
            l.append(int(sqrt(list[x])))
        else:
            li = []
            for x in range(1,list[x],1):
                if is_patrat(x) == True:
                    li.append(x)
            l.append(li)

    return l


def test_lista_patrat_perfect():
    """test_lista_patrat_perfect testeaza functia lista_patrat_perfect()
    """
    assert lista_patrat_perfect([4,9]) == [2,3]
    assert lista_patrat_perfect([5,4]) == [[1,4],2]
    assert lista_patrat_perfect([25, 13, 26, 9, -4, 0]) == [5, [1, 4, 9], [1, 4, 9, 16, 25], 3, -4, 0]


def suma_cifrelor(nr):
    """suma_cifrelor suma cifrelor unui numar nr

    Args:
        nr (int): numarul ce urmeaza a fi folosit

    Returns:
        int: suma cifrelor lui nr
    """
    suma = 0
    while nr > 0:
        suma = suma + nr%10
        nr = nr // 10

    return suma


def suma_cifrelor_mai_mare_decat_n(list,n):
    """suma_cifrelor_mai_mare_decat_n suma cifrelor fiecarui numar ce este mai mare sau egala decat n

    Args:
        list (int): lista ce urmeaza a fi folosita
        n (int): numar dat 
    Return:
        l (int): lista ceruta
    """
    l = []
    for x in range(len(list)):
        if suma_cifrelor(list[x]) >= n:
            l.append(list[x])
        
    return l


def test_suma_cifrelor_mai_mare_decat_n():
    assert suma_cifrelor_mai_mare_decat_n([1,12,44,2],5) == [44]
    assert suma_cifrelor_mai_mare_decat_n([1,31,22,12],1) == [1,31,22,12]
    assert suma_cifrelor_mai_mare_decat_n([0,0,0,0],1) == []

def suma_lower_bigger(list):
    """suma_lower_bigger Calculeaza suma dintre cel mai mic numar din lista si cel mai mare

    Args:
        list (int): lista ce urmeaza a fi utilizata
    Returns:
        int:Suma dintre cel mai mic numar si cel mai mare numar din sir
    """
    min = 99999999
    max = 0
    for x in range(len(list)):
        if list[x] < min:
            min = list[x]
    for x in range(len(list)):
        if list[x] > max:
            max = list[x]
    sum = min + max
    return sum



def test_suma_lower_bigger():
    """test_suma_lower_bigger testeaza functia suma_lower_bigger(list)
    """
    assert suma_lower_bigger([1,2,3,4]) == 5
    assert suma_lower_bigger([-1,4,1,2]) == 3
    assert suma_lower_bigger([3,1,12,34]) == 35



def afiseaza_toate_numerele_pozitize_concatenate(list):
    """afiseaza_toate_numerele_pozitize_concatenate Afiseaza toate numerele pozitive concatenate

    Args:
        list (int): lista numerelor ce urmeaza a fi verificate

    Returns:
        int: toate numerele pozitive cocantenate
    """
    c = 0
    for x in range(len(list)):
        if list[x] > 0:
            c = c*10 + list[x]
    return c

def test_afiseaza_toate_numerele_pozitize_concatenate():
    """test_afiseaza_toate_numerele_pozitize_concatenate testeaza functia afiseaza_toate_numerele_pozitize_concatenate
    """
    assert afiseaza_toate_numerele_pozitize_concatenate([1,2,3,4]) == 1234
    assert afiseaza_toate_numerele_pozitize_concatenate([0,1,2,3]) == 123
    assert afiseaza_toate_numerele_pozitize_concatenate([1,-1,2,3]) == 123

def citire_lista():
    """citire_lista Citeste o lista de la tastatura despartita prin caracterul ","
    """
    list = input("Citeste numerele din lista despartite prin <,>:" )
    list = list.split(",")
    for x in range(len(list)):
        list[x] = int(list[x])

    return list



def menu():
    """menu Afiseaza meniul de fiecare data cand functia este apelata
    """
    print("1.Citeste lista.")
    print("2.Afișeaza numărul obținut prin concatenarea tuturor numerelor pozitive din listă.")
    print("3.Afiseaza suma dintre cel mai mare număr din listă și cel mai mic număr din listă.")
    print("4.Afiseaza toate numerelor care au suma cifrelor mai mare sau egală decat un număr n citit de la tastatură.")
    print("5.Afiseaza lista obtinuta din lista inițială în care numerele pătrat perfect sunt înlocuite cu radicalul acestora.")
    print("6.Iesire.")



def main():
    test_lista_patrat_perfect()
    test_suma_lower_bigger()
    test_afiseaza_toate_numerele_pozitize_concatenate()
    test_suma_cifrelor_mai_mare_decat_n()
    while True:
        menu()
        optiune = int(input("Selectati Optiunea: "))
        if optiune == 1:
           list = citire_lista()
        if optiune == 2:
            print(afiseaza_toate_numerele_pozitize_concatenate(list))
        if optiune == 3:
            print(suma_lower_bigger(list))
        if optiune == 4:
            n = int(input("Citeste numarul n: "))
            print(suma_cifrelor_mai_mare_decat_n(list,n))
        if optiune == 5:
            print(lista_patrat_perfect(list))
        if optiune == 6:
            break
        else:
            print("Optiunea aleasa nu exista, incercati din nou!")

if __name__ == "__main__":
    main()