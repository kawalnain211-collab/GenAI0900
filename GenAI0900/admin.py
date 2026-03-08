def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Please enter a number >= 1")
        except ValueError:
            print("Please enter a valid integer")


def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Please enter something")


def main():
    data = [
        {"name": "Forrest Gump", "year": 1994,
            "duration": 142, "genres": ["Drama", "Romance"]},
        {"name": "Avengers: Endgame", "year": 2019, "duration": 181,
            "genres": ["Action", "Adventure", "Drama"]},
        {"name": "Back to the Future", "year": 1985, "duration": 114,
            "genres": ["Adventure", "Comedy", "Sci-Fi"]}
    ]

    print("Welcome to the Movie Admin Program!")

    while True:
        print("\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
        choice = input("> ").lower()

        if choice == "a":
            name = input_something("Enter movie name: ")
            year = input_int("Enter release year: ")
            duration = input_int("Enter duration (minutes): ")

            genres = []
            while True:
                genre = input_something(
                    "Enter a genre (or type 'done' when finished): ")
                if genre.lower() == "done":
                    if len(genres) >= 1:
                        break
                    else:
                        print("You must enter at least one genre.")
                else:
                    genres.append(genre)

            movie = {
                "name": name,
                "year": year,
                "duration": duration,
                "genres": genres
            }
            data.append(movie)
            print(f"Movie '{name}' added successfully!")

        elif choice == "l":
            if not data:
                print("No movies saved")
            else:
                for i, movie in enumerate(data, start=1):
                    print(f"{i}) {movie['name']} ({movie['year']})")

        elif choice == "s":
            if not data:
                print("No movies saved")
            else:
                search_term = input_something("Enter search term: ").lower()
                found = False
                for i, movie in enumerate(data, start=1):
                    if search_term in movie["name"].lower():
                        print(f"{i}) {movie['name']} ({movie['year']})")
                        found = True
                if not found:
                    print("No results found")

        elif choice == "v":
            if not data:
                print("No movies saved")
            else:
                index = input_int("Enter movie index: ")
                if 1 <= index <= len(data):
                    movie = data[index - 1]
                    genres = ", ".join(movie["genres"])
                    print(f"\nName: {movie['name']}")
                    print(f"Year: {movie['year']}")
                    print(f"Duration: {movie['duration']} minutes")
                    print(f"Genres: {genres}")
                else:
                    print("Invalid index number")

        elif choice == "d":
            if not data:
                print("No movies saved")
            else:
                index = input_int("Enter movie index to delete: ")
                if 1 <= index <= len(data):
                    removed = data.pop(index - 1)
                    print(f"Movie '{removed['name']}' deleted.")
                else:
                    print("Invalid index number")

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
