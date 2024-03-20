# Algorytm sprawdzania identyczności grafów:
# 1. Sprawdź, czy grafy mają tę samą liczbę wierzchołków i krawędzi. Jeśli nie, grafy nie są identyczne.
# 2. Sprawdź, czy wierzchołki o tych samych numerach mają takich samych sąsiadów.


def graphIdentical(G1, G2):
    # Ad. 1
    # ilosc wierzcholkow
    if len(G1)!= len(G2):
        return False
    #ilosc krawedzi
    E1 = 0
    E2 = 0
    for i in range (0,len(G1)):
        E1 += len(G1[i])
        E2 += len(G2[i])
    if(E1!=E2):
        return False
    
    # Ad. 2
    # sortowanie grafów
    sorted_G1 = {k: sorted(v) for k, v in G1.items()}
    sorted_G2 = {k: sorted(v) for k, v in G2.items()}

    for vertex in sorted_G1:
        if vertex not in sorted_G2:
            return False
        if sorted_G1[vertex] != sorted_G2[vertex]:
            return False

    return True


    
G1 = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
G2 = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
G3 = {0: [1, 2], 1: [2, 0], 2: [1, 0]} # identyczny do G1 i G2
G4 = {0: [1, 2], 1: [0, 3], 2: [0, 1]} # nieidentyczny

print(graphIdentical(G1, G2)) # true
print(graphIdentical(G1, G3)) # true
print(graphIdentical(G1, G4)) # false