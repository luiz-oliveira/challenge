from django.core.validators import RegexValidator

class CustomValidators():
    """
        This class contains all custom validations used on database
    """  
    def validate_phone():
        # Simple phone validation just to check the size of the field
        return [RegexValidator(regex=r'^(?:(55\d{2})|\d{2})[6-9]\d{8}$', message="Invalid phone number")]