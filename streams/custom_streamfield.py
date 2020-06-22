from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from wagtail.core import blocks


class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    button_url = blocks.URLBlock(required=False)
    button_page = blocks.PageChooserBlock(required=False)

    class Meta:  # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"

    def clean(self, value):
        # Error container 
        errors = {}

        # Check if both fields are empty 
        if not value.get('button_url') and value.get('button_page') is None:
            errors['button_url'] = ErrorList(['You must select a page, or enter a URL. Please fill just one of these.'])
            errors['button_page'] = ErrorList(['You must select a page, or enter a URL. Please fill just one of these.'])
        # Check if both fields are filled
        elif value.get('button_url') and value.get('button_page'):
            errors['button_url'] = ErrorList(['Please select a page OR enter a URL (choose one)'])
            errors['button_page'] = ErrorList(['Please select a page OR enter a URL (choose one)'])

        # If there are errors, raise a validation with the errors dict from line 20. 
        if errors:
            raise ValidationError('Validation error in StructBlock', params=errors)

        # If no ValidationError was raised, perform a regular clean on this StreaemField. 
        return super().clean(value)