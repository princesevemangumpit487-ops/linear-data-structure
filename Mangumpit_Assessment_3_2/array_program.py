# Assessment 3.2 - Array (dynamic: works for any last name)

def main():
    name = input("Enter last name (press Enter for MANGUMPIT): ").strip().upper() or "MANGUMPIT"

    A = [None] * len(name)   # array sized to the name
    count = 0

    print("\n--- ADD ---")
    for ch in name:
        A[count] = ch
        count += 1
        print(f"Added {ch}: {A}")

    print("\n--- REMOVE ---")
    removed = []
    while count > 0:
        count -= 1
        ch = A[count]
        removed.append(ch)
        A[count] = None
        print(f"Removed {ch}: {A}")

    print("\nAfter adding : [" + ", ".join(name) + "]")
    print("Removal order:", ", ".join(removed), "-> [ ] (empty)")


if __name__ == "__main__":
    main()
