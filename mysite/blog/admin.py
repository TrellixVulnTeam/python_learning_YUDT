from django.contrib import admin
from .models import Post,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','slug','author','body','publish','status',)
	list_filter = ('status','created','publish','author',)
	search_fields = ('title','body',)
	prepopulated_fields = {'slug':('title',)}
	ordering = ['status','-publish']
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','email','post','created','active',)
	list_filter = ('active','created','updated',)
	search_fields = ('name','email','body',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)