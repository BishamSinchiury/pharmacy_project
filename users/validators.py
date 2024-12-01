from django.core.exceptions import ValidationError
import os
import re
from pathlib import Path

from django.core.exceptions import ValidationError
from django.utils import timezone
def check_required_fields(data, required_fields, message=None):
    # List of required fields for POST requests
    for field in required_fields:
        if field not in data or data[field] is None:
            raise ValidationError(
                {field: "This field is required and cannot be blank."}
            )


def get_unique_filename(instance, filename):
    """
    Generates a unique filename based on the instance and its associated file field.

    Args:
        instance (Model instance): The instance of the model where the file is being uploaded.
        filename (str): The original filename of the uploaded file.

    Returns:
        str: The full file path including the unique filename.

    Raises:
        ValueError: If the instance type is invalid or if no matching field for the filename is found.
    """
    # Ensure the instance is of a valid type
    valid_types = ["InstitutionDocuments", "IndividualDocuments"]
    if instance.__class__.__name__ not in valid_types:
        raise ValueError(
            f"Invalid instance type. Expected one of {valid_types}, got {instance.__class__.__name__}."
        )

    # Get the field name where the file is being uploaded
    field_name = None
    for field in instance._meta.fields:
        if (
            hasattr(instance, field.name)
            and getattr(instance, field.name) == filename
        ):
            field_name = field.name
            break

    # Raise error if field name is not found
    if field_name is None:
        raise ValueError(
            f"No matching field found for the given filename: {filename}"
        )

    # Extract file extension using os.path.splitext
    _, file_extension = os.path.splitext(filename)
    file_extension = file_extension.lstrip(
        "."
    )  # Remove leading dot from extension

    # Generate the unique filename
    unique_filename = f"{field_name}.{file_extension}"

    # Determine the directory path based on the instance type
    if instance.__class__.__name__ == "IndividualDocuments":
        dir_path = Path(
            f"media/documents/individual/{instance.individual.id}/{field_name}"
        )
    else:
        dir_path = Path(
            f"media/documents/institution/{instance.institution.id}/{field_name}"
        )

    # Create directory if it doesn't exist
    dir_path.mkdir(parents=True, exist_ok=True)

    # Check if there are any existing files starting with the field name and remove them
    for existing_file in dir_path.iterdir():
        if existing_file.stem.startswith(field_name):
            existing_file.unlink()

    # Return the full file path
    file_path = dir_path / unique_filename
    return str(file_path)



def validate_image_file_extension(value):
    """
    Validates that the uploaded file has a valid image extension (JPG or PNG).

    Args:
        value (File): The uploaded file to be validated.

    Raises:
        ValidationError: If the file extension is not JPG or PNG.
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if ext.lower() not in valid_extensions:
        raise ValidationError("Only JPG and PNG files are allowed.")
    

def convert_to_lowercase(data):
    """
    Recursively converts all string values in a dictionary or list to lowercase.

    Args:
        data (dict or list): The data to be converted to lowercase.

    Returns:
        dict or list: The data with all string values in lowercase.
    """
    if isinstance(data, dict):
        return {key: convert_to_lowercase(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_to_lowercase(item) for item in data]
    elif isinstance(data, str):
        return data.lower()  # Convert string to lowercase
    else:
        return data  # Return data as is if it's not a dict, list, or string
