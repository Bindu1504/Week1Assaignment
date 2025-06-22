# Define functions

def add_album(library, album_info):
    artist, title, year, songs = album_info
    library[title] = (artist, year, songs)
    return library


def create_playlist(library, song_selections):
    playlist = []
    for album_title, song_name in song_selections:
        if album_title in library:
            _, _, songs = library[album_title]
            if song_name in songs:
                playlist.append(song_name)
    return playlist


def add_song_to_album(library, album_title, new_song):
    if album_title in library:
        artist, year, songs = library[album_title]
        if new_song not in songs:
            songs.append(new_song)
        library[album_title] = (artist, year, songs)
    return library


def remove_song_from_playlist(playlist, song):
    if song in playlist:
        playlist.remove(song)
    return playlist


def display_library(library):
    for title, (artist, year, songs) in library.items():
        print(f"\nAlbum: {title}")
        print(f"  Artist: {artist}")
        print(f"  Year: {year}")
        print(f"  Songs: {', '.join(songs)}")


def display_playlist(playlist):
    print("\nCurrent Playlist:")
    for idx, song in enumerate(playlist, 1):
        print(f"{idx}. {song}")



library = {}
playlist = []
unique_artists = set()
unique_genres = set()


while True:
    print("\n--- Music Library Menu ---")
    print("1. Add a New Album")
    print("2. Create a Playlist")
    print("3. Add a Song to an Album")
    print("4. Remove a Song from Playlist")
    print("5. Display Music Library")
    print("6. Display Playlist")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        artist = input("Enter artist name: ")
        title = input("Enter album title: ")
        year = int(input("Enter release year: "))
        songs_input = input("Enter songs (comma separated): ")
        songs = [song.strip() for song in songs_input.split(",")]
        album_info = (artist, title, year, songs)
        library = add_album(library, album_info)
        unique_artists.add(artist)
        print("Album added successfully.")

    elif choice == '2':
        song_selections = []
        print("Enter songs for playlist (enter 'done' to finish):")
        while True:
            album_title = input("  Album Title: ")
            if album_title.lower() == 'done':
                break
            song_name = input("  Song Name: ")
            if song_name.lower() == 'done':
                break
            song_selections.append((album_title, song_name))
        playlist = create_playlist(library, song_selections)
        print("Playlist created successfully.")

    elif choice == '3':
        album_title = input("Enter album title: ")
        new_song = input("Enter new song name to add: ")
        library = add_song_to_album(library, album_title, new_song)
        print("Song added to album successfully.")

    elif choice == '4':
        song = input("Enter song name to remove from playlist: ")
        playlist = remove_song_from_playlist(playlist, song)
        print("Song removed from playlist successfully.")

    elif choice == '5':
        display_library(library)

    elif choice == '6':
        display_playlist(playlist)

    elif choice == '7':
        print("Exiting Music Library. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
