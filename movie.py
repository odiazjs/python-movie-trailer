import re
import media


class Movie(media.Media):
    """This class is targeted to instantiate a movie object and
    is represented by inherting from Media class since it shares 
    a media properties.

    - **parameters**, **types**, **return** and **return types**::
          :param title: the title of the media clip
          :param storyline: a short definition of the movie's story
          :param poster_image_url: the url of the poster picture
          :param trailer_url: the url of the movie's trailer clip
          :param release_date: the date that the media clip was released
          :type title: type string
          :type story_line: type string
          :type poster_image_url: type string
          :type trailer_url: type string
          :type release_date: type string
          :return: return movie instance
          :rtype: the return type Movie class
          
          :Example:
          
          video_clip = new Movie('The Movie', 'A wonderful tale.', 'poster.jpg', 'youtube.com/12345', 01/01/2015')
          
    """
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
