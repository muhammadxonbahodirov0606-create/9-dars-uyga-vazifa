import matplotlib.pyplot as plt 

fanlar = ["Matematika", "Python", "Ingliz tili", "Fizika", "Tarix"]
ballar = [85, 95, 72, 80, 88]

plt.bar(fanlar, ballar)
plt.title("Fanlardan olingan ballar")
plt.ylabel("Ballar")
plt.show()