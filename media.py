import webbrowser

class Movie():
	""" This class provides a way to store information about movies"""
	VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
	def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
		""" This method provides a way to store information about movies"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_trailer
	def show_trailer(self):
		""" This class provides a way to show trailers in the browser"""
		webbrowser.open(self.trailer_youtube_url)

