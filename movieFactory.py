class MovieFactory():
    """ Couple a movie into
        a stateful factory to be created
        whenever we need to represent a movie

    - **parameters**, **types**, **return** and **return types**::
          :param movie: the movie instance
          :type movie: type Movie
          :return: return movie instance
          :rtype: the return type MovieFactory class
          
          :Example:
          
          movie = new Movie(...)
          movie_factory = new MovieFactory(movie)
          
    """
    def __init__(self, movie):
        self.movie = movie
        self.content_html = '''
        <a href="#openModal{youtube_id}" onclick="onYouTubeIframeAPIReady('{youtube_id}')">
            <div class="movie-item-container">
                <div class="movie-item" style="background: url({img_url}) no-repeat scroll 0px 0px;"></div>
                <div>
                    <h3 class="movie-info truncate">{title}</h3>
                    <p class="movie-info truncate">{storyline}</p>
                </div>
            </div>
        </a>
        <div id="openModal{youtube_id}" class="modalDialog">
            <div><a href="#close" title="Close" class="close" onclick="stopVideo(this)">X</a>
                <h2>{title}</h2>
                <p>{storyline}</p>
                <div id={youtube_id}></div>
            </div>
        </div>
        '''

    def format_html_content(self):
        return self.content_html.format(
            title=self.movie.title,
            storyline=self.movie.storyline,
            img_url=self.movie.poster_image_url,
            trailer_url=self.movie.trailer_url,
            youtube_id=self.movie.youtube_id
        )
