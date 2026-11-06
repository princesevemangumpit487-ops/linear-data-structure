# Assessment 3.2 - Stack (LIFO) (dynamic: works for any last name)

class Stack:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, ch):
        self.top += 1
        self.items[self.top] = ch

    def pop(self):
        ch = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return ch

    def view(self):
        return self.items[: self.top + 1]


def main():
    name = input("Enter last name (press Enter for MANGUMPIT): ").strip().upper() or "MANGUMPIT"
    S = Stack(len(name))

    print("\n--- PUSH ---")
    for ch in name:
        S.push(ch)
        print(f"Pushed {ch}: {S.view()} (bottom -> top)")

    print("\n--- POP ---")
    popped = []
    while not S.is_empty():
        ch = S.pop()
        popped.append(ch)
        print(f"Popped {ch}: {S.view()}")

    print("\nPop order:", ", ".join(popped), "-> empty (last in, first out)")


if __name__ == "__main__":
    main()
