# Cache Design-Space Explorer

A CPU cache simulator written in Python to explore how **cache size**, **block size**, **associativity**, and **memory access patterns** affect cache hit rate.

## What It Does

The simulator models a set-associative cache using an **LRU replacement policy**.

For each memory address, it determines the block number, set index, and tag, then decides whether the access results in a cache hit or miss.

## Experiments

The design space includes:

* Cache sizes: 1 KB, 2 KB, 4 KB
* Block sizes: 16 B, 32 B, 64 B
* Associativity: 1-way, 2-way, 4-way

Four synthetic workloads are tested:

* Sequential
* Repeated
* Random
* Conflict-intensive

This produces **108 cache/workload combinations**.

## Results

Results are written to `results.csv` and visualized using Matplotlib.

Key observations:

* Larger blocks improve sequential workloads through spatial locality.
* Repeated accesses benefit from temporal locality.
* Higher associativity reduces conflict misses.
* Random access patterns generally produce weaker cache performance.

## Run

```bash
python main.py
python plot_results.py
```

## Files

* `cache.py` — cache model and LRU replacement
* `workloads.py` — memory trace generators
* `experiment.py` — experiment runner and CSV export
* `plot_results.py` — result visualization
* `main.py` — design-space exploration driver
