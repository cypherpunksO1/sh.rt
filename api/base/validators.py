from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # Переводит строки на англ.
import urlextract


def validate_link(value):
    links_extractor = urlextract.URLExtract()
    found_links = links_extractor.find_urls(value)
    if not found_links:
        raise ValidationError(
            _('Значение не является ссылкой.'),
            params={'value': value},
        )
