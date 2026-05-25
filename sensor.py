def spray_control(soil_moisture):
    if soil_moisture < 50:
        return "Spray ON"
    else:
        return "Spray OFF"

print(spray_control(45))