"""Shared request validation for warehouse operational workflows."""
from datetime import date
import re

SKU_PATTERN = re.compile(r"^[A-Z0-9][A-Z0-9._-]{1,39}$")
CODE_PATTERN = re.compile(r"^[A-Z0-9][A-Z0-9-]{2,39}$")

class ValidationError(ValueError):
    """A client-submitted field did not satisfy a business rule."""

def required_text(data, key, label=None, maximum=160):
    value = str(data.get(key, "")).strip()
    if not value:
        raise ValidationError(f"{label or key.replace('_', ' ').title()} is required.")
    if len(value) > maximum:
        raise ValidationError(f"{label or key.replace('_', ' ').title()} must be {maximum} characters or fewer.")
    return value

def optional_text(data, key, maximum=240):
    value = str(data.get(key, "")).strip()
    if len(value) > maximum:
        raise ValidationError(f"{key.replace('_', ' ').title()} must be {maximum} characters or fewer.")
    return value

def integer(data, key, *, minimum=0, maximum=2_000_000_000):
    try:
        value = int(data.get(key))
    except (TypeError, ValueError):
        raise ValidationError(f"{key.replace('_', ' ').title()} must be a whole number.")
    if value < minimum or value > maximum:
        raise ValidationError(f"{key.replace('_', ' ').title()} must be between {minimum} and {maximum}.")
    return value

def money(data, key, *, minimum=0, maximum=1_000_000_000):
    try:
        value = round(float(data.get(key)), 2)
    except (TypeError, ValueError):
        raise ValidationError(f"{key.replace('_', ' ').title()} must be a valid amount.")
    if value < minimum or value > maximum:
        raise ValidationError(f"{key.replace('_', ' ').title()} must be between {minimum} and {maximum}.")
    return value

def normalized_code(data, key, *, sku=False):
    value = required_text(data, key, maximum=40).upper()
    pattern = SKU_PATTERN if sku else CODE_PATTERN
    if not pattern.fullmatch(value):
        raise ValidationError(f"{key.replace('_', ' ').title()} contains unsupported characters.")
    return value

def iso_date(data, key, *, optional=True):
    value = optional_text(data, key, 10)
    if not value and optional:
        return ""
    try:
        date.fromisoformat(value)
    except ValueError:
        raise ValidationError(f"{key.replace('_', ' ').title()} must use YYYY-MM-DD format.")
    return value

def one_of(data, key, choices):
    value = required_text(data, key, maximum=60)
    if value not in choices:
        raise ValidationError(f"{key.replace('_', ' ').title()} must be one of: {', '.join(sorted(choices))}.")
    return value
