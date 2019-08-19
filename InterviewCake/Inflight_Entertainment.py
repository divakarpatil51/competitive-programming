# Write a function that takes an integer flight_length (in minutes) and a list of integers
# movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers
# in movie_lengths whose sum equals flight_length.


def inflight_entertainment(flight_length, movie_lengths):
    size = len(movie_lengths)
    if not size or size < 2:
        return False

    if size == 2:
        return flight_length == movie_lengths[0] + movie_lengths[1]

    watched_movie = []
    for first_movie_length in movie_lengths:

        second_movie_length = flight_length - first_movie_length
        if second_movie_length in watched_movie:
            return True
        watched_movie.append(first_movie_length)

    return False


if __name__ == "__main__":
    print(inflight_entertainment(120, [10, 10, 60, 70, 10]))
