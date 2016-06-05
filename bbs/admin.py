#-*- coding:utf-8 -*-
from django.contrib import admin

from models import Bbs, BBS_user, Category
# Register your models here.

class BBS_Admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'signature','view_count', 'ranking', 'create_date', 'updated_date')
    list_filter  = ('title', 'author')
    search_fields = ('title', 'author__user__username')
    
    #add other model message
    def signature(self, obj):
        return obj.author.signature
    
    signature.short_Description = '开发者账号描述'
    
    
class Category_Admin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter  = ('name', 'user')
    #search_fields = ('name', 'user__user__username')
    
class BBS_user_Admin(admin.ModelAdmin):
    list_display = ('user', 'signature')
    list_filter  = ('user', 'signature')
    #search_fields = ('user__user__username', 'signature')
        
admin.site.register(Bbs, BBS_Admin)
admin.site.register(BBS_user, BBS_user_Admin)
admin.site.register(Category, Category_Admin)
