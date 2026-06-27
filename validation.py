def validate(weight, height):

    # Check empty fields
    if weight.strip() == "" or height.strip() == "":
        return False, "Weight and Height cannot be empty."

    # Check numbers
    try:
        weight = float(weight)
        height = float(height)

    except ValueError:
        return False, "Please enter numbers only."

    # Check weight
    if weight < 20 or weight > 300:
        return False, "Weight must be between 20 and 300 kg."

    # Check height
    if height < 0.5 or height > 2.5:
        return False, "Height must be between 0.5 and 2.5 meters."

    # Everything is correct
    return True, ""