class Movie:
    def __init__(self, title, duration, rating):
        self.title = title
        self.duration = duration
        self.rating = rating
    
class Screening:
    def __init__(self, movie: Movie, screening_time, avaible_seats):
        self.movie = movie
        self.screening_time = screening_time
        self.avaible_seats = avaible_seats
        self.reserved_seat = 0
    
    def reserve_seat(self, num_seats):
        if num_seats > self.avaible_seats:
            print(f"Sorry. We have only {self.avaible_seats}")
        elif num_seats <= 0:
            print("Seats number must be greater than 0!")
        else:
            self.avaible_seats -= num_seats
            self.reserved_seat += num_seats
            print (f"Excellent! You have reserved {num_seats} seats.")
    
    def cancel_reservation(self, num_seats):
        if num_seats > self.reserved_seat:
            print("Wrong seats number to cancel reservation!")
        elif num_seats <= 0:
            print("Seats number must be greater than 0!")
        else:
            self.reserved_seat -= num_seats
            self.avaible_seats += num_seats
            print("You have successfully canceled the reservation.")
            


movie1 = Movie("Inception", 148, 8.8)  # Tytuł, czas trwania, ocena
movie2 = Movie("The Matrix", 136, 8.7)
movie3 = Movie("Interstellar", 169, 8.6)
screening1 = Screening(movie1, "18:00", 100)  # Film, godzina seansu, liczba miejsc
screening2 = Screening(movie2, "20:30", 80)
screening3 = Screening(movie3, "15:45", 120)
screening1.reserve_seat(15)
screening1.cancel_reservation(10)
screening1.cancel_reservation(100)
print(screening1.avaible_seats)
