from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.views import generic

from app.forms import BookForm
from app.models import Book

# 既存のDjango Viewを使うやり方
class IndexView(generic.ListView):
    template_name = "app/book_list.html"

    def get_queryset(self):
        return Book.objects.all().order_by("id")


class DetailView(generic.DetailView):
    model = Book
    # template 名も自動で、book_detail.html が選ばれる


# 原始的やり方
def book_list(request):
    books: QuerySet[Book] = Book.objects.all().order_by("id")
    return render_to_response("app/book_list.html", {"book_list": books})


def book_edit(request, book_id=None):
    if book_id:  # book_id が指定されている (修正時)
        book: Book = get_object_or_404(Book, pk=book_id)
    else:  # book_id が指定されていない (追加時)
        book: Book = Book()

    # 既存Bookの取得
    if request.method == "POST":
        form: BookForm = BookForm(request.POST, instance=book)
        if form.is_valid():
            # book = form.save(commit=False)  # commit=False にするとDBにSaveされない
            # # なにかbookを編集する
            # book.save()

            # ModelFormからModel.save_m2m()を内部で呼び出して保存される
            form.save()
            return redirect("app:book_list")

    else:  # GET
        form = BookForm(instance=book)

    return render(request, "app/book_edit.html", {"form": form, "book_id": book_id})


def book_del(request, book_id):
    book: Book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect("app:book_list")


def other(request):
    return HttpResponse("ただのレスポンス")
