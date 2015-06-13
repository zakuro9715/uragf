from django.views.gereric import TemplateView


def template(template_name):
    return TemplateView.as_view(template_name=template_name)
