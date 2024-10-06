class Music:
    def play(self):
        pass


class Song(Music):
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

    def play(self):
        print(f"Грає пісня: {self.name} від {self.artist}")

    def show_by_artist(self, artist):
        if self.artist == artist:
            print(f"Пісня: {self.name}, Виконавець: {self.artist}")


class Playlist(Music):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: Music):
        self.children.append(component)

    def play(self):
        print(f"\nГрає плейлист: {self.name}")
        for child in self.children:
            child.play()

    def show_by_artist(self, artist):
        for child in self.children:
            child.show_by_artist(artist)


main_playlist = Playlist("Усі пісні")
playlist1 = Playlist("Улюблене")
playlist2 = Playlist("Для ігор")

main_playlist.add(playlist1)
main_playlist.add(playlist2)

song1 = Song("Room", "IVOXYGEN")
song2 = Song("casino123", "IVOXYGEN")
song3 = Song("I need U", "NOIXES")
song4 = Song("Internet love", "IVOXYGEN")

playlist1.add(song1)
playlist1.add(song2)

playlist2.add(song3)
playlist2.add(song4)

print('\nПісні виконавця "IVOXYGEN" в усіх плейлистах:')
main_playlist.show_by_artist("IVOXYGEN")

print('\nПісні виконавця "IVOXYGEN" в плейлисті "Для ігор" :')
playlist2.show_by_artist("IVOXYGEN")

main_playlist.play()
