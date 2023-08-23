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


### app 전용 경로 하나 더 만들기

1.  pjt folder의 `urls.py`

```python
urlpatterns = [
    ...
    path('posts/',include('posts.urls')),
]
```

2. app folder에 `urls.py` 생성

```python 
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index'),
]

```

### 공용 base 만들어 쓰기

1. 최상단에 `templates` folder 생성 -> 공용으로 사용할 tool인 `bass.html` 생성

2. pjt folder의 `settings.py`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        ...
    }
]
```

3. `base.html`
- `! + tab`으로 기본틀 생성
- 원하는 내용을 넣을 구멍 생성
```python
<body>
    <div class='container'>
        {% block content %}
        {% endblock %}
    </div>
</body>
```

4. `appname/templates/원하는 html`
- `block` 안에 원하는 내용 넣기
```python
{% enxtends 'base.html' %}

{% block content %}
    # 원하는 내용
{% endblock %}
```