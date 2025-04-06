class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, package):
        if len(package) != 2:
            return print("Invalid input")
        print(f"Adding {package}")
        self.heap.append(package)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index]["priority"] < self.heap[parent_index]["priority"]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def insert_queue(self, queue):
        for package in queue:
            self.insert(package)

    def show(self):
        print("Priority queue:")
        for package in self.heap:
            print(package)
        
    def update(self, element, new_priority):
        for i in self.heap:
            if element == i["package"]:
                old = i["priority"]
                i["priority"] = new_priority
                print(f"Package {element} updated. Old priority: {old} New: {i["priority"]}")
                return
        print("Package not found")

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
        {"priority": 5, "package": "Package 1"},
        {"priority": 2, "package": "Package 2"},
        {"priority": 3, "package": "Package 3"},
        {"priority": 7, "package": "Package 4"},
        {"priority": 4, "package": "Package 5"},
    ]

    heap = MinHeap()
    heap.insert_queue(queue)
    heap.show()
    heap.update("Package 3", 2)
    heap.pop()
    heap.show()
  