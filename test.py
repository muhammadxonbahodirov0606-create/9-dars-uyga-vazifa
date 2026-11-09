from pathlib import Path, Path

import matplotlib.pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat, ball, color="purple", s=100)
plt.title("Tayyorlanish vaqti va test ballari")
plt.xlabel("Tayyorlanish vaqti (soat)")
plt.ylabel("Test bali")
plt.grid(True)

rasm_fayli = Path(__file__).with_name("oqish_vaqti_test_bali.png")
plt.savefig(rasm_fayli)
plt.show()

print("Bog'liqlik: tayyorlanish vaqti oshgani sari test ballari ham ko'tarilgan.")