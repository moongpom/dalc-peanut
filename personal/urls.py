"""peanut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from personal.views import *
from personal.models import *
urlpatterns = [
    path('imageUpload/',imageUpload,name="imageUpload"),

    # 나중에는 아래에 주석 있는 애 풀고 커밋
    #path('colorSelect/', colorSelect, name="colorSelect"),

    path('colorSelect1/<int:imageId>',colorSelect1,name="colorSelect1"),
    path('colorSelect2/<int:imageId>',colorSelect2,name="colorSelect2"),
    path('colorSelect3/<int:imageId>',colorSelect3,name="colorSelect3"),
    path('colorSelect4/<int:imageId>',colorSelect4,name="colorSelect4"),
    # #최종 결과에서는 이미지 아이디 넘겨주기
    # #path('result/<int:imageId>',result,name="result"),


    path('result/<int:result_val>', result, name="result"),
    path('loading/<int:imageId>', loading, name="loading"),
]
