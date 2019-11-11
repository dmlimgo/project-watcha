



# watcha 구현 과제

> PJT_v1.1.pdf 명세서에 맞추어 watcha와 같은 영화 추천 웹 페이지를 구성하였습니다.





## Install

가상환경에서 진행

```bash
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddata cast.json
$ python manage.py loaddata crew.json
$ python manage.py loaddata genre.json
$ python manage.py loaddata movie.json
$ python manage.py runserver
```

이후 localhost:8000 으로 접속





## 개발 환경

###### Django, Python, Sqlite3, TheMovieDB





## 팀 구성

본인 : DB설계 및 Django

팀원 : DB크롤링 및 데이터 정제 





## ERD

###### ERD 설계 목표

- user간 follow 기능 (M:N)
- user profile (1:1)
- rating기능 구현 (1:N, 1:M)
- TheMovieDB에서 제공하는 similar_movie를 movie와 M:N구조로 연결
- genre, cast, crew를 movie와 연결

![erd](images\erd.png)





## 구현

#### 메인 페이지

데이터베이스에서 데이터를 읽어와 watcha와 비슷한 레이아웃으로 구성하였습니다.

![watcha1](images\watcha1.PNG)



#### 검색 기능

페이지 상단의 검색창에 검색어를 입력하면 검색 결과를 표시합니다. ORM의 filter를 사용하였습니다.

![watcha4](images\watcha4.PNG)

```python
def search(request):
    # pass
    movies = Movie.objects.all()
    keyword = request.POST.get('search')
    results = []
    for movie in movies.filter(title__contains=keyword):
        results.append(movie)
    print(results)
    context = {
        'keyword': keyword,
        'results': results
    }
    return render(request, 'movies/search.html', context)
```



#### 상세 페이지

![watcha2](images\watcha2.PNG)



#### 댓글 작성

평점을 남길 수 있습니다. ModelForm을 이용하여 구성하였습니다.

![watcha3](images\watcha3.PNG)