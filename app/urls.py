from django.urls import path
from .views import home,about,portfolio, blog, blog_detail


urlpatterns = [
    path('', home),
    path('about/', about),
    path('portfolio/', portfolio),
    path('blog/', blog, name="blog"),
    path('blog/<int:pk>/', blog_detail, name="blog_detail")
]
