# Assign: 12
# Q. 4)

""" Create two lists to store cities and locations by accepting values from user.
Display 1st city and 1st location
then 2nd city and 2nd location ....... (zip function)"""



num = int(input("Enter the number of cities: "))

cities = []
locations = []

# Accept cities and locations from the user
for i in range(num):
    city = input(f"Enter city {i + 1}: ")
    location = input(f"Enter location for {city}: ")
    cities.append(city)
    locations.append(location)

# Display each city with its location
print("\nCities and Locations: ")
print()
for city, location in zip(cities, locations):
    print(f"{city}: {location}")
