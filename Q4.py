# Create a list of 3 strings with some best movies
movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]

# Insert a movie at the end of the list
movies.append("Pulp Fiction")

# Insert a movie at the beginning of the list
movies.insert(0, "Inception")

# Print the length of the list
print("Length of the list:", len(movies))

# ---------------------------------------------------------------------
import random

# Generate a list of 10 random integers
random_integers = [random.randint(1, 100) for _ in range(10)]

# Print the list of random integers
print("List of random integers:", random_integers)

# -------------------------------------------------------------------
# Generate a list of 10 random boolean values
random_bools = [random.choice([True, False]) for _ in range(10)]

# Print the list of random boolean values
print("List of random boolean values:", random_bools)

