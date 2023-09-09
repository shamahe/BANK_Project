from django.contrib import admin
from accountapp.models import  District, Branch,Person,Gender,AccountType


admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Person)
admin.site.register(Gender)
admin.site.register(AccountType)

