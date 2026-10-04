# Ejercicio 5: 39. Combination Sum    
# Familia: backtracking
# https://leetcode.com/problems/combination-sum/
#
# QUÉ SE ELIGE:  un candidato candidates[i] (se puede reutilizar).
# QUÉ SE DESHACE: el último elegido (path.pop()) al regresar de la recursión.
# PODA:           si el candidato supera lo que falta, se corta la rama.

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []     
        path = []    

        def bt(start, remaining):
            if remaining == 0:
                res.append(path[:])   
                return

            for i in range(start, len(candidates)):
                c = candidates[i]

                # PODA: este candidato (y los siguientes) se pasan del resto.
                if c > remaining:
                    break

                path.append(c)           
                bt(i, remaining - c)      
                                          
                path.pop()                

        bt(0, target)
        return res

# Complejidad: con n = len(candidates), t = target y min = menor candidato,
#   tiempo: exponencial en la profundidad, O(n^(t/min)) en el peor caso;
#   espacio: O(t/min) para la pila de recursión (más la salida).
