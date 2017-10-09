class SerieFactory():
    """ Couple a serie into
        a stateful factory to be created
        whenever needed to represent a serie

    - **parameters**, **types**, **return** and **return types**::
          :param serie: a serie instance object
          :type serie: type Serie
          :return: return SerieFactory instance
          :rtype: the return type SerieFactory class
          
          :Example:
          
          serie = new Serie(...)
          serie_factory = new SerieFactory(serie)
          
    """
    def __init__(self, serie):
        self.serie = serie
        self.content_html = '''
            <a href="#openModal{title}">
                <div class="movie-item-container">
                    <div class="movie-item" style="background: url({img_url}) no-repeat scroll 0px 0px;"></div>
                    <div>
                        <h3 class="movie-info truncate">{title}</h3>
                        <p class="movie-info truncate">{description}</p>
                        <p class="movie-info">{seasons} Seasons</p>
                    </div>
                </div>
            </a>
            <div id="openModal{title}" class="modalDialog">
                <div><a href="#close" title="Close" class="close">X</a>
                    <h2>{title}</h2>
                    <p>{description}</p>
                    <div>{seasons} Seasons</div>
                </div>
            </div>
            '''

    def format_html_content(self):
        return self.content_html.format(
            title=self.serie.title,
            description=self.serie.description,
            img_url=self.serie.poster_image_url,
            seasons=self.serie.seasons
        )