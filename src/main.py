from calculator import calculate


def main():
    tier: int = int(input("Enter client tier: "))
    total: int = int(input("Enter order total: "))
    result = calculate(tier=tier, total=total)
    print(f"The discounted price is: {result}")


if __name__ == "__main__":
    main()
