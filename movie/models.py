from django.db import models

# Create your models here.

class MovieModel(models.Model):
	class Meta:
		db_table = "movie"

	from tmdbv3api import TMDb, Movie

	tmdb = TMDb()
	tmdb.api_key = '0462420f053eaee646c334e3a226605b'

	tmdb.language = 'ko'
	tmdb.debug = True

	movie = Movie()
	for i in range(1, 2):
		popular = movie.popular(i)
		img = 'https://www.themoviedb.org/t/p/w220_and_h330_face'

		for p in popular:
			# print(len(p))
			print('ID : ', p.id)
			print('제목 : ', p.title)
			print('줄거리 : ', p.overview)
			print('사진 url : ', img + p.poster_path)
			print('평점 : ', round(p.vote_average / 2, 1))
			print('장르 : ', p.genre_ids)
			print(' ')