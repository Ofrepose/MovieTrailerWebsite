import media
import fresh_tomatoes

# create instance of movie of your choice.
# example code --> nameofmovie = media.Movie("Movie Title", "Movie
# Description", "Poster Image URL", "Movie Trailer URL")

toy_story = media.Movie(
    "Toy Story",
    "Toys come to life and fight each other for control over some kid's"
    "affection",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar", "On the lush alien world of Pandora live the Na'vi, beings who"
    "appear primitive but are highly evolved. Because the planet's environment"
    "is poisonous, human/Na'vi hybrids, called Avatars, must link to human"
    "minds to allow for free movement on Pandora. Jake Sully (Sam"
    "Worthington), a paralyzed former Marine, becomes mobile again through"
    "one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a"
    "bond with her grows, he is drawn into a battle for the survival of her"
    "world.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

equilibrium = media.Movie(
    "Equilibrium",
    "In a futuristic world, a regime has eliminated war by suppressing"
    "emotions: books, art and music are strictly forbidden and feeling is"
    " a crime punishable by death. Clerick John Preston (Christian Bale) is a"
    "top-ranking government agent responsible for destroying those who resist"
    "these rules. When he misses a dose of Prozium, a mind-altering drug that"
    "hinders emotion, Preston, who has been trained to enforce strict laws of"
    "the new regime, suddenly becomes the one capable of overthrowing it.",
    "https://upload.wikimedia.org/wikipedia/en/f/f6/Equilibriumposter.jpg",
    "https://www.youtube.com/watch?v=gskwYHE0zww")

the_invention_of_lying = media.Movie(
    "The Invention Of Lying",
    "Mark Bellison (Ricky Gervais) is a down-on-his-luck writer who lives in"
    "world where falsehoods are completely unknown. When Mark suddenly"
    "develops the ability to lie, the notion that 'honesty is the best policy'"
    "goes out the window, and he uses his newfound skill for personal gain.",
    "https://upload.wikimedia.org/wikipedia/en/2/2b/Invention_of_lying_ver2.jpg",  # NOQA
    "https://www.youtube.com/watch?v=UJLeymrMzIk")

the_shape_of_water = media.Movie(
    "The Shape Of Water", "Elisa is a mute, isolated woman who works as a"
    "cleaning lady in a hidden, high-security government laboratory in 1962"
    "Baltimore. Her life changes forever when she discovers the lab's"
    "classified secret -- a mysterious, scaled creature from South America"
    "that lives in a water tank. As Elisa develops a unique bond with her new"
    "friend, she soon learns that its fate and very survival lies in the hands"
    "of a hostile government agent and a marine biologist.",
    "https://upload.wikimedia.org/wikipedia/en/3/37/The_Shape_of_Water_%28film%29.png",  # NOQA
    "https://www.youtube.com/watch?v=XFYWazblaUA")

coriolanus = media.Movie(
    "Coriolanus",
    "Caius Martius, aka Coriolanus (Ralph Fiennes), is an arrogant and"
    "fearsome general who has built a career on protecting Rome from"
    "its enemies. Pushed by his ambitious mother (Vanessa Redgrave) to seek"
    "the position of consul, Coriolanus is at odds with the masses and"
    "unpopular with certain colleagues (James Nesbitt, Paul Jesson). When a"
    "riot results in his expulsion from Rome, Coriolanus seeks out his sworn"
    "enemy, Tullus Aufidius (Gerard Butler). Together, the pair vow to destroy"
    "the great city.",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Coriolanus_%282011_film%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Di-XOO_LTlw")


movies = [  # Creates a list with all movie intances you have created above.
    toy_story,
    avatar,
    equilibrium,
    the_invention_of_lying,
    the_shape_of_water,
    coriolanus]


# This creates the html file and opens the Webpage with all of your Movies
fresh_tomatoes.open_movies_page(movies)
