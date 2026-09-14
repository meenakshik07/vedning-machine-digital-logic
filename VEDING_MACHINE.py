"""
Digital Beverage Vending Machine
---------------------------------
A Python simulation of a digital vending machine
that dispenses Coffee, Tea, or Milk.

Inputs:
    Beverage selection
    Money inserted

Outputs:
    Beverage dispensed
    Change returned
    Error message for insufficient money
"""

# Beverage prices
PRICES = {
    1: ("Coffee", 20),
    2: ("Tea", 15),
    3: ("Milk", 10)
}


def display_menu():
    """Display available beverages."""
    print("\n" + "=" * 40)
    print("       DIGITAL BEVERAGE VENDING MACHINE")
    print("=" * 40)
    print("1. Coffee - Rs.20")
    print("2. Tea    - Rs.15")
    print("3. Milk   - Rs.10")
    print("4. Exit")
    print("=" * 40)


def select_beverage():
    """Get and validate beverage selection."""
    while True:
        try:
            choice = int(input("Select beverage (1-4): "))

            if choice in PRICES:
                beverage, price = PRICES[choice]
                return beverage, price

            elif choice == 4:
                return None, None

            else:
                print("Invalid selection. Please choose 1, 2, or 3.")

        except ValueError:
            print("Please enter a valid number.")


def insert_money(price):
    """Accept money until sufficient amount is inserted."""
    total = 0

    print(f"\nPrice: Rs.{price}")

    while total < price:
        try:
            money = int(input("Insert money: "))

            if money <= 0:
                print("Enter a positive amount.")
                continue

            total += money

            if total < price:
                print(f"Remaining amount: Rs.{price - total}")

        except ValueError:
            print("Please enter a valid amount.")

    return total


def dispense_beverage(beverage):
    """Dispense the selected beverage."""
    print("\nProcessing...")
    print(f"✓ {beverage} selected")
    print(f"✓ {beverage} is being dispensed!")


def return_change(amount):
    """Return change to the user."""
    if amount > 0:
        print(f"✓ Change returned: Rs.{amount}")
    else:
        print("✓ No change.")


def vending_machine():
    """Main vending machine controller."""

    print("\nWelcome to the Digital Beverage Vending Machine!")

    while True:

        display_menu()

        beverage, price = select_beverage()

        if beverage is None:
            print("\nThank you for using the vending machine!")
            break

        print(f"\nSelected: {beverage}")

        money = insert_money(price)

        change = money - price

        dispense_beverage(beverage)
        return_change(change)

        print("\nTransaction completed.")


if __name__ == "__main__":
    vending_machine()