from django.contrib import admin

from app.models import Book, Impression


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "publisher", "page")  # 一覧に出したい項目
    list_display_links = ("id", "name")  # リンクをつける項目


admin.site.register(Book, BookAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ("id", "comment")
    list_display_links = ("id", "comment")
    # raw_id_fields = ("book",)  # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）


admin.site.register(Impression, ImpressionAdmin)
