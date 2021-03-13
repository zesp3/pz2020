from facebook_scraper import get_posts
import sys

listposts = []

#page - liczba stron wczytywanych przez scraper
#jeśli nie jest podana z linii poleceń, to wartość
#domyślna wynosi 4
if len(sys.argv) < 2:
    page = 4
else:
    page = int(sys.argv[1])

for post in get_posts('GminaLubianka', pages = page):
    print(post['post_id'])
    print(post['time'])
    #maksymalny rozmiar posta na Facebooku wynosi 63206 znaków
    print(post['text'][:63206])
    print(post['image'])
    print(post['images'])
    print(post['video'])
    print(post['likes'])
    print(post['comments'])
    print(post['shares'])
    print(post['post_url'])
    print(post['link'])
    print(post['is_live'])
