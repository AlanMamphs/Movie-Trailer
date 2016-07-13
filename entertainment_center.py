import media
import fresh_tomatoes
# Creating new Movie objects from media class
toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://youtu.be/KYz2wyBy3kc")
avatar = media.Movie("Avatar", 
					"A marine on an alien planet",
					"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", #NOQA
					"https://youtu.be/5PSNL1qE6VY")
terminator_2 = media.Movie("Terminator 2", 
							"Robots try to change future changing the past", 
							"https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
							"https://youtu.be/eajuMYNYtuY" )
theRevenent = media.Movie("The Revenent",
						 "A man and his revenge", 
						 "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
						 "https://youtu.be/oYiT-vLjhC4")
theMachinist = media.Movie("The Machinist", 
							"A psychologica thriller", 
							"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcS8208Lqm9BKTePeMd9vBwP38K1u6ewOpBRjPoaBya6a-E4RL15",#NOQA
							"https://www.youtube.com/watch?v=gxH8U_49QnU")
prestige = media.Movie("The Prestige", 
					"A mystery thriller drama film", 
					"https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Prestige_poster.jpg/220px-Prestige_poster.jpg",
					 "https://youtu.be/ijXruSzfGEc")
# Creating list of created Movie objects
movies = [toy_story, avatar, terminator_2, theRevenent, theMachinist, prestige]
# Passing Movies list into fresh tomatoes python file
fresh_tomatoes.open_movies_page(movies)
