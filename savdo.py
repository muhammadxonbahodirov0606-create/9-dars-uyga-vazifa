import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

eng_kop_index = sotuv.index(max(sotuv))
eng_kam_index = sotuv.index(min(sotuv))

ranglar = ["steelblue"] * len(mahsulotlar)
ranglar[eng_kop_index] = "green"
ranglar[eng_kam_index] = "red"

ustunlar = plt.bar(mahsulotlar, sotuv, color=ranglar)
umumiy_sotuv = sum(sotuv)
for ustun, soni in zip(ustunlar, sotuv):
    foiz = soni / umumiy_sotuv * 100
    plt.text(
        ustun.get_x() + ustun.get_width() / 2,
        ustun.get_height(),
        f"{foiz:.1f}%",
        ha="center",
        va="bottom",
    )

plt.title("Do'konda bir haftada sotilgan mahsulotlar")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotilgan soni")
plt.ylim(0, max(sotuv) * 1.15)
plt.savefig("savdo_diagrammasi.png")
plt.show()

print(f"Eng ko'p sotilgan: {mahsulotlar[eng_kop_index]} ({sotuv[eng_kop_index]} ta)")
print(f"Eng kam sotilgan: {mahsulotlar[eng_kam_index]} ({sotuv[eng_kam_index]} ta)")