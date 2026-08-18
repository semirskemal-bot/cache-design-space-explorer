import random

def strided_workload(count, stride):
    addresses = []
    for i in range(count):
        addresses.append(i*stride)
    return addresses
import random


def sequential_workload(count, stride=4):
    addresses = []

    for i in range(count):
        addresses.append(i * stride)

    return addresses


def repeated_workload(count):
    addresses = []
    hot_addresses = [0, 4, 8, 12]

    for i in range(count):
        addresses.append(hot_addresses[i % len(hot_addresses)])

    return addresses


def random_workload(count, max_address=4096):
    addresses = []

    for _ in range(count):
        address = random.randrange(0, max_address, 4)
        addresses.append(address)

    return addresses


def conflict_workload(count, spacing):
    addresses = []

    for i in range(count):
        addresses.append((i % 4) * spacing)

    return addresses