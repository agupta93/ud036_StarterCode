import media
import fresh_tomatoes

# Below are the instances of the movie objects for 4 Movies
blade_runner = media.Movie('Blade Runner', 'https://m.media-amazon.com/images/M/MV5BMTk2OTU3MDA3N15BMl5BanBnXkFtZTgwMTg5NjUyMjI@._V1_QL50_SX1777_CR0,0,1777,744_AL_.jpg', 'https://www.youtube.com/watch?v=gCcx85zbxz4')
thor_ragnarock = media.Movie('Thor Ragnarock', 'https://m.media-amazon.com/images/M/MV5BMTY1NDA1Mjc3MF5BMl5BanBnXkFtZTgwNTExMjgwNDI@._V1_QL50_SX1777_CR0,0,1777,744_AL_.jpg', 'https://www.youtube.com/watch?v=ue80QwXMRHg')
alien_covenant = media.Movie('Alien: (Covenant)', 'https://m.media-amazon.com/images/M/MV5BOTE5NzgwMmQtYzcxYy00ZjBkLWJmMGQtZmEyNjA2M2FhNTI1XkEyXkFqcGdeQXVyNDg2MjUxNjM@._V1_QL50_SY1000_CR0,0,1551,1000_AL_.jpg', 'https://www.youtube.com/watch?v=svnAD0TApb8')
split = media.Movie('Split', 'https://m.media-amazon.com/images/M/MV5BMTc1NDYyOTA5MV5BMl5BanBnXkFtZTgwMjE2MDY1OTE@._V1_QL50_SY1000_CR0,0,1552,1000_AL_.jpg', 'https://www.youtube.com/watch?v=84TouqfIsiI')

# A List of movies to be displayed on the web page
movies = [blade_runner, thor_ragnarock, alien_covenant, split]

# Opens the browser with the movies list page.
fresh_tomatoes.open_movies_page(movies)