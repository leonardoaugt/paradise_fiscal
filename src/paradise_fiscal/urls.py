"""nfe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

from paradise_fiscal.paradise_api.views import *

urlpatterns = [

    # NFeTransaction
    url(r'^api/nfetran/resume/$'), NfeTran.as_view()),
    url(r'^api/nfetran/resume/(?P<key>.+)$'), NfeTranKey.as_view()),

    # NFe
    url(r'^api/nfe/all/$', Nfes.as_view()),
    url(r'^api/nfe/tipo/(?P<type>.+)$', NfeType.as_view()),
    url(r'^api/nfe/chave/(?P<key>.+)$', NfeKey.as_view()),
    url(r'^api/nfe/cnpjcpf/(?P<personal_doc>.+)$', NfePersonalDocument.as_view()),
    url(r'^api/nfe/status/(?P<status>.+)$', NfeStatus.as_view()),

]