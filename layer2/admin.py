from django.contrib import admin

# Register your models here.



from .models import Switch, Interface


class SwitchAdmin(admin.ModelAdmin):
    pass


class InterfaceAdmin(admin.ModelAdmin):
	pass


admin.site.register(Switch, SwitchAdmin)
admin.site.register(Interface, InterfaceAdmin)

