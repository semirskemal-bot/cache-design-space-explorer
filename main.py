from workloads import (
    sequential_workload,
    repeated_workload,
    random_workload,
    conflict_workload
)

from experiment import run_experiment, save_results

addresses = sequential_workload(1000)

cache_sizes = [1024, 2048, 4096]
block_sizes = [16, 32, 64]
associativities = [1, 2, 4]

workloads = {
    "sequential": sequential_workload(1000),
    "repeated": repeated_workload(1000),
    "random": random_workload(1000),
    "conflict": conflict_workload(1000, 1024)
}
results = []


for workload_name, addresses in workloads.items():
    for cache_size in cache_sizes:
        for block_size in block_sizes:
            for associativity in associativities:
                result = run_experiment(
                    addresses,
                    cache_size,
                    block_size,
                    associativity,
                    workload_name
                )

                results.append(result)
save_results(results, "results.csv")


