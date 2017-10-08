class Media():
    """This class holds the common properties of a media type object

    - **parameters**, **types**, **return** and **return types**::
          :param title: the title of the media clip
          :param poster_image_url: the url of the poster picture
          :param release_date: the date that the media clip was released
          :type title: type string
          :type poster_image_url: type string
          :type release_date: type string
          :return: return media instance
          :rtype: the return type Media class
          
          :Example:
          
          video_clip = new Media('The Video Clip', 'http://www.images.com/the_video_clip.jpeg', '01/01/2015')
          
    """
    def __init__(self, title, poster_image_url, release_date):
        self.title = title
        self.poster_image_url = poster_image_url
        self.release_date = release_date