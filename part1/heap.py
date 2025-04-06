from random import randrange
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, process):
        if len(process) != 3:
            return print("Invalid input")
        print(f"Adding {process}")
        self.heap.append(process)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index]["priority"] < self.heap[parent_index]["priority"]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def insert_queue(self, queue):
        for process in queue:
            self.insert(process)

    def show(self):
        print("Priority queue:")
        for process in self.heap:
            print(process)
        
    def update(self, element, new_priority):
        for i in self.heap:
            if element == i["process"]:
                old = i["priority"]
                i["priority"] = new_priority
                print(f"Process {element} updated. Old priority: {old} New: {i["priority"]}")
                return
        print("Process not found")

    def pop(self):
        if len(self.heap) == 0:
            print("There is nothing to remove")
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        print(f"Root {root} removed")
        return root

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < len(self.heap) and self.heap[left_child]["priority"] < self.heap[smallest]["priority"]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child]["priority"] < self.heap[smallest]["priority"]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def show_root(self):
        print(f"The root is {self.heap[0]}")

if __name__ == "__main__":
    queue = [
        {"priority": 5, "process": "Process 1", "execution_time": 4},
        {"priority": 2, "process": "Process 2", "execution_time": 3},
        {"priority": 3, "process": "Process 3", "execution_time": 2},
        {"priority": 7, "process": "Process 4", "execution_time": 1},
        {"priority": 1, "process": "Process 5", "execution_time": 6},
    ]

    heap = MinHeap()
    heap.insert_queue(queue)
    heap.show()
    heap.update("Process 3", 4)
    heap.pop()
    heap.insert({"priority": 1, "process": "Process 8", "execution_time": 4})
    heap.show()
  