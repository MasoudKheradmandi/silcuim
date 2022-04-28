from django.urls import path
from .import views



app_name="blog"

urlpatterns=[
	path('',views.home,name='home'),
	path('page/<int:page_number>/',views.home,name='home'),
	path('article/<slug:slug>/',views.detailview,name="detailview"),
	path('category/<slug:slug>/',views.category,name='category'),
]
