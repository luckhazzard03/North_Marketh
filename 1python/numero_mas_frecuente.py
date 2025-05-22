from collections import Counter

# se define la función num_frecuente que toma una lista de números como argumento
def num_frecuente(lista):    
    # se crea el diccionario con la frecuencia de cada número
    conteo = Counter (lista)
    max_frecuencia = max (conteo.values ())# se obtiene la frecuencia máxima
    # se filtran los numeros que tiene la frecuencia máxima
    num_frecuentes = [num for num, freq in conteo.items () if freq == max_frecuencia]
    # retorna el menor de los números que tienen la mayor frecuencia 
    return min(num_frecuentes) 

if __name__ == "__main__":
    # Ejemplos de uso
    lista1 = [1, 3, 1, 3, 2, 1]# lista de prueba
    resultado1 = num_frecuente(lista1)# llamada a la función
    print(f"El número más frecuente en la lista {lista1} es: {resultado1}")# imprime el resultado
    
    #Segundo ejemplo
    lista2= [4, 4, 5, 5]# lista de prueba
    resultado2 = num_frecuente(lista2)# llamada a la función
    print(f"El número más frecuente en la lista {lista2} es: {resultado2}")# imprime el resultado
    
