from django.forms import SelectDateWidget


class FixedSelectDateWidget(SelectDateWidget):
    def get_context(self, *args, **kwargs):
        old_state = self.is_required
        self.is_required = False
        result = super(FixedSelectDateWidget,
                       self).get_context(*args, **kwargs)
        self.is_required = old_state
        return result
