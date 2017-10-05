# couple a serie into
# a stateful factory to be created
# whenever needed to represent a serie

class SerieFactory():
    def __init__(self, serie):
        self.serie = serie
        self.contentHtml = '''
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

    def formatHtmlContent(self):
        return self.contentHtml.format(
            title=self.serie.title,
            description=self.serie.description,
            img_url=self.serie.poster_image_url,
            seasons=self.serie.seasons
        )