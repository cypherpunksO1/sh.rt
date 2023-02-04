from django.views.generic import TemplateView
from api.base.tools import get_client_ip
from .models import Link
from .serializers import *


class HomePageTemplateView(TemplateView):
    template_name = 'home.html'


class APIDocsPageTemplateView(TemplateView):
    template_name = 'api_docs.html'


class LinkStatisticsPageTemplateView(TemplateView):
    template_name = 'link_statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = self.kwargs["key"]

        return context


class ForwardingPageTemplateView(TemplateView):
    template_name = 'forwarding.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _link = Link.objects.filter(key=self.kwargs["key"])
        if _link:
            _link = _link[0].link
            context["link"] = _link

            data = {'ip_address': get_client_ip(self.request)}
            serializer = AddPassedSerializer(data=data)
            serializer.is_valid()
            serializer.create(serializer.validated_data, key=self.kwargs['key'])

            return context
