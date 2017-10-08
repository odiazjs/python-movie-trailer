import re
import media


class Movie(media.Media):
    def __init__(
        self,
        title,
        storyline,
        poster_image_url,
        trailer_url,
        release_date
    ):
        media.Media.__init__(self, title, poster_image_url, release_date)
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_url = self.get_youtube_embeded_url(trailer_url)
        self.release_date = release_date

    def get_youtube_embeded_url(self, trailer_url):
        # Extract the youtube ID from the url
        youtube_id = re.search(r'(?<=v=)[^&#]+', trailer_url)
        youtube_id = youtube_id or re.search(r'(?<=be/)[^&#]+', trailer_url)
        trailer_youtube_id = youtube_id.group(0) if youtube_id else None
        self.youtube_id = trailer_youtube_id
        base_url = 'http://www.youtube.com/embed/'
        return base_url + trailer_youtube_id + '?autoplay=1&html5=1'
