from django.contrib import admin

from models import Host, Machine_Room

class HOST_Admin(admin.ModelAdmin):
    list_display = ('ipaddr', 'hostname', 'status', 'opersys', 'supporter', 'mroom')
    list_filter  = ('adddate', 'hostname', 'status', 'opersys')
    search_fields = ('hostname', 'status', 'opersys')
    
class Mroom_Admin(admin.ModelAdmin):
    list_display = ('name', 'address', 'telphone', 'email', 'overtime')
    list_filter  = ('name', 'address', 'telphone', 'email')
    
        
admin.site.register(Host, HOST_Admin)
admin.site.register(Machine_Room, Mroom_Admin)
