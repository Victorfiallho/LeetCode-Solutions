class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1 
        
        anterior = 1
        atual = 2
        
        for i in range (n - 2):
            proximo = anterior + atual
            anterior = atual 
            atual = proximo
            
        return atual