from dataclasses import dataclass

@dataclass
class LoopState:
    count: int = 0
    longest: int = 0
    previous: int = 0
    length: int = 0

    def _end_of_increasing_subarray(self, current):
        return current <= self.previous

    def _update_count(self):
        if self.length > self.longest:
            self.longest = self.length
            self.count = 1
        elif self.length == self.longest:
            self.count += 1

        self.length = 0

    def update(self, current = 0):
        if self._end_of_increasing_subarray(current):
            self._update_count()

        self.length += 1
        self.previous = current


def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    state = LoopState()

    for num in A:
        state.update(num)

    state.update()
    return state.count

