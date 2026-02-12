def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    x1 = "available"
    x2 = "total"
    x3 = "meters"
    if (unit == "packets"):
        x = x1
    elif (unit == "grams"):
        x = x2
    elif (unit == "area"):
        x = x3
    else:
        x = "Unknown unit type"
    print(seed_type, " seeds: ", quantity, unit, x)
