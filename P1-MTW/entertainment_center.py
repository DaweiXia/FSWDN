import media
import fresh_tomatoes

'''Fllows are scripts to produce a movies website.'''

# The Shawshank Redemption
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
    "A prominent banker unjustly convicted of murder spends many years in \
    the Shawshank prison. He is befriended by a convict who knows the ropes \
    and helps him to cope with the frightning realities of prison life. MPAA \
    Rating: R (c) 1994 Warner Bros. Entertainment Inc. All Rights Reserved.",
    "https://i.ytimg.com/vi_webp/RLw6hBFJ8bk/movieposter.webp",
    "https://youtu.be/K_tLp7T6U1c")

# Star Wars: The Force Awakens
star_wars_the_force_awakens = media.Movie("Star Wars: The Force Awakens",
    "Visionary director J.J. Abrams brings to life the motion picture event \
    of a generation. As Kylo Ren and the sinister First Order rise from the \
    ashes of the Empire, Luke Skywalker is missing when the galaxy needs him \
    most. It's up to Rey, a desert scavenger, and Finn, a defecting \
    stormtrooper, to join forces with Han Solo and Chewbacca in a desperate \
    search for the one hope of restoring peace to the galaxy.",
    "https://i.ytimg.com/vi_webp/-eYxeRJCYMY/movieposter.webp",
    "https://youtu.be/UitsQDWSlUg")

# The Secret Lift of Pets
the_secret_lift_of_pets = media.Movie("The Secret Life of Pets",
    "Find out what your pets do when you're not at home in this animated \
    comedy featuring the voice talents of Louis C.K., Eric Stonestreet, and \
    Kevin Hart.",
    "https://i.ytimg.com/vi_webp/HdAAeM9jKpM/movieposter.webp",
    "https://youtu.be/Ag-hLxUGn-M")

# Gandhi
gandhi = media.Movie("Gandhi",
    "Sir Ben Kingsley stars as Mohandas Gandhi in Lord Richard Attenborough's \
    riveting biography of the man who rose from simple lawyer to worldwide \
    symbol of peace and understanding. A critical masterpiece, GANDHI is an \
    intriguing story about activism, politics, religious tolerance and freedom. \
    But at the center of it all is an extraordinary man who fought for a \
    nonviolent, peaceful existence, and set an entire nation free. ",
    "https://i.ytimg.com/vi_webp/IQnJjmrcxxQ/movieposter.webp",
    "https://youtu.be/WNAm4jO9t-w")

movies = [
    the_shawshank_redemption, star_wars_the_force_awakens,
    the_secret_lift_of_pets, gandhi
]

# Generate movies page from movies list
fresh_tomatoes.open_movies_page(movies)
