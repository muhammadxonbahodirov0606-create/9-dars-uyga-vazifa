import matplotlib.pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
ali = [10, 15, 12, 20, 25, 22, 30]
vali = [8, 12, 18, 16, 22, 27, 28]

plt.plot(kunlar, ali, color="blue", label="Ali")
plt.plot(kunlar, vali, color="red", label="Vali")

plt.title("Ikki o'quvchining haftalik o'qish natijalari")
plt.xlabel("Kunlar")
plt.ylabel("O'qish ko'rsatkichi")
plt.legend()
plt.grid(True)

plt.show()