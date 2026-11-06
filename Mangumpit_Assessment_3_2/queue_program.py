# Assessment 3.2 - Queue (FIFO) (dynamic: works for any last name)

class Queue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0          # next free position

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, ch):
        self.items[self.rear] = ch
        self.rear += 1

    def dequeue(self):
        ch = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        return ch

    def view(self):
        return self.items[self.front : self.rear]


def main():
    name = input("Enter last name (press Enter for MANGUMPIT): ").strip().upper() or "MANGUMPIT"
    Q = Queue(len(name))

    print("\n--- ENQUEUE ---")
    for ch in name:
        Q.enqueue(ch)
        print(f"Enqueued {ch}: {Q.view()} (front -> rear)")

    print("\n--- DEQUEUE ---")
    removed = []
    while not Q.is_empty():
        ch = Q.dequeue()
        removed.append(ch)
        print(f"Dequeued {ch}: {Q.view()}")

    print("\nDequeue order:", ", ".join(removed), "-> empty (first in, first out)")


if __name__ == "__main__":
    main()
