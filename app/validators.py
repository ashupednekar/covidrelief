from rest_framework.serializers import ValidationError


def numeric_mobile_validator(mobile):
    if not mobile.isdigit():
        raise ValidationError(
            "This pin is not entirely numeric.",
            code='pin_entirely_numeric',
        )


def mobile_length_validator(pin):
    if not len(pin) == 10:
        raise ValidationError(
            "Please enter 10 digit mobile number.",
            code='invalid_mobile_no',
        )

