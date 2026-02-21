def ft_count_harvest_recursive():
    Days_until_harvest = int(input("Days until harvest:"))
    ft_counter(1, Days_until_harvest)
    print("Harvest time!")


def ft_counter(i, Days_until_harvest):
    if i > Days_until_harvest:
        return
    print("Day ", i)
    ft_counter(i + 1, Days_until_harvest)
