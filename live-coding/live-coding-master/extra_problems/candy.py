"""
Halloween is coming, and you need to figure out how much candy to buy.

Luckily you have tracked the weather, temperature, and number of tricker treaters from years past.

From your research you have tracked 4 different types of weather: "Clear", "Cloudy", "Raining", "Full Moon"

From your research you have tracked 4 differnt types of temperature 40s, 50s, 60s, 70s

You get 10% more trick or treaters if the weather is clear
You get 0% more trick or treaters if the weather is cloudy
You get 25% less trick or treaters if the weather is rainy
You get 25% more trick or treaters if the weather is Full Moon

You get more trick or treaters the warmer the weather
You get 5% less trick or treaters if it's in the 40s
You get 0% more trick or treaters if it's in the 50s
You get 5% more trick or treaters if it's in the 60s
You get 20% more trick or treaters if its' in the 70s

On average you get 250 trick or treaters, and you want to give each kid 3 pieces of candy.

How much candy do you need to buy if it's clear, and in the 50s?
825

How much candy do you need to buy if it's a full moon, and in the 40s?
900

How much candy do you need to buy if it's raining, and in the 70s?
712.5

"""

def how_much_candy(weather, temperature, base):
    trick_or_treaters = base
    if weather == "clear":
        trick_or_treaters += base * .1
    elif weather == "cloudy":
        pass
    elif weather == "rainy":
        trick_or_treaters -= base * .25
    elif weather == "full moon":
        trick_or_treaters += base * .25

    if temperature == "40s":
        trick_or_treaters -= base * .05
    elif temperature == "50s":
        pass
    elif temperature == "60s":
        trick_or_treaters += base * .05
    elif temperature == "70s":
        trick_or_treaters += base * .20


    candy = trick_or_treaters * 3
    return candy


print(how_much_candy("clear", "50s", 250))
print(how_much_candy("full moon", "40s", 250))
print(how_much_candy("rainy", "70s", 250))




    