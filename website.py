import webbrowser
import os
import movieFactory
import serieFactory

# for every movie
# create and format html content
def get_movies_html(movie_list):

    movies_content = ''
    for movie in movie_list:
        
        movie_factory = movieFactory.MovieFactory(movie)
        movies_content += movie_factory.formatHtmlContent()
    
    return movies_content

# for every serie
# create and format html content
def get_series_html(serie_list):
    
    series_content = ''
    for serie in serie_list:
        
        serie_factory = serieFactory.SerieFactory(serie)
        series_content += serie_factory.formatHtmlContent()

    return series_content

# inject html head, style and script
# and create the html 
def openSite(movies_content, series_content):
    
    main_page_head = '''
        <head>
            <meta charset="utf-8">
            <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
            <style>
                body {
                    background-color: whitesmoke;
                }
                a{
                    text-decoration:none;
                }
                div, h2, h3, h4 {
                    font-family: 'Roboto', sans-serif;
                    color: black;
                }
                .truncate{
                    width: 175px;
                    text-overflow: ellipsis;
                    overflow: hidden;
                    white-space: nowrap;
                }
                .container{
                    display: flex;
                }
                .movie-item{
                    padding: 10px;
                    border: 1px solid #ccc;
                    height: 200px;
                    width: 150px;
                    box-shadow: 0px 5px 5px 0px #ccc;
                    background-color: whitesmoke;
                    margin: 5px;
                    background-size: cover !important;
                }
                .movies-title{
                    font-size: 24px;
                    font-weight: 600;
                    text-align: center;
                }
                .movie-info{
                    text-align: center;
                    padding: 0px;
                    margin: 0px;
                }
                .modalDialog {
                    position: fixed;
                    font-family: Arial, Helvetica, sans-serif;
                    top: 0;
                    right: 0;
                    bottom: 0;
                    left: 0;
                    background: rgba(0, 0, 0, 0.8);
                    z-index: 99999;
                    opacity:0;
                    -webkit-transition: opacity 400ms ease-in;
                    -moz-transition: opacity 400ms ease-in;
                    transition: opacity 400ms ease-in;
                    pointer-events: none;
                }
                .modalDialog:target {
                    opacity:1;
                    pointer-events: auto;
                }
                .modalDialog > div {
                    width: 600px;
                    position: relative;
                    margin: 10% auto;
                    padding: 5px 20px 13px 20px;
                    background: #fff;
                }
                .close {
                    background: #424242;
                    color: #FFFFFF;
                    line-height: 25px;
                    position: absolute;
                    right: 0px;
                    text-align: center;
                    top: 0px;
                    width: 24px;
                    text-decoration: none;
                    font-weight: bold;
                    -webkit-border-radius: 12px;
                    -moz-border-radius: 12px;
                    border-radius: 0px;
                    -moz-box-shadow: 1px 1px 3px #000;
                    -webkit-box-shadow: 1px 1px 3px #000;
                    box-shadow: 1px 1px 3px #000;
                }
                .close:hover {
                    background: #ccc;
                }
            </style>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js"></script>
            <script>
                // 2. This code loads the IFrame Player API code asynchronously.
                var tag = document.createElement('script');

                tag.src = "https://www.youtube.com/iframe_api";
                var firstScriptTag = document.getElementsByTagName('script')[0];
                firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

                // 3. This function creates an <iframe> (and YouTube player)
                //    after the API code downloads.
                var player;
                function onYouTubeIframeAPIReady(videoId) {
                    player = new YT.Player(videoId, {
                    height: '300',
                    width: '600',
                    videoId: videoId,
                    events: {
                        'onReady': onPlayerReady,
                        'onStateChange': onPlayerStateChange
                    }
                    });
                }

                // 4. The API will call this function when the video player is ready.
                function onPlayerReady(event) {
                    event.target.playVideo();
                }

                // 5. The API calls this function when the player's state changes.
                //    The function indicates that when playing a video (state=1),
                //    the player should play for six seconds and then stop.
                var done = false;
                function onPlayerStateChange(event) {
                    if (event.data == YT.PlayerState.PLAYING && !done) {
                    setTimeout(stopVideo, 6000);
                    done = true;
                    }
                }
                function stopVideo() {
                    player.stopVideo();
                }
            </script>
        </head>'''

    main_page_content = '''
    <!DOCTYPE html>
        <html lang="en">
            <body>
                <div class="movies-title">
                    Movies
                </div>
                <div class="container">
                    {movies}
                </div>
                <br/>
                <div class="movies-title">
                    Series
                </div>
                <div class="container">
                    {series}
                </div>
            </body>
        </html>'''

    # use pythons
    # webbrowser api to
    # open the html site content
    output_file = open('template.html', 'w')
    final_content = main_page_content.format(movies=movies_content, series=series_content)
    output_file.write(main_page_head + final_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)