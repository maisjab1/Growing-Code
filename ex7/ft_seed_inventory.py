def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    x1 = "available"
    x2 = "total"
    x3 = "square meters"
    if (unit == "packets"):
        x = x1
        print(seed_type, " seeds: ", quantity, unit, x)
    elif (unit == "grams"):
        x = x2
        print(seed_type, " seeds: ", quantity, unit, x)
    elif (unit == "area"):
        x = x3
        print(seed_type, " seeds: covers ", quantity, x)
    else:
        print("Unknown unit type")
