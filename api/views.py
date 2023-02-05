from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from api.models import Link, UniquePassed


class HomePageTemplateView(TemplateView):
    """Home page view."""

    template_name = 'home.html'


class APIDocsPageTemplateView(TemplateView):
    """Api docs page view."""

    template_name = 'api_docs.html'


class LinkStatisticsPageTemplateView(TemplateView):
    """Link statistics page view."""

    template_name = 'link_statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = self.kwargs['key']

        return context


class ForwardingPageTemplateView(TemplateView):
    """Forwarding user to short link."""

    template_name = 'forwarding.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        link = get_object_or_404(Link.objects.filter(key=self.kwargs['key']))

        context['link'] = link.link

        # save passed
        if not self.request.session.session_key:
            # Get session
            self.request.session.save()
        session_key = self.request.session.session_key

        if not UniquePassed.objects.filter(session_key=session_key):
            passed = UniquePassed()
            passed.link = link
            passed.session_key = session_key
            passed.save()

        link.passed += 1
        link.save()
        return context


def custom_404_error(request, exception):
    """Custom 404 error page"""

    response_data = {'error_code': 404, 'description': 'Данной страницы не существует. '
                                                       'Вы уверены, что верно указали адрес?.'}
    return render(request, 'error.html', response_data)


def custom_500_error(request, exception=None):
    """Custom 404 error page"""

    response_data = {'error_code': 500, 'description': 'Ошибка сервера. '
                                                       'Знаем, чиним. Повторите попытку чуть позже.'}
    return render(request, 'error.html', response_data)


def custom_403_error(request, exception=None):
    """Custom 403 error page"""

    response_data = {'error_code': 403, 'description': 'Ошибка авторизации. '
                                                       'Авторизуйтесь и повторите попытку позже.'}
    return render(request, 'error.html', response_data)
