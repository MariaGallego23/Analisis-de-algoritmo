# Ejercicio 3: 1143. Longest Common Subsequence    
# Familia: programación dinámica
# https://leetcode.com/problems/longest-common-subsequence/
#
# ESTADO:      dp[i][j] = longitud de la LCS de text1[0..i) y text2[0..j)
# BASE:        dp[0][j] = dp[i][0] = 0  (un prefijo vacío no tiene nada en común)
# RECURRENCIA: si text1[i-1] == text2[j-1]:  dp[i][j] = 1 + dp[i-1][j-1]
#              si no:   dp[i][j] = max(dp[i-1][j], dp[i][j-1])

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n, m = len(text1), len(text2)

        # Tabla de (n+1) x (m+1) llena de ceros. La fila 0 y la columna 0
        # ya cumplen el caso base.
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Las letras coinciden: extendemos la mejor subsecuencia
                    # de los prefijos sin esas dos letras.
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # No coinciden: descartamos la última letra de text1
                    # o la de text2, y nos quedamos con la mejor opción.
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # La respuesta usa los prefijos completos.
        return dp[n][m]

# Complejidad: tiempo Θ(n·m), espacio Θ(n·m)
# (se puede bajar a Θ(min(n, m)) guardando solo dos filas).
