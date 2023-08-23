# Board

## HTTP status code

- 200 : OK
- 30n : redirect
- 4nn : client error(사용자 잘못)
    - 401 : Unauthorized(인증 문제)
    - 403 : forbidden(권한 문제)
    - 404 : Not Found(url 실수)
- 500 : server error
--- 
<br>

- 프로젝트 생성 / 앱 생성

```bash
django-admin startproject <pjtname> .
django-admin startapp <appname>
```

- 그 외 나머지 명령어

```bash
python manage.py <command>
```

---
<br>

1. django 프로젝트 생성 -> 가상환경 설정 -> django 설치 -> 서버 실행 확인 -> 앱 활성화(생성 및 등록)

2.  pjt folder의 `urls.py`
```python
path('posts/',include('posts.urls')),
```

3. app folder에 `urls.py` 생성
```python 
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index'),
]

```