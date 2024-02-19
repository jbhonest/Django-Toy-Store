from django.contrib import admin
from django.db.models import Count
from .models import Category, Product, Comment, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category',
                    'comment_count')
    list_filter = ('category', )
    search_fields = ('name', 'description')
    inlines = [ImageInline, CommentInline]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(comment_count=Count('comments'))

    @admin.display(ordering='comment_count')
    def comment_count(self, product):
        return product.comments.count()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'product_count')

    search_fields = ('name', 'description')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count('products'))

    @admin.display(ordering='product_count')
    def product_count(self, category):
        return category.products.count()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'text', 'author',
                    'publish_date', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'author')
    search_fields = ('text',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image', 'caption')
    list_filter = ('product',)
