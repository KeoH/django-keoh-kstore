from kstore.models import BasicConfiguration

def get_theme_url():
    return BasicConfiguration.objects.all().first().get_theme_url()
