from pathlib import Path

import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

eng_yuqori_index = ballar.index(max(ballar))
eng_past_index = ballar.index(min(ballar))
ortacha_ballar = sum(ballar) / len(ballar)

ranglar = ["skyblue"] * len(ismlar)
ranglar[eng_yuqori_index] = "green"
ranglar[eng_past_index] = "red"

ustunlar = plt.bar(ismlar, ballar, color=ranglar)
for ustun, ball in zip(ustunlar, ballar):
    plt.text(
        ustun.get_x() + ustun.get_width() / 2,
        ustun.get_height(),
        f"{ball}%",
        ha="center",
        va="bottom",
    )

plt.axhline(ortacha_ballar, color="orange", linestyle="--", label=f"O'rtacha: {ortacha_ballar:.1f}")
plt.title("O'quvchilar natijalari")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar (%)")
plt.grid(axis="y")
plt.ylim(0, 110)
plt.legend()
plt.tight_layout()

papka = Path(__file__).parent
plt.savefig(papka / "oquvchilar_natijasi.png")
plt.show()

tahlil = [
    f"Eng yuqori ball: {ismlar[eng_yuqori_index]} — {ballar[eng_yuqori_index]} ball.",
    f"Eng past ball: {ismlar[eng_past_index]} — {ballar[eng_past_index]} ball.",
    f"O'quvchilarning o'rtacha bali: {ortacha_ballar:.1f}.",
]

hisobot = "O'quvchilar tahlili\n\n" + "\n".join(
    f"{raqam}. {gap}" for raqam, gap in enumerate(tahlil, start=1)
)
(papka / "oquvchilar_tahlili.txt").write_text(hisobot, encoding="utf-8")

print(hisobot)