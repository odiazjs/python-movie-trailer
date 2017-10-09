import media


class Serie(media.Media):
    """This class is targeted to instantiate a serie object and
    is represented by inherting from Media class since it shares 
    a media properties.

    - **parameters**, **types**, **return** and **return types**::
          :param title: the title of the media clip
          :param description: a short description of the serie
          :param poster_image_url: the url of the poster picture
          :param seasons: number of seasons released
          :param release_date: the date that the media clip was released
          :type title: type string
          :type description: type string
          :type poster_image_url: type string
          :type seasons: type number
          :type release_date: type string
          :return: return serie instance
          :rtype: the return type Serie class
          
          :Example:
          
          serie = new Serie('The Serie', 'A funny one.', 'poster.jpg', 10, 01/01/2015')
          
    """
    def __init__(
        self,
        title,
        description,
        poster_image_url,
        seasons,
        release_date
    ):
        media.Media.__init__(self, title, poster_image_url, release_date)
        self.title = title
        self.description = description
        self.poster_image_url = poster_image_url
        self.seasons = seasons
        self.release_date = release_date
