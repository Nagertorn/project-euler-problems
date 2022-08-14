from solution_by_mind import solution_by_mind
from solution_by_hand import solution_by_hand
import os
os.system('clear')


print("--- DE 1 A 10 ---")
print("Número a partir de la solución")
print(solution_by_hand([5, 7, 8, 9]))
print("--")
print("Número a partir de mi solución")
print(solution_by_mind(range(1, 11)))
