from django.urls import path

from app import views
from app.views import IndexView, DetailView

app_name = "app"  # htmlからURLを生成する時に使う名前空間

urlpatterns = [
    # 書籍
    path("books/", IndexView.as_view(), name="book_list"),  # 一覧
    # path("books/", views.book_list, name="book_list"),  # 一覧
    path("books/detail/<int:pk>/", DetailView.as_view(), name="book_detail"),  # 詳細
    path("books/add/", views.book_edit, name="book_add"),  # 登録
    path("books/mod/<int:book_id>/", views.book_edit, name="book_edit"),  # 修正
    path("books/del/<int:book_id>/", views.book_del, name="book_del"),  # 削除
    # other
    path("other", views.other, name="other"),
]
