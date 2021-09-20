class Professor:
    def __init__(self, first_name, last_name, average_rating, ratings_count, would_take_again_rate):
        self.first_name = first_name
        self.last_name = last_name
        self.average_rating = average_rating
        self.ratings_count = ratings_count
        self.would_take_again_rate = would_take_again_rate

    def __repr__(self):
        return "Professor{first_name: %s, last_name: %s, average_rating: %s, ratings_count: %s, would_take_again_rate: %s}" % (
            self.first_name, self.last_name, self.average_rating, self.ratings_count, self.would_take_again_rate)
