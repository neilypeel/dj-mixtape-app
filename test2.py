




print('\n\nhello, here is a list of genres from playlist to choose\n\n')

the_records = [1, 2, 3, 4, 5, 6, 7]
artist = ['moodymann', 'sheila e', 'awesome dre','james black', 'amajika', 'can', 'anthony shakir', 'mark stewart', 'ron hardy', 'fred wesley', 'model 500', 'neneh cherry']
genres = ['beatdown house', 'hip hop','no wave new york punk disco.', 'afro funk.', 'avantegarde.', 'detroit techno.', '80s industrial.', 'chicago house.',
          '70s jazz funk', 'freestyle\n']







for genre in genres:
  print(f"Genre: {genre}")

def introduction_text(name):
    print("")
    print(
      "Let's pick some records for a new dj mix to listen to while at work.."
  )
    print(
      "My favourite genres range from hip hop, jazz, funk, chicago house, freestyle, detroit techno, no wave, post punk, disco and experimental electronica. "
  )
    print("The record library is calling!")
    print("")
    print(f"ok {name}, lets put this mix together")
    print("")


class Genre:
    def __init__(self, name, artist):
      self.name = name
      self.artist = artist





class Artist:
    def __init__(self, name, artist, title, description):
      self.name = name
      self.artist = artist
      self.title = title
      self.description = description




class Record1(Artist):
    def __init__(self):
      self.name = "Moodymann"
      self.title = "Taken Away"
      self.description = "It is a double lp of on fire detroit funk by Mr Kenny Dixon Jnr, but with an added bonus lp of a previous mp3 only release mini album."
      self.song = ("/Users/apple1/Music/iTunes/iTunes Media/Music/Awesome Dre & The Hardcore Commitee/You Can't Hold Me Back/08 committing rhymes.mp3")



class Record2(Artist):
    def __init__(self):
      self.name = "Sheila E"
      self.title = "Glamorous Life"
      self.description = "Prince infused freestyle electro pop heaven with awesome TR- 727 drum patterns."


class Record3(Artist):
    def __init__(self):
      self.name = "Awesome Dre"
      self.title = "You Can't Hold Me Back"
      self.description = "up tempo 1989 hip hop from The D with razor sharp lyrics. "

class Record4(Artist):
    def __init__(self):
      self.name = "Neneh Cherry"
      self.title = "Buffalo Stance"
      self.description = "1980s freestyle chart hit"
class Record:
  def __init__(self, artist, title, genre, year, label):
    self.artist = artist
    self.title = title
    self.genre = genre
    self.year = year
    self.label = label

  def show(self):
    print('artist:\t\t',self.artist, 'title:\t\t', self.title, 'genre:\t\t', self.genre, 'year:\t\t', self.year, 'label:\t\t', self.label)

moodymann = Record('moodymann.', 'taken away.', 'beatdown house.', '2020.', 'kdj.\n')
sheila_e = Record('sheila e.', 'glamorous life.', 'freestyle.', '1984.', 'warner.\n')
awesome_dre =Record('awesome dre.', 'you cant hold me down.', 'hip hop.', '1989.', 'bentley.\n' )
james_black = Record('james black.', 'contort yourself.', 'no wave new york punk disco.', '1980.', 'Z.\n')
amajika = Record('amajika.', 'got my magic working.', 'afro funk.', '1982.', 'la casa tropical.\n')
can = Record('can.', 'tago mago.', '70s prog rock.', '1971.', 'united artists.\n')
anthony_shakir = Record('shake.', 'songs for my mother.', 'detroit techno.', '2000.', 'frictional.\n')
mark_stewart = Record('mark stewart.', 'as the veneer of democracy begins to fade.', 'industrial, 80s.', '1984.', 'mute.\n')
ron_hardy = Record('ron hardy.', 'sensation.', 'chicago house.', '1985.', 'trax.\n')
fred_wesley = Record('fred wesley.', 'damn right i am somebody.', '70s jazz funk.', '1973.', 'people.\n')
model_500 = Record('model 500.', 'no ufos.', 'detroit techno.', '1986.', 'metroplex.\n')
records = [moodymann, sheila_e, james_black, amajika, can, anthony_shakir, mark_stewart, ron_hardy, fred_wesley, model_500]



moodymann.show()
sheila_e.show()
james_black.show()
amajika.show()
can.show()
anthony_shakir.show()
mark_stewart.show()
ron_hardy.show()
fred_wesley.show()
model_500.show()







def filterByGenre():
  print('\nAlbums by genre:')
  for albumGenre in genres:
    for record in records:
      if record.__getattribute__('genre') == albumGenre:
        print('This album is from genre ', albumGenre)
        record.show()

filterByGenre()




class Mixtape:
  def __init__(self):
    pass

  def start(self):
      name = input("What is your name?\n")
      introduction_text(name)

      choice = input(
        "So first, what record should we start the mix with? a. Moodymann, b. Sheila E, c. Awesome Dre, d.Neneh Cherry\n"
      )
      if choice == "a":
        artist = Record1()


      elif choice == "b":
        artist = Record2()


      elif choice == "c":
        artist = Record3()

      elif choice == "d":
        artist = Record4()



      else:
        print("You have not selected a valid option!")
        exit()

      genre = Genre(name, artist)

      self.middle(genre,artist)

  def middle(self, genre, artist):
      print(
        f"This record is by {artist.name} and it's title is named {artist.title}. {artist.description}\n"
      )

      self.end(artist, genre)

  def end(self, artist, genre):
      print(
          f"Cool choice, {genre.name}! You chose {genre.artist.name} to kick off the new mix, perfect intro!"
      )

      choice = input(
          "So first, what record should we start the mix with? a. Moodymann, b. Sheila E or c. Awesome Dre\n"
      )
      if choice == "a":
          artist = Record1()
          from PIL import Image
          im = Image.open(r"/Users/apple1/Desktop/taken_away.jpg")
          im.show()
          from playsound import playsound
          playsound("/Users/apple1/Music/iTunes/iTunes Media/Music/Moodymann/Taken Away/05 Slow Down.mp3")



      elif choice == "b":
        artist = Record2()
        from PIL import Image
        im =Image.open(r"/Users/apple1/Desktop/sheila_e.jpg")
        im.show()
        from playsound import playsound
        playsound("/Users/apple1/Music/iTunes/iTunes Media/Music/Sheila E_/The Glamorous Life (8 Minute Version) (UK 12_ Promo)/01 The Glamorous Life (8 Minute Version).mp3")

      elif choice == "c":
        artist = Record3()
        from PIL import Image
        im =Image.open(r"/Users/apple1/Desktop/dre.jpg")
        im.show()
        from playsound import playsound
        playsound(
            "/Users/apple1/Music/iTunes/iTunes Media/Music/Awesome Dre & The Hardcore Commitee/You Can't Hold Me Back/08 committing rhymes.mp3")
      elif choice == "d":
        artist = Record4()
        from PIL import Image
        im = Image.open(r"/Users/apple1/Desktop/neneh.jpg")
        im.show()
        from playsound import playsound
        playsound("/Users/apple1/Music/iTunes/iTunes Media/Music/Now That's What I Call Music 14/Now That's What I Call Music 14 - CD 2/01 Buffalo Stance.mp3")


new_mix = Mixtape()
new_mix.start()