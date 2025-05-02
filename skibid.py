import matplotlib.pyplot as plt

# Immigration data by region (approximate numbers in millions for illustrative purposes)
decades = [
    "1820s", "1830s", "1840s", "1850s", "1860s", "1870s", "1880s", "1890s", "1900s"
]

# Approximate immigration numbers by region (in millions)
northern_western_europe = [0.1, 0.5, 1.5, 2.6, 1.3, 1.9, 3.2, 2.5, 1.8]
southern_eastern_europe = [0, 0, 0, 0.1, 0.2, 0.4, 1.0, 1.8, 2.5]

plt.figure(figsize=(12, 6))
plt.plot(decades, northern_western_europe, marker='o', label='Northern & Western Europe')
plt.plot(decades, southern_eastern_europe, marker='o', label='Southern & Eastern Europe')

plt.title("U.S. Immigration by European Region (19th Century to Early 20th)")
plt.xlabel("Decade")
plt.ylabel("Immigrants (Millions)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
