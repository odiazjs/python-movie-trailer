import movie
import serie
import website

#Create some movies
movies_content = ''
toy_story = movie.Movie('Toy Story', 'A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boys room.', 'https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg', 'https://www.youtube.com/watch?v=KYz2wyBy3kc', '2014')
moneyball = movie.Movie('Moneyball', 'Oakland Athletics general manager Billy Beanes successful attempt to assemble a baseball team on a lean budget by employing computer-generated analysis to acquire new players.', 'https://upload.wikimedia.org/wikipedia/en/2/2e/Moneyball_Poster.jpg', 'https://www.youtube.com/watch?v=-4QPVo0UIzc', '2016')
leage_of_their_own = movie.Movie('A League Of Their Own', 'Two sisters join the first female professional baseball league and struggle to help it succeed amidst their own growing rivalry.', 'https://images-na.ssl-images-amazon.com/images/I/51x%2BvjamsHL.jpg', 'https://www.youtube.com/watch?v=WcN392H2jx0', '1999')
payback = movie.Movie('Payback', 'After a successful heist, Porter is shot by his wife and his best friend. They leave him there to die but when he recovers, he seeks revenge and wants his share of the money.', 'https://www.ecartelera.com/carteles/7400/7453/001_cxvzm4.jpg', 'https://www.youtube.com/watch?v=vpV9eIXbVlU', '1999')
movies = [toy_story, moneyball, leage_of_their_own, payback, toy_story, moneyball, leage_of_their_own]

#Create some series
series_content = ''
friends = serie.Serie('Friends', 'An American television sitcom, created by David Crane and Marta Kauffman, which aired on NBC from September 22, 1994, to May 6, 2004, lasting ten seasons.', 'https://www.merchandisingplaza.co.uk/43640/2/Posters-Friends-Friends-Poster-l.jpg', 10, '2001')
breaking_bad = serie.Serie('Breaking Bad', 'An American neo-western crime drama television series created and produced by Vince Gilligan. The show originally aired on the AMC network for five seasons, from January 20, 2008 to September 29, 2013.', 'http://www.wired.com/images_blogs/underwire/2013/09/BreakingBadComingSoon.jpg', 5, '2013')
the_office = serie.Serie('The Office', 'An American television comedy series that aired on NBC from March 24, 2005, to May 16, 2013.[1] It is an adaptation of the BBC series of the same name.', 'https://pbs.twimg.com/profile_images/734141362031984640/2I-QZZkR.jpg', 10, '2009')
orange_is_the_new_black = serie.Serie('Orange Is The New Black', 'Convicted of a decade old crime of transporting drug money to an ex-girlfriend, normally law abiding Piper Chapman is sentenced to a year and a half behind bars to face the reality of how life changing prison can really be.', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTU1OTcwNjg2Nl5BMl5BanBnXkFtZTgwOTk0NTk0MjI@._V1_UY1200_CR90,0,630,1200_AL_.jpg', 5, '2013')
series = [friends, breaking_bad, the_office, orange_is_the_new_black, friends, breaking_bad, the_office]

movies_content = website.get_movies_html(movies)
series_content = website.get_series_html(series)
website.openSite(movies_content, series_content)