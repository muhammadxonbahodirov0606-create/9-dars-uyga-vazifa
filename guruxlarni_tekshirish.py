import matplotlib.pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar, guruh_a, color="blue", marker="o", label="Guruh A")
plt.plot(testlar, guruh_b, color="red", marker="s", label="Guruh B")

plt.title("Ikki guruhning test natijalari")
plt.xlabel("Testlar")
plt.ylabel("Ballar")
plt.legend()
plt.grid(True)

plt.savefig("guruhlar_natijasi.png")
plt.show()

ortacha_a = sum(guruh_a) / len(guruh_a)
ortacha_b = sum(guruh_b) / len(guruh_b)
if ortacha_a > ortacha_b:
    print(f"Guruh A yaxshiroq natija ko'rsatdi (o'rtacha {ortacha_a:.1f} ball).")
elif ortacha_b > ortacha_a:
    print(f"Guruh B yaxshiroq natija ko'rsatdi (o'rtacha {ortacha_b:.1f} ball).")
else:
    print(f"Ikkala guruhning o'rtacha natijasi teng: {ortacha_a:.1f} ball.")