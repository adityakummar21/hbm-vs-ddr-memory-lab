# 🧠 The Memory Wall: HBM vs DDR Memory Lab
A systems-focused project exploring the “memory wall” problem by simulating and visualizing the differences between DDR5 and HBM3E memory architectures using Python benchmarks and hardware-based LED demonstrations.


## Quick Comparison

- **DDR5:** Traditional system memory with narrower bus widths optimized for general-purpose computing.
- **HBM3E:** Stacked high-bandwidth memory using extremely wide buses designed for AI and data-center workloads.

## Memory Wall
The memory wall is the growing gap between how fast processors can compute and how fast memory can deliver data

Modern CPUs and GPUs can process data extremely quickly, but many workloads become bottlenecked by how fast memory can deliver data to the processor. This is especially important in AI workloads, where large tensors and matrices must be moved constantly.

This project compares DDR5 and HBM3E memory architectures through software simulation and visual demonstrations. The goal is to show how memory bandwidth, latency, and bus width affect performance in data-heavy workloads.


## Project Goal

The goal of this project is not to perfectly model real hardware, but to build an educational simulation that explains why high-bandwidth memory is important for modern AI systems.

## Planned Features

- Python bandwidth and latency simulator
- Memory transfer benchmarking
- DDR5 vs HBM3E workload comparisons
- Interactive data visualizations
- Physical LED matrix bus-width demonstration
- AI workload simulation experiments
