from tmdbv3api import TMDb, Movie
import csv


tmdb = TMDb()
tmdb.api_key = '0462420f053eaee646c334e3a226605b'

tmdb.language = 'ko'
tmdb.debug = True

movie = Movie()
movie_data = []
for i in range(400, 500):
    popular = movie.popular(i)
    img = 'https://www.themoviedb.org/t/p/w220_and_h330_face'

    for p in popular:
        if not p.poster_path:
            p.poster_path = ''
        movies = {"movie_id": p.id,
                  "title": p.title,
                  "overview": p.overview,
                  "poster": img + p.poster_path,
                  "score": round(p.vote_average/2, 1),
                  "genre": p.genre_ids
                  }
        movie_data.append(movies)

# print(movie_data)

f = open('movie_data.csv','w',encoding='utf-8',newline='')
csvWriter = csv.writer(f)
for i in movie_data:
    # dictionary 형태이므로 i의 value 값을 뽑아줘야 함
    csvWriter.writerow(i.values())

f.close()
print('완료')