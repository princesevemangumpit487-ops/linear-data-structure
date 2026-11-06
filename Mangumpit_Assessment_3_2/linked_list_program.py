# Assessment 3.2 - Linked List (dynamic: works for any last name)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, ch):
        node = Node(ch)
        if self.head is None:          # empty list: node becomes head
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node            # attach at tail

    def delete_head(self):
        node = self.head
        self.head = node.next          # old node is freed by Python
        return node.data

    def view(self):
        parts, current = [], self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        return " -> ".join(parts + ["NULL"])


def main():
    name = input("Enter last name (press Enter for MANGUMPIT): ").strip().upper() or "MANGUMPIT"
    L = LinkedList()

    print("\n--- INSERT ---")
    for ch in name:
        L.append(ch)
        print(f"Inserted {ch}: {L.view()}")

    print("\n--- DELETE ---")
    removed = []
    while L.head is not None:
        ch = L.delete_head()
        removed.append(ch)
        print(f"Deleted {ch}: {L.view()}")

    print("\nRemoval order:", ", ".join(removed), "-> NULL (empty)")


if __name__ == "__main__":
    main()
