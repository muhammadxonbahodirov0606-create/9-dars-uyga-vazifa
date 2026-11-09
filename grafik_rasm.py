from pathlib import Path

import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
kitob_betlari = [12, 18, 15, 24, 20, 30, 35]

plt.plot(kunlar, kitob_betlari, marker="o")
plt.title("Hafta davomida o'qilgan kitob sahifalari")
plt.xlabel("Hafta kunlari")
plt.ylabel("O'qilgan sahifalar soni")
plt.grid(True)

rasm_fayli = Path(__file__).with_name("natija.png")
plt.savefig(rasm_fayli)
plt.show()