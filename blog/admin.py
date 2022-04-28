from django.contrib import admin
from .models import Article,Category
# Register your models here.

@admin.action(description='منتشر شود')
def make_published(modeladmin, request, queryset):
    queryset.update(status='Publish')

@admin.action(description='پیش نویس شود')
def make_drafted(modeladmin, request, queryset):
    queryset.update(status='Draft')

class CategoryAdmin(admin.ModelAdmin):
	list_display=('position','title','slug','parent','status')
	list_filter=(['status'])
	search_fields = ('title','slug')
	prepopulated_fields={"slug":("title",)}

admin.site.register(Category,CategoryAdmin)



@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','slug','publish','author','status','Category_to_str')
	list_editable = ('status',)
	prepopulated_fields = {"slug": ("title",)}
	actions = [make_published, make_drafted]


	def Category_to_str(self,obj):
		return ",".join([category.title for category in obj.category.all()])
	Category_to_str.short_description = 'دسته بندی'