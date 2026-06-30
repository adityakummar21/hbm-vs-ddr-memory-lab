# Memory Wall Simulator v0.1
# Goal: compare theoretical transfer time for DDR5 vs HBM3E

def transfer_time(payload_gb, bandwidth_gb_per_sec, latency_ns):
  """
    payload_gb: amount of data being moved in gigabyte
    bandwidth_gb_per_sec: how many gigabytes the memory can move per second
    latency_ns: delay before transfer starts, measured in nano seconds

  """
  latency_seconds = latency_ns / 1_000_000_000
  transfer_seconds = payload_gb/bandwidth_gb_per_sec

  total_time = latency_seconds + transfer_seconds
  return total_time

# Example memory specs
ddr5_bandwidth = 80      # GB/s, approximate high-end DDR5 system memory
hbm3e_bandwidth = 1200   # GB/s, approximate HBM3E stack bandwidth

ddr5_latency = 80        # ns, rough example latency
hbm3e_latency = 20       # ns, rough example latency

payload_sizes = [0.001, 0.1, 1, 10, 100]


print("Memory Wall Simulator Version 0.2")
print("----------------------------------")

for payload in payload_sizes:
  ddr5_time = transfer_time(payload, ddr5_bandwidth, ddr5_latency)
  hbm3e_time = transfer_time(payload, hbm3e_bandwidth, hbm3e_latency)

  print(payload, ddr5_time, hbm3e_time)



