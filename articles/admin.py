from django.contrib import admin

# Register your models here.
from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp' #updated
	search_fields = ['title','content']
	list_display = ['title','slug','updated']
	list_editable = ['title']
	list_filter = []
	readonly_fields = ['updated','timestamp']
	prepopulated_fields = {"slug":("title",)}
	class Meta:
		model = Article


admin.site.register(Article,ArticleAdmin)