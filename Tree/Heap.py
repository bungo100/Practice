import sys


class MiniHeap:

    def __init__(self):
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0

    def parent_index(self, index):
        return index // 2

    def left_child_index(self, index):
        return index * 2

    def right_child_index(self, index):
        return index * 2 + 1

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapfy_up(self, index):
        while self.parent_index(index) > 0:
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def min_child(self, index):
        if self.right_child_index(index) > self.current_size:
            return self.left_child_index(index)
        else:
            if (self.heap[self.left_child_index(index)] <
                self.heap[self.right_child_index(index)]):
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)

    def heapfy_down(self, index):
        while self.left_child_index(index) <= self.current_size:
            min_child_index = self.min_child(index)
            if self.heap[index] > self.heap[min_child_index]:
                self.swap(index, min_child_index)
            index = min_child_index



    def push(self, value):
        self.heap.append(value)
        self.current_size += 1
        self.heapfy_up(self.current_size)

    def pop(self):
        if len(self.heap) == 1:
            return

        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.current_size -= 1
        self.heapfy_down(1)
        return root



if __name__ == "__main__":
    min_heap = MiniHeap()
    min_heap.push(5)
    min_heap.push(6)
    min_heap.push(2)
    min_heap.push(9)
    min_heap.push(13)
    min_heap.push(11)
    min_heap.push(1)
    print(min_heap.heap)
    print(min_heap.pop())
    print(min_heap.heap)