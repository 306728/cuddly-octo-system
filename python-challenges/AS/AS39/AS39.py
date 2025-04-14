import random

def generate_playlist(num_artists, num_songs):
    # 2D list
    songs = []
    for artist in range(num_artists):
        artist_songs = []
        for i in range(num_songs):
            song_name = "A" + str(artist+1) + "_S" + str(i+1)
            artist_songs.append(song_name)
        songs.append(artist_songs)
    
    print("2D List")
    print(songs)

    # Single list for shuffling
    all_songs = []
    
    for sublist in songs:
        for song in sublist:
            all_songs.append(song)

    """
    Add 2 songs with different artists to the new list
    When adding a new song to this new list, ensure they the artists are different from
    those of the last and second last songs in the new list
    """
    
    # First random song
    new_list = [] 
    rand_song1 = random.choice(all_songs)
    rand_song1_artist = rand_song1.split("_")[0]
    new_list.append(rand_song1)
    all_songs.remove(rand_song1)
    
    # Second random song
    rand_song2 = random.choice(all_songs)
    rand_song2_artist = rand_song2.split("_")[0]
    
    # Ensure that the first 2 songs have different artists
    while rand_song1_artist == rand_song2_artist:
        rand_song2 = random.choice(all_songs)
        rand_song2_artist = rand_song2.split("_")[0]
        
    new_list.append(rand_song2)
    all_songs.remove(rand_song2)
    
    
    while len(all_songs) >= 1:
        prev_artist1 = new_list[-1].split("_")[0]   # Artist of the last song in the new list
        prev_artist2 = new_list[-2].split("_")[0]   # Artist of the second last song in the new list
        
        next_song = random.choice(all_songs)
        next_song_artist = next_song.split("_")[0]
        
        while (next_song_artist == prev_artist1) or (next_song_artist == prev_artist2):
            next_song = random.choice(all_songs)
            next_song_artist = next_song.split("_")[0]
            
        new_list.append(next_song)
        all_songs.remove(next_song)

    return new_list


num_artists = 10 
num_songs = 10  

playlist = generate_playlist(num_artists, num_songs)
print("\nShuffled Playlist:")

for index, song in enumerate(playlist):
    print(str(index + 1) + ": " + song)
