from dataclasses import dataclass
from typing import List
from time import time

@dataclass
class Data:
    a: int
    b: int

    @classmethod
    def new(cls, x: int) -> 'Data':
        return cls(a=x // 2, b=x // (x % 2 + 1))

def main():
    start_time = time()
    #
    vec = [Data.new(i) for i in range(500_000)]
    #
    end_time = time()
    elapsed_time = (end_time - start_time) * 1_000_000  # Convert seconds to microseconds
    print(elapsed_time)

if __name__ == "__main__":
    main()