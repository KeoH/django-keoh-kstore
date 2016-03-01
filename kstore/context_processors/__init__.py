#encoding:utf-8
from kstore.models import BasicConfiguration

def basic_configuration_context_processor(request):
    try:
        config = BasicConfiguration.objects.all().first()
    except Exception as e:
        config = {
            'company_name': 'No company Name',
            'theme': 'one'
        }

    return {'superconfig': config}
