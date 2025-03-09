class Hotel:
    def __init__(self, name, rooms_available, location, rating, price_per_room):
        self.name = name
        self.rooms_available = rooms_available
        self.location = location
        self.rating = rating
        self.price_per_room = price_per_room

    def __repr__(self):
        return f"{self.name} | Rooms: {self.rooms_available} | Location: {self.location} | Rating: {self.rating} | Price: {self.price_per_room}"


class User:
    def __init__(self, user_name, user_id, booking_cost):
        self.user_name = user_name
        self.user_id = user_id
        self.booking_cost = booking_cost

    def __repr__(self):
        return f"{self.user_name} | UserID: {self.user_id} | Booking Cost: {self.booking_cost}"


# Initialize hotel data
hotels = [
    Hotel("H1", 4, "Bangalore", 5, 100),
    Hotel("H2", 5, "Bangalore", 5, 200),
    Hotel("H3", 6, "Mumbai", 3, 100)
]

# Initialize user data
users = [
    User("U1", 2, 1000),
    User("U2", 3, 1200),
    User("U3", 4, 1100)
]

# Function to print hotel data
def print_hotel_data(hotel_list):
    for hotel in hotel_list:
        print(hotel)

# Sort hotels by Name
def sort_hotels_by_name(hotel_list):
    return sorted(hotel_list, key=lambda x: x.name)

# Sort hotels by highest rating
def sort_hotels_by_rating(hotel_list):
    return sorted(hotel_list, key=lambda x: x.rating, reverse=True)

# Print hotel data for Bangalore Location
def filter_hotels_by_location(hotel_list, location):
    return [hotel for hotel in hotel_list if hotel.location == location]

# Sort hotels by maximum number of rooms available
def sort_hotels_by_rooms_available(hotel_list):
    return sorted(hotel_list, key=lambda x: x.rooms_available, reverse=True)

# Print user booking data
def print_user_data(user_list):
    for user in user_list:
        print(user)

# Execute the tasks
print("Hotel Data:")
print_hotel_data(hotels)

print("\nSorted Hotels by Name:")
print_hotel_data(sort_hotels_by_name(hotels))

print("\nSorted Hotels by Highest Rating:")
print_hotel_data(sort_hotels_by_rating(hotels))

print("\nHotel Data for Bangalore Location:")
print_hotel_data(filter_hotels_by_location(hotels, "Bangalore"))

print("\nSorted Hotels by Maximum Number of Rooms Available:")
print_hotel_data(sort_hotels_by_rooms_available(hotels))

print("\nUser  Booking Data:")
print_user_data(users)
