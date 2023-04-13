from django.urls import path
from page import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('article/<int:pk>',views.ArticleDetailView.as_view(),name='article-detail'),
    path('add_post',views.AddPostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>',views.UpdatePostView.as_view(),name='update_post'),
    path('article/<int:pk>/remove',views.DeletePostView.as_view(),name='delete_post'),
    path('article/<int:pk>/comment/',views.AddCommentView.as_view(),name='add_comment'),
    path('article/<int:post_id>/comment/<int:comment_id>/reply/',views. CommentReplyView.as_view(), name='add_reply'),

]
