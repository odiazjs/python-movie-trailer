import media

class Serie(media.Media):
    def __init__(self, title, description, poster_image_url, seasons, release_date):
        media.Media.__init__(self, title, poster_image_url, release_date)
        self.title = title
        self.description = description
        self.poster_image_url = poster_image_url
        self.seasons = seasons
        self.release_date = release_date