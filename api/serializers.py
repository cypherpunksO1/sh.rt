from rest_framework.serializers import ModelSerializer
from api.models import *
from api.base.tools import make_link_key


def convert_link(link: str) -> str:
    if 'https' not in link or 'http' not in link:
        link = 'https://' + link
    return link


class CutLinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('link',)

    def create(self, validated_data):
        model = Link()
        model.link = convert_link(validated_data['link'])
        model.key = make_link_key()
        model.save()

        return model


class AddPassedSerializer(ModelSerializer):
    class Meta:
        model = Passed
        fields = '__all__'

    def create(self, validated_data, key):
        link_model = Link.objects.filter(key=key)
        if link_model:
            link_model = link_model[0]
            link_model.passed += 1
            link_model.save()

        try:
            passed_model = Passed(ip_address=validated_data['ip_address'],
                                  link_key=key)
            passed_model.save()
        except:
            ...

        return link_model
