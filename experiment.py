from cache import Cache
import csv


def save_results(results, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "workload",
                "cache_size",
                "block_size",
                "associativity",
                "hits",
                "misses",
                "hit_rate",
                "amat"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

def run_experiment(addresses, cache_size, block_size, associativity, workload_name):

    cache = Cache(cache_size, block_size, associativity)

    for address in addresses:
        cache.access(address)

    return {
        "cache_size": cache_size,
        "block_size": block_size,
        "associativity": associativity,
        "hits": cache.hits,
        "misses": cache.misses,
        "hit_rate": cache.get_hit_rate(),
        "workload": workload_name,
        "amat": cache.get_amat()
    }