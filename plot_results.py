import csv
import matplotlib.pyplot as plt

results = []

with open("results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        results.append(row)

workload_names = [
    "sequential",
    "repeated",
    "random",
    "conflict"
]

average_hit_rates = []

for workload in workload_names:
    rates = []

    for row in results:
        if row["workload"] == workload:
            rates.append(float(row["hit_rate"]))

    average = sum(rates) / len(rates)
    average_hit_rates.append(average)

plt.bar(workload_names, average_hit_rates)

plt.xlabel("Memory Workload")
plt.ylabel("Average Hit Rate")
plt.title("Cache Performance Across Memory Access Patterns")
plt.ylim(0, 1)

plt.savefig("workload_comparison.png")
plt.show()