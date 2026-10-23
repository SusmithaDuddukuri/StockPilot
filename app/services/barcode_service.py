"""Barcode verification, symbology validation, and label generation standards."""
import re
from .validation import ValidationError


def calculate_ean13_check_digit(digits_12):
    """Calculate the standard GS1 modulo-10 check digit for 12 numeric digits."""
    if not (isinstance(digits_12, str) and digits_12.isdigit() and len(digits_12) == 12):
        raise ValidationError("EAN-13 input must be exactly 12 numeric digits.")
    
    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits_12))
    remainder = total % 10
    return 0 if remainder == 0 else 10 - remainder


def verify_barcode(code, symbology="Code128"):
    """Verify barcode data integrity and symbology compliance."""
    if not isinstance(code, str) or not code.strip():
        return {
            "valid": False,
            "error": "Barcode payload cannot be empty.",
            "grade": "F"
        }
    
    clean_code = code.strip()
    symbology_lower = symbology.lower()

    if symbology_lower in ("code128", "code-128"):
        # Code 128 accepts standard ASCII characters 32 to 126
        if re.fullmatch(r"[\x20-\x7E]+", clean_code) and len(clean_code) <= 80:
            return {
                "valid": True,
                "code": clean_code,
                "symbology": "Code 128",
                "character_count": len(clean_code),
                "grade": "A",
                "print_quality": "High",
                "quiet_zone_mm": 6.35
            }
        return {
            "valid": False,
            "code": clean_code,
            "symbology": "Code 128",
            "error": "Invalid character set or exceeds maximum 80 characters.",
            "grade": "F"
        }

    elif symbology_lower in ("ean13", "ean-13", "upc-a"):
        clean_numeric = re.sub(r"\D", "", clean_code)
        if len(clean_numeric) == 12:
            check_digit = calculate_ean13_check_digit(clean_numeric)
            full_code = f"{clean_numeric}{check_digit}"
            return {
                "valid": True,
                "code": full_code,
                "symbology": "EAN-13",
                "check_digit": check_digit,
                "check_digit_verified": True,
                "grade": "A",
                "quiet_zone_mm": 3.63
            }
        elif len(clean_numeric) == 13:
            expected_check = calculate_ean13_check_digit(clean_numeric[:12])
            actual_check = int(clean_numeric[12])
            is_valid = (expected_check == actual_check)
            return {
                "valid": is_valid,
                "code": clean_numeric,
                "symbology": "EAN-13",
                "check_digit": actual_check,
                "check_digit_verified": is_valid,
                "grade": "A" if is_valid else "F",
                "error": None if is_valid else f"Check digit mismatch: expected {expected_check}, got {actual_check}"
            }
        return {
            "valid": False,
            "code": clean_code,
            "symbology": "EAN-13",
            "error": "EAN-13 barcodes must contain 12 or 13 digits.",
            "grade": "F"
        }

    elif symbology_lower in ("gs1-128", "gs1"):
        # Parse basic application identifiers, e.g. (01)01234567890128(10)LOT123
        ai_matches = re.findall(r"\((\d{2,4})\)([A-Za-z0-9_-]+)", clean_code)
        if ai_matches:
            parsed = {ai: val for ai, val in ai_matches}
            return {
                "valid": True,
                "code": clean_code,
                "symbology": "GS1-128",
                "application_identifiers": parsed,
                "grade": "A",
                "quiet_zone_mm": 6.35
            }
        return {
            "valid": False,
            "code": clean_code,
            "symbology": "GS1-128",
            "error": "Could not parse GS1 Application Identifiers. Expected format: (01)...(10)...",
            "grade": "F"
        }

    return {
        "valid": False,
        "code": clean_code,
        "symbology": symbology,
        "error": f"Unsupported barcode symbology: {symbology}",
        "grade": "F"
    }
