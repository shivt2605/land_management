from django.contrib import admin

# Register your models here.
from .models import *

class StateAdmin(admin.ModelAdmin):
	list_display=('id','name','image_tag')
admin.site.register(State,StateAdmin)

class CityAdmin(admin.ModelAdmin):
	list_display=('id','name','image_tag')
admin.site.register(City,CityAdmin)


class LocalityAdmin(admin.ModelAdmin):
	list_display=('id','name','image_tag')
admin.site.register(Locality,LocalityAdmin)


class ProjectAdmin(admin.ModelAdmin):
	list_display=('id','name','image_tag')
admin.site.register(Project,ProjectAdmin)


class BlockAdmin(admin.ModelAdmin):
	list_display=('id','name','image_tag')
admin.site.register(Block,BlockAdmin)


class PlatAdmin(admin.ModelAdmin):
	list_display=('id','block','plat_no','size', 'price_sq_ft','total_price','dimension','image_tag')
admin.site.register(Plat,PlatAdmin)



