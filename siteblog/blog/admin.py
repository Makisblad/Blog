from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe# для показа миниатуюры изображения в админке


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields ='__all__'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # для автозаполнения слага на основании тайтла
    form = PostAdminForm
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category','tags')
    save_on_top = True
    readonly_fields = ('viwes', 'created_at', 'get_photo')
    fields = ('title', 'slug','category','tags', 'content', 'photo', 'get_photo', 'viwes', 'created_at')



    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width=50 >')
        return '-'
    get_photo.short_description = 'Фото'

class PostsInline(admin.TabularInline):
    model = Post.tags.through
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        PostsInline,
    ]

class CategotyAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategotyAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
