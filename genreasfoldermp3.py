import os
from mutagen.id3 import ID3

# Ścieżka do folderu z plikami mp3
folder_path = r"V:\Muzyka\"

# Przejście przez wszystkie pliki w folderze
for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        file_path = os.path.join(folder_path, filename)
        
        # Otwarcie pliku mp3 i odczytanie gatunku z ID3Tag
        audio = ID3(file_path)
        genre = audio.get("TCON")
        
        # Sprawdzenie, czy tag ID3 z gatunkiem istnieje
        if genre is not None:
            genre = genre.text[0]
            
            # Zastąpienie niedozwolonych znaków w nazwie podfolderu
            genre = genre.replace("/", "-")
            
            # Tworzenie podfolderu o nazwie gatunku, jeśli nie istnieje
            genre_folder_path = os.path.join(folder_path, genre)
            if not os.path.exists(genre_folder_path):
                os.makedirs(genre_folder_path)
            
            # Przeniesienie pliku do odpowiedniego podfolderu
            new_file_path = os.path.join(genre_folder_path, filename)
            os.rename(file_path, new_file_path)
