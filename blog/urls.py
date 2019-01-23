from django.urls import path
from . import views
urlpatterns=[
	path('blog/',views.post,name='post'),
	path('blog/<int:post_id>',views.detail,name='detail')
]