# Ejercicio 1: 56. Merge Intervals  
# Familia: ordenamiento
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0][:]]

        for s, e in intervals[1:]:
            ultimo = res[-1]
            if s <= ultimo[1]:
                
                ultimo[1] = max(ultimo[1], e)
            else:
                res.append([s, e])
        return res

# Complejidad: tiempo O(n log n) (domina el sort), espacio O(n) para la salida.
