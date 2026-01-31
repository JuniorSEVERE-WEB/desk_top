"""Simple calculator (CLI) with exception handling.

Learning goals:
- Functions
- Loops
- `match` for menu choices
- try/except (ValueError, ZeroDivisionError)
"""


def read_number(prompt: str) -> float:
    """Read a number from the user (float). Re-asks until valid."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("❌ Please type a valid number (example: 12 or 12.5).")


def read_operation() -> str:
    """Read an operation choice from the user."""
    print("\n=== Calculator ===")
    print("1) Add (+)")
    print("2) Subtract (-)")
    print("3) Multiply (*)")
    print("4) Divide (/)")
    print("5) Power (**) ")
    print("0) Quit")
    return input("Choose an option: ").strip()


def compute(a: float, b: float, op: str) -> float:
    match op:
        case "1" | "+":
            return a + b
        case "2" | "-":
            return a - b
        case "3" | "*" | "x" | "X":
            return a * b
        case "4" | "/":
            return a / b
        case "5" | "**" | "^":
            return a**b
        case _:
            raise ValueError("Unknown operation")


def main() -> None:
    while True:
        op = read_operation()

        if op in {"0", "q", "Q", "quit", "exit"}:
            print("Bye!")
            return

        a = read_number("First number: ")
        b = read_number("Second number: ")

        try:
            result = compute(a, b, op)
        except ZeroDivisionError:
            print("❌ Division by zero is not allowed.")
            continue
        except ValueError:
            print("❌ Invalid choice. Please pick 0-5 (or + - * / **).")
            continue

        print(f"✅ Result: {result}")


if __name__ == "__main__":
    main()