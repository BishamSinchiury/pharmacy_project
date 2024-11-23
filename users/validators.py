from django.core.exceptions import ValidationError

def check_required_fields(data, required_fields, message=None):
    # List of required fields for POST requests
    for field in required_fields:
        if field not in data or data[field] is None:
            raise ValidationError(
                {field: "This field is required and cannot be blank."}
            )

def validate_password():
    pass