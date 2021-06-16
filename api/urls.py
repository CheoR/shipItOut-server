from django.conf.urls import url
from .views import index

urlpatterns = [
    # By assigning the url a name you can use this value
    #  as a reference in view methods and templates,
    #  which means any future changes made to the url path,
    #  automatically updates all url definitions in view
    #  methods and templates.
    url(r'^$', index, name='index'),
]

# Application namespaces of included URLconfs
app_name = 'api'
