import matplotlib.pyplot as plt

tillar = ["Python", "C", "JavaScript", "Java"]
oquvchilar = [15, 8, 12, 5]

ajratish = [0.1, 0, 0, 0]
plt.pie(oquvchilar, labels=tillar, autopct="%1.1f%%", explode=ajratish)
plt.title("Sinf o'quvchilarining sevimli dasturlash tillari")
plt.axis("equal")

plt.show()