from django.contrib import admin

# Register your models here.


from .models import Rule, Router, InterfaceRouter


class RouterAdmin(admin.ModelAdmin):
    pass


class RuleAdmin(admin.ModelAdmin):
    pass


class InterfaceRouterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Router, InterfaceRouterAdmin)
admin.site.register(InterfaceRouter, RouterAdmin)
admin.site.register(Rule, RuleAdmin)
