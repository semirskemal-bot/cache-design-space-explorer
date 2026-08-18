class Cache:
    def __init__(self, cache_size, block_size, associativity):
        self.cache_size = cache_size
        self.block_size = block_size
        self.associativity = associativity
        self.hits = 0
        self.misses = 0

        self.num_sets = cache_size // (block_size * associativity)
        self.sets = [[] for _ in range(self.num_sets)]

    def print_config(self):
        print("Cache Size:", self.cache_size)
        print("Block Size:", self.block_size)
        print("Associativity:", self.associativity)
        print("Number of Sets:", self.num_sets)
    
    def get_location(self, address):
        block_number = address // self.block_size
        set_index = block_number % self.num_sets
        tag = block_number // self.num_sets

        return block_number, set_index, tag


    def access(self, address):
        block_number, set_index, tag = self.get_location(address)

        if tag in self.sets[set_index]:
            self.hits += 1
            self.sets[set_index].remove(tag)
            self.sets[set_index].append(tag)
            return "HIT"
        else:
            self.misses += 1
            if len(self.sets[set_index]) >= self.associativity:
                self.sets[set_index].pop(0)
            self.sets[set_index].append(tag)
            return "MISS"
    
    def get_hit_rate(self):
        total_accesses = self.hits+self.misses

        if total_accesses == 0:
            return 0

        return self.hits/total_accesses

    def get_miss_rate(self):
        total_accesses = self.hits+self.misses

        if total_accesses == 0:
            return 0

        return self.misses / total_accesses
        