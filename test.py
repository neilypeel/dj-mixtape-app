print('\n\nhello, here is a list of genres from playlist to choose\n\n')


artist = ['moodymann', 'sheila e', 'awesome dre','ESG', 'amajika', 'can', 'inner city', 'new order', 'ron hardy', 'fred wesley', 'model 500', 'neneh cherry', 'fela kuti']
genres = ['beatdown house', 'hip hop','no wave new york punk disco.', 'afro funk.', 'avantegarde.', 'detroit techno.', '80s new wave electro.', 'chicago house.',
          '70s jazz funk', 'freestyle\n']
song_list = ("song library/01 Controversy.mp3", "song library/1-02 Everything's Gone Green.mp3", "song library/02 Buggin' Out.mp3", "song library/05 Slow Down.mp3", "song library/sensation.mp3")




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
      self.name = "Inner City"
      self.title = "Big Fun"
      self.description = "Cool choice to start the party! A classic detroit techno burner!."




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
esg = Record('ESG.', 'moody.', 'no wave new york punk disco.', '1980.', '99.\n')
amajika = Record('amajika.', 'got my magic working.', 'afro funk.', '1982.', 'la casa tropical.\n')
can = Record('can.', 'im so green.', '70s prog rock.', '1972.', 'united artists.\n')
inner_city = Record('inner city.', 'big fun.', 'detroit techno.', '1988.', 'kms.\n')
new_order = Record('new order.', 'everythings gone green.', '80s new wave electro.', '1981.', 'factory.\n')
ron_hardy = Record('ron hardy.', 'sensation.', 'chicago house.', '1985.', 'trax.\n')
fred_wesley = Record('fred wesley.', 'damn right i am somebody.', '70s jazz funk.', '1973.', 'people.\n')
model_500 = Record('model 500.', 'no ufos.', 'detroit techno.', '1986.', 'metroplex.\n')
neneh_cherry = Record('neneh cherry', 'buffalo stance', 'freestyle', '1988', 'circa\n' )
fela_kuti = Record('fela kuti', 'upside down','afro funk', '1976', 'afrodisia\n')
records = [moodymann, sheila_e, esg, amajika, can, inner_city, new_order, ron_hardy, fred_wesley, model_500]



moodymann.show()
sheila_e.show()
esg.show()
amajika.show()
can.show()
inner_city.show()
new_order.show()
ron_hardy.show()
fred_wesley.show()
model_500.show()
neneh_cherry.show()
fela_kuti.show()






#gets called when an attribute is accessed
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
    choice = ""
    artist = Record("","","","","")
    genre = Genre("","")
    pass

  def start(self):
      name = input("What is your name?\n")
      introduction_text(name)

      self.choice = input(
        "So first, what record should we start the mix with? a. Inner City, b. Sheila E, c. Awesome Dre, d.Neneh Cherry\n"
      )

      if self.choice == "a":
        self.artist = Record1()


      elif self.choice == "b":
        self.artist = Record2()


      elif self.choice == "c":
        self.artist = Record3()

      elif self.choice == "d":
        self.artist = Record4()



      else:
        print("Track choice not specified!")
        exit()

      self.genre = Genre(name, self.artist)

      self.middle()

  def middle(self):
      print(
        f"This record is by {self.artist.name} and it's title is named {self.artist.title}. {self.artist.description}\n"
      )

      self.end()

  def end(self):
      print(
          f"{self.genre.artist.name}"
      )

      if self.choice == "a":
          self.artist = Record1()
          from PIL import Image
          im = Image.open(r"/Users/apple1/Desktop/bigfun.jpg")
          im.show()
          from playsound import playsound
          playsound("song library/05 Big Fun.mp3")



      elif self.choice == "b":
        self.artist = Record2()
        from PIL import Image
        im =Image.open(r"/Users/apple1/Desktop/sheila_e.jpg")
        im.show()
        from playsound import playsound
        playsound("./song library/01 The Glamorous Life (8 Minute Version).mp3")

      elif self.choice == "c":
        self.artist = Record3()
        from PIL import Image
        im =Image.open(r"/Users/apple1/Desktop/dre.jpg")
        im.show()
        from playsound import playsound
        playsound("./song library/08 committing rhymes.mp3")

      elif self.choice == "d":
        self.artist = Record4()
        from PIL import Image
        im = Image.open(r"/Users/apple1/Desktop/neneh.jpg")
        im.show()
        from playsound import playsound
        playsound("./song library/01 Buffalo Stance.mp3")

new_mix = Mixtape()
new_mix.start()

from playsound import playsound
from PIL import Image

artist = ['moodymann', 'sheila e', 'awesome dre','ESG', 'amajika', 'can', 'inner city', 'new order', 'ron hardy', 'fred wesley', 'model 500', 'neneh cherry', 'fela kuti']
genres = ['beatdown house', 'hip hop','no wave new york punk disco.', 'afro funk.', 'avantegarde.', 'detroit techno.', '80s new wave electro.', 'chicago house.',
          '70s jazz funk', 'freestyle\n']
song_list = ("song library/01 Controversy.mp3", "song library/1-02 Everything's Gone Green.mp3", "song library/no UFOs.mp3", "song library/01 Upside Down.mp3", "song library/02 Blow Your Head.mp3")
art_list = ("/Users/apple1/Desktop/controversy.jpg", "/Users/apple1/Desktop/new order.jpg", "/Users/apple1/Desktop/noufos.jpg", "/Users/apple1/Desktop/upsidedown.jpg", "/Users/apple1/Desktop/fredwesley.jpg")
while True:
    choice = input("ok dj!! so lets now choose more songs from the list.. press numbers 0 - 4 to select\n\n")
    index= int(choice)
    print(song_list[index])
    im = Image.open(art_list[index])
    im.show()
    playsound(song_list[index])












