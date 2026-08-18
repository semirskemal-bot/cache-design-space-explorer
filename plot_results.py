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

average_amats = []

for workload in workload_names:
    amats = []

    for row in results:
        if row["workload"] == workload:
            amats.append(float(row["amat"]))

    if len(amats) > 0:
        average_amat = sum(amats) / len(amats)
        average_amats.append(average_amat)
    else:
        print("No results found for:", workload)

plt.bar(workload_names, average_amats)

plt.xlabel("Memory Workload")
plt.ylabel("Average Memory Access Time (ns)")
plt.title("AMAT Across Memory Workloads")

plt.savefig("amat_comparison.png")
plt.show()