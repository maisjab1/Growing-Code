def ft_count_harvest_recursive():
    Days_until_harvest = int(input("Days until harvest:"))
    for i in range(1, Days_until_harvest + 1, 1):
        ft_counter(i, Days_until_harvest)
    print("Harvest time!")


def ft_counter(i, Days_until_harvest):
    if (i <= Days_until_harvest):
        print("Day ", i)
