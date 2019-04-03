from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect

from app.forms import BookForm
from app.models import Book


def book_list(request):
    books = Book.objects.all().order_by("id")
    return render_to_response("app/book_list.html", dict(books=books))


def book_edit(request, book_id=None):
    # 既存Bookの取得
    if book_id:  # book_id が指定されている (修正時)
        book = get_object_or_404(Book, pk=book_id)
    else:  # book_id が指定されていない (追加時)
        book = Book()

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            book = form.save(commit=False)

            # なにかやる

            book.save()
            return redirect("app:book_list")

    else:  # GET
        form = BookForm(instance=book)

    return render_to_response("app/book_edit.html", dict(form=form, book_id=book_id))


def book_del(request, book_id):
    return HttpResponse("書籍の削除")
