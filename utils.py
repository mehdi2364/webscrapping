def get_word_in_parenthesis(input_string):
    # Find the position of the opening and closing curly braces
    start_index = input_string.find("(") + 1
    end_index = input_string.find(")")

    # Extract the word between the curly braces
    if start_index != 0 and end_index != -1 and start_index < end_index:
        word_in_braces = input_string[start_index:end_index].strip()
        return word_in_braces
    else:
        return None

def get_class_aqi(aqi):
    if 0 <= aqi <= 50:
        return "Good"
    elif 51 <= aqi <= 100:
        return "Moderate"
    elif 101 <= aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif 151 <= aqi <= 200:
        return "Unhealthy"
    elif 201 <= aqi <= 300:
        return "Very Unhealthy"
    elif 301 <= aqi <= 500:
        return "Hazardous"
    else:
        return "Invalid AQI value"
