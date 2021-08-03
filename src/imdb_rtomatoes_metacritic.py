import requests
from bs4 import BeautifulSoup

class Rating:

    imdb_url=""
    metacritic_url=""
    rtomatoes_url=""

    def __init__(self, name):
        self.name=name

        google_search=requests.get("https://www.google.com/search?q="+self.name)
        soup = BeautifulSoup(google_search.text, 'html.parser')
        span = soup.find_all('span', class_="BNeawe")

        for i in range(3):
            for link in span[i]:
                last=link['href'].find('&')
                url=link['href'][7:last]
                if i == 0:
                    Rating.imdb_url=url
                if i == 1:
                    Rating.rtomatoes_url=url
                if i == 2:
                    Rating.metacritic_url=url
    
    def soup(self,url):
        user_agent = {'User-agent': 'Mozilla/5.0'}
        return BeautifulSoup(requests.get(url, headers= user_agent).content, 'html.parser')

    def imdb_score(self):
        imdb_r = self.soup(Rating.imdb_url).find_all('span', class_="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV")
        return (imdb_r[0].contents[0])

    def imdb_votes(self):
        imdb_v = self.soup(Rating.imdb_url+"ratings/?ref_=tt_ov_rt").find_all('div', class_ = "allText")
        votes  = imdb_v[0].contents[1].contents[0]
        end = votes.rfind('\n')
        start = votes[:23].rfind(' ')
        return (votes[start+1:end])

    def metacritic_score(self):
        meta_s = self.soup(Rating.imdb_url).find_all('span', class_="score-meta")
        return (meta_s[0].contents[0])

    def metacritic_votes(self):
        meta_c = self.soup(Rating.metacritic_url).find_all('span', class_ ="based_on")
        return (meta_c[0].contents[0].split(' ')[2])

    def tomatometer(self):
        t_meter = self.soup(Rating.rtomatoes_url).find('score-board').attrs['tomatometerscore']
        return (t_meter)

    def tomatometer_reviews(self):
        t_review = self.soup(Rating.rtomatoes_url).find_all('a', class_="scoreboard__link scoreboard__link--tomatometer")
        return (t_review[0].contents[0][:3])
    