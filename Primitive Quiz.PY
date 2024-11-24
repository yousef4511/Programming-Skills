def quiz():
    #dictionary of countries and their capitals
    capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Netherlands": "Amsterdam",
        "Belgiumt": "Brussels",
        "Sweden": "Stockholm",
        "Norway": "Oslo",
        "Finland": "Helsinki",
        "Austria": "Vienna"
    }

    for country, capital in capitals.items():
        answer = input(f"what is the capital of {country}?")

        if answer.lower() == capital.low():
            print("correct!")
        else:
            print(f"wrong! The correct answer is {capital}.")
quiz()
