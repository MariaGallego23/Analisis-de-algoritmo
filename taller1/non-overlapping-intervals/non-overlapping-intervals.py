# Ejercicio 4: 435. Non-overlapping Intervals  
# Familia: greedy
# https://leetcode.com/problems/non-overlapping-intervals/
#
# Es la "selección de actividades" contada al revés:
#   maximizar los intervalos que CABEN = minimizar los que se BORRAN.
# CRITERIO GREEDY: ordenar por end y, entre los que aún caben,
#   quedarse con el que TERMINA ANTES (deja más espacio para los siguientes).

class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Ordenamos por el extremo derecho (end).
        intervals.sort(key=lambda x: x[1])

        kept = 0                 # cuántos intervalos nos quedamos
        end = float('-inf')      # end del último intervalo aceptado

        for s, e in intervals:
            if s >= end:
                # No pisa al último aceptado. Ojo: s == end NO es solapamiento
                # (los intervalos que solo se tocan son válidos).
                kept += 1
                end = e          # este pasa a ser el último aceptado
            # Si s < end se solapa: se "borra" (simplemente no lo contamos).

        # Los que se borran = total - los que se quedaron.
        return len(intervals) - kept

# Complejidad: tiempo O(n log n) por el sort, espacio O(1) extra
# si se ordena in-place (en Python el sort usa O(n) auxiliar).
