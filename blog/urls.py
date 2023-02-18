from django.urls import path, include
from .views import Index, DetailArticleView, LikeArticle, Featured, DeleteArticle

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/delete/', DeleteArticle.as_view(), name='delete'),
    path('<int:pk>/likes', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='featured'),
]