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
    def __init__(self, name, title, description):
      self.name = name
      self.title = title
      self.description = description




class Record1(Artist):
    def __init__(self):
      self.name = "Moodymann"
      self.title = "Taken Away"
      self.description = "It is a double lp of on fire detroit funk by Mr Kenny Dixon Jnr, but with an added bonus lp of a previous mp3 only release mini album."




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


class Mixtape:
  def __init__(self):
    pass

  def start(self):
      name = input("What is your name?\n")
      introduction_text(name)

      choice = input(
        "So first, what record should we start the mix with? a. Moodymann, b. Sheila E or c. Awesome Dre\n"
      )
      if choice == "a":
        artist = Record1()
      elif choice == "b":
        artist = Record2()
      elif choice == "c":
        artist = Record3()
      else:
        print("You have not selected a valid option!")
        exit()

      genre = Genre(name, artist)

      self.middle(genre,artist)


  def middle(self, genre, artist):
      print(
        f"This record is by {artist.name} and it's title is named {artist.title}. {artist.description}\n"
      )

      self.end(genre)


  def end(self, genre):
      print(
        f"Cool choice, {genre.name}! You chose {genre.artist.name} to kick off the new mix, perfect intro!"
      )

new_mix = Mixtape()
new_mix.start()


class Record:
  def __init__(self, artist, title, genre, year, label):
    self.artist = artist
    self.title = title
    self.genre = genre
    self.year = year
    self.label = label
    print('here are some more to add to the mix from my library')
  def show(self):
    print('artist:\t\t',self.artist, 'title:\t\t', self.title, 'genre:\t\t', self.genre, 'year:\t\t', self.year, 'label:\t\t', self.label)


james_black = Record('james black.', 'contort yourself.', 'no wave new york punk disco.', '1980.', 'Z.')
amajika = Record('amajika.', 'got my magic working.', 'afro funk.', '1982.', 'la casa tropical.')
can = Record('can.', 'tago mago.', '70s prog rock.', '1971.', 'united artists.')
anthony_shakir = Record('shake.', 'songs for my mother.', 'detroit techno', '2000.', 'frictional.')
mark_stewart = Record('mark stewart.', 'as the veneer of democracy begins to fade.', 'industrial, 80s.', '1984.', 'mute.')
ron_hardy = Record('ron hardy.', 'sensation.', 'chicago house.', '1985.', 'trax.')
fred_wesley = Record('fred wesley.', 'damn right i am somebody.', '70s jazz funk.', '1973.', 'people.')
model_500 = Record('model 500.', 'no ufos.', 'detroit techno.', '1986.', 'metroplex.')
records = [james_black, amajika, can, anthony_shakir, mark_stewart, ron_hardy, fred_wesley, model_500]


the_records = [1, 2, 3, 4, 5, 6, 7]
artist = ['james black', 'amajika', 'can', 'anthony shakir', 'mark stewart', 'ron hardy', 'fred wesley', 'model 500']
genres = ['no wave new york punk disco', 'afro funk', 'prog rock', 'detroit techno', '80s industial', 'chicago house',
          '70s jazz funk']

# this first kind of for-loop goes through a list
for number in the_records:
  print(f"This is record {number}")

# same as above
for artist in artist:
  print(f"name of artist: {artist}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for genre in genres:
  print(f"I got {genre}")

# we can also build lists, first start with an empty one
amount = []

# then use the range function to do 0 to 5 counts
for the_records in range(0, 8):
  print(f"Adding {the_records} to the list.")
# append is a function that lists understand
amount.append(the_records)

# now we can print them out too
for the_records in amount:
  print(f"total amount was: {the_records}")

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