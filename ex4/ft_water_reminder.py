def ft_water_reminder():
    lastWater = int(input("Days since last  watering:"))
    if (lastWater > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
