import sys

"""
Kodeoppgave - Ardoq

Funksjonen høyesteProdukt() tar inn en liste med tall, og retunerer det høyeste produktet mellom
tre av tallene i listen. 

En mulig løsning kunne vært å sortere listen, og dermed ta maksimum av summen av de tre største tallene, 
eller det største tallet multiplisert med de to laveste, men dette er en mindre effektiv løsning 
ettersom sortering av en liste kjører i O(n log n).

En bedre løsning er den som er skrevet under, som kjører i lineær tid (O(n)) ettersom vi itererer listen, kun
en gang, med følgende konstanttidsoperasjoner. Her unngår vi kjøretiden som følger av å sortere listen, 
ettersom vi - for hver iterasjon - oppdaterer variablene som trengs for å beregne det største produktet. 
"""

def høyesteProdukt(tallListe):
    minste = sys.maxsize
    nestMinste = sys.maxsize
    største = -sys.maxsize - 1
    nestStørste = -sys.maxsize - 1
    tredjeStørste = -sys.maxsize - 1

    for tall in tallListe:
        if tall < minste:
            nestMinste = minste
            minste = tall
        elif tall < nestMinste:
            nestMinste = tall
        
        if tall > største:
            tredjeStørste = nestStørste
            nestStørste = største
            største = tall
        elif tall > nestStørste:
            tredjeStørste = nestStørste
            nestStørste = tall
        elif tall > tredjeStørste:
            tredjeStørste = tall
    
    # Det høyeste produktet kan sammenfatte de to laveste tallene, ettersom de kan være negative
    return max(største * nestStørste * tredjeStørste, største * nestMinste * minste)

assert høyesteProdukt([1, 10, 2, 6, 5, 3]) == 300
assert høyesteProdukt([-100, -10, 5, 3, 10]) == 10000
assert høyesteProdukt([3, 4, -10, 1]) == 12