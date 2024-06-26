import copy
from time import time
from functools import lru_cache

class Model:
    def __init__(self):
        self._anagrammi = set() #elimina le ripetizioni
        self.anagrammi_list = []

    def calcola_anagrammi(self, parola):
        self._anagrammi = set()
        self.ricorsione("", "".join(sorted(parola))) #al livello 0 ho una stringa vuota come parziale
        return self._anagrammi

    @lru_cache(maxsize=None)
    def ricorsione(self, parziale, lettere_rimanenti):
        #Caso terminale, non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self._anagrammi.add(parziale)
            return
        else:
            #Caso non terminale: dobbiamo provare ad aggiungere una lettera per volta
            #e andare avanti nella ricorsione
            for i in range(len(lettere_rimanenti)):
                parziale += lettere_rimanenti[i] #aggiungo una lettera
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:] #saltiamo l'i-esimo
                self.ricorsione(parziale, nuove_lettere_rimanenti) #vado avanti con la ricorsione
                parziale = parziale[:-1] #tolgo la lettera che avevo aggiunto
    @lru_cache(maxsize=None)
    def calcola_anagrammi_list(self, parola):
        self.anagrammi_list = []
        self.ricorsione_list([], parola) #al livello 0 ho una lista vuota come parziale
        return self.anagrammi_list

    def ricorsione_list(self, parziale, lettere_rimanenti): #stesso metodo ma usando una LISTA
        #Caso terminale, non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self.anagrammi_list.append(copy.deepcopy(parziale)) #copia della lista
            return
        else:
            #Caso non terminale: dobbiamo provare ad aggiungere una lettera per volta
            #e andare avanti nella ricorsione
            for i in range(len(lettere_rimanenti)):
                parziale.append(lettere_rimanenti[i]) #aggiungo una lettera
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:] #saltiamo l'i-esimo
                self.ricorsione_list(parziale, nuove_lettere_rimanenti) #vado avanti con la ricorsione
                parziale.pop() #tolgo la lettera che avevo aggiunto


if __name__ == "__main__":
    model = Model()
    start_time = time()
    print(model.calcola_anagrammi("casasasasa"))
    end_time = time()
    print(end_time - start_time)
    print(model.calcola_anagrammi_list(["c","s","a"]))
