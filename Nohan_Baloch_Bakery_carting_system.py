#Bakery carting system
shop = {
    "aloosamosa": 30,
    "qeemasamosa": 80,
    "pakora": 600,
    "jalebi": 450,
    "kheni": 250,
    "kalakand": 300,
    "labeshireen": 950,
    "laddu": 1100,
    "kheer": 900,
    "gulabjaman": 1250,
    "seviyan": 950,
    "sohanhalwa": 1500,
    "sujihalwa": 400
}
cart = {}
total = 0

print("Welcome to the Bakery Shop!")
while True:
    print("\nAvailable Items:")
    for item, price in shop.items():
        print(f"- {item} (${price:.2f})")

    choice = input("Enter item name (or 'q' to quit): ")
    if choice == 'Q':
        break

    if choice not in shop:
        print(f"Sorry, we don't have {choice} in our shop.")
        continue

    quantity = int(input(f"Enter quantity for {choice}: "))
    cart[choice] = cart.get(choice, 0) + quantity
    print(f"{quantity} {choice} added!")

    while True:
        cont = input("Continue shopping? (Y/N): ").upper()
        if cont in ('Y', 'N'):
            break
        print("Invalid choice. Please enter Y or N.")

    if cont == 'N':
        break

if cart:
    print("\nYour Cart:")
    for item, quantity in cart.items():
        price = shop[item]
        subtotal = price * quantity
        print(f"- {quantity} {item} (${price:.2f}) - Subtotal: ${subtotal:.2f}")
    total = sum(price * quantity for price, quantity in cart.items())
    print(f"\nTotal: ${total:.2f}\n")
    print("Thank you for shopping!")