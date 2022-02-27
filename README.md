# dalc-peanut
peanut -  personal+nut    퍼스널컬러
## 서비스 소개

## 개발자
동덕여대 
기획(목지영)
디자인(김수연)
AI(김미소, 김진아, 최다솜)
개발(김은진,정은영)
## 개발 환경

<span>
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/>
 + 텐서플로우  코랩 케라스
</span>


## Reuirements

# git 

* git clone 주소

* git clone 한 뒤에 순서대로 입력하기

* git init


```터미널 git bash로 실행하기``` 

# 가상환경 

* python -m venv myvenv      
* source myvenv/Scripts/activate

* pip install django  
* pip install pillow 
* pip install django-session-timeout

* 폴더 안으로 이동 : cd dalc-peanut

# 클론 끝나고 필요시 사용할 명령어랑 깔아야 할 것 목록
 이거 하려면 secrets.json 파일추가하고 은영 시크릿키 넣어야함 필요하신분 은영이에게 연락쥬세요ㅕ >,< (secrets.json 위치 = manage.py랑 같은 위치)

* python manage.py collectstatic (static파일 모으는 거)

* python manage.py makemigrations

* python manage.py migrate
*  python manage.py makemigrations personal

* python manage.py migrate personal

* python manage.py runserver

# runserver 전 수행해야할 것
* setting.py의 secret key 수정
* python 3.7.9 환경 변수 추가 옵션으로 다운받기 (다운 완료 후에 컴퓨터 껐다 켜야 함)
* vscode에서 python 버전 3.7.9로 변경

# AI 관련 install 목록
* pip install numpy
* pip install sklearn
* pip install joblib

# 머신러닝 실행(폴더는 프로젝트 폴더안에서)
python personal/optimized_peanut_knn_model.py
# 계정
* (admin superuser 이 계정으로 로그인해도 되고 새로만들어도 됨 
* -중간에 데이터날리면서 사라질경우 python manage.py createsuperuser 해서 생성해주기

* id :dalc  #pw :aa112233    )

# 헤로쿠 배포
* pip install gunicorn
* pip install dj-database-url
* pip install psycopg2-binary
* pip install whitenoise


#자주씀
pip freeze > requirements.txt
