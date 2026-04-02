def resistor_label(colors):

    color_code = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6,
        "violet": 7, "grey": 8, "white": 9
    }

    tolerance = {
        "grey": "0.05%", "violet": "0.1%", "blue": "0.25%",
        "green": "0.5%", "brown": "1%", "red": "2%",
        "gold": "5%", "silver": "10%"
    }

    # one band resistor
    if len(colors) == 1:
        return "0 ohms"

    # four band
    if len(colors) == 4:
        value = (color_code[colors[0]] * 10 + color_code[colors[1]]) * (10 ** color_code[colors[2]])
        tol = tolerance[colors[3]]

    # five band
    else:
        value = (
            color_code[colors[0]] * 100
            + color_code[colors[1]] * 10
            + color_code[colors[2]]
        ) * (10 ** color_code[colors[3]])
        tol = tolerance[colors[4]]

    if value >= 1_000_000:
        value = value / 1_000_000
        unit = "megaohms"
    elif value >= 1000:
        value = value / 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    value = int(value) if value == int(value) else value

    return f"{value} {unit} ±{tol}"