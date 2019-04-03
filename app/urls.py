from django.urls import path

from app import views

app_name = "app"  # htmlからURLを生成する時に使う名前空間

urlpatterns = [
    # 書籍
    path("book/", views.book_list, name="book_list"),  # 一覧
    path("book/add/", views.book_edit, name="book_add"),  # 登録
    path("book/mod/<int:book_id>/", views.book_edit, name="book_edit"),  # 修正
    path("book/del/<int:book_id>/", views.book_del, name="book_del"),  # 削除
]
