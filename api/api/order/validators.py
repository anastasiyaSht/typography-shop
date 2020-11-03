from django.core.exceptions import ValidationError


def validate_only_numbers(value):
    if not value.isdigit():
        raise ValidationError("Value must be a digit.")
