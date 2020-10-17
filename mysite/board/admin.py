from django.contrib import admin
from board.models import Board, Comment


class BoardAdmin(admin.ModelAdmin):
    readonly_fields = ('views',)


admin.site.register(Board, BoardAdmin)
admin.site.register(Comment)
