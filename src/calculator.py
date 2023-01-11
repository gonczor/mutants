def calculate(tier: int, total: int) -> float:
    if tier == 2:
        return total * 0.9
    elif tier == 1:
        return float(total)
    else:
        raise ValueError("Wrong client tier.")
