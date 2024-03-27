from django.contrib import admin
from django.db.models import Count
from .models import BlogCategory, Post, BlogComment, BlogImage


class ImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1


class CommentInline(admin.TabularInline):
    model = BlogComment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'category',
                    'comment_count', 'publish_date')
    list_filter = ('author', 'category', 'publish_date')
    search_fields = ('title', 'content')
    inlines = [ImageInline, CommentInline]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(comment_count=Count('comments'))

    @admin.display(ordering='comment_count')
    def comment_count(self, post):
        return post.comments.count()


@admin.register(BlogCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'post_count')

    search_fields = ('name', 'description')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(post_count=Count('posts'))

    @admin.display(ordering='post_count')
    def post_count(self, category):
        return category.posts.count()


@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'text', 'author',
                    'publish_date', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('post', 'author')
    search_fields = ('text',)


@admin.register(BlogImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'image', 'caption')
    list_filter = ('post',)
