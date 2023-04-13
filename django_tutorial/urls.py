from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')), # 전체프로젝트 구조에서는 /까지만 뒷부분은 articles url에서 불러옴
]