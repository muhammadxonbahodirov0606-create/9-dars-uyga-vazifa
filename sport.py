import matplotlib.pyplot as plt

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

plt.plot(
    mashgulot,
    masofa,
    color="green",
    marker="o",
    linewidth=2,
)
plt.title("Sportchining yugurish masofasi")
plt.xlabel("Mashg'ulot")
plt.ylabel("Masofa (km)")
plt.grid(True, linestyle=":")

plt.show()