from django.forms import BaseForm


def get_form_defaults(Form: BaseForm):
    form = Form()
    defaults = {}
    for name, field in form.fields.items():
        if field.initial:
            defaults[name] = field.initial
    return defaults
