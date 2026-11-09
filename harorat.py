from matplotlib import pyplot

kunlar = ["9.11", "10.11", "11.11", "12.11", "13.11", "14.11", "15.11"]
Fergana = [19, 18, 11, 11, 8, 10, 12]

pyplot.plot(kunlar, Fergana, marker="o", linestyle="-.", color="red", label="Fergana")

pyplot.legend()


pyplot.title("Fergana ℃")
pyplot.xlabel("Kunlar")
pyplot.ylabel("Haroratlar (℃)")

pyplot.grid(True)

pyplot.savefig("haroratlar.png")   
pyplot.show()