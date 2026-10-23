"""Hazardous materials regulatory classification, storage segregation, and containment rules."""
from .validation import ValidationError

HAZARD_CLASSES = {
    "CLASS_3_FLAMMABLE": {
        "label": "Class 3 - Flammable Liquids & Solvents",
        "allowed_zone_prefix": "HAZ-FLAM",
        "secondary_containment_required": True,
        "ventilation_required": "Explosion-proof mechanical ventilation",
        "incompatible_with": ["CLASS_5_OXIDIZER", "CLASS_8_CORROSIVE"]
    },
    "CLASS_8_CORROSIVE": {
        "label": "Class 8 - Corrosive Acids & Alkalis",
        "allowed_zone_prefix": "HAZ-CORR",
        "secondary_containment_required": True,
        "ventilation_required": "Corrosion-resistant localized exhaust",
        "incompatible_with": ["CLASS_3_FLAMMABLE", "CLASS_4_FLAMMABLE_SOLIDS"]
    },
    "CLASS_9_LITHIUM_BATTERIES": {
        "label": "Class 9 - Lithium Ion Cells & Batteries",
        "allowed_zone_prefix": "HAZ-BATT",
        "secondary_containment_required": False,
        "ventilation_required": "Standard warehouse with fire suppression blankets",
        "incompatible_with": ["CLASS_3_FLAMMABLE"]
    },
    "NON_HAZARDOUS": {
        "label": "General Commercial Inventory",
        "allowed_zone_prefix": "",
        "secondary_containment_required": False,
        "ventilation_required": "Standard Ambient",
        "incompatible_with": []
    }
}


def validate_hazmat_storage(hazard_class, target_location, neighboring_classes=None):
    """Validate that hazardous materials are stored according to segregation laws."""
    h_class = str(hazard_class).strip().upper()
    rule = HAZARD_CLASSES.get(h_class)
    if not rule:
        raise ValidationError(f"Invalid hazard class: {hazard_class}. Valid options: {', '.join(HAZARD_CLASSES.keys())}")

    loc = str(target_location).strip().upper()
    required_prefix = rule["allowed_zone_prefix"]

    # Zone prefix check
    prefix_compliant = True
    if required_prefix and not loc.startswith(required_prefix):
        prefix_compliant = False

    # Segregation check
    segregation_passed = True
    segregation_conflicts = []
    if neighboring_classes:
        for neighbor in neighboring_classes:
            n_clean = str(neighbor).strip().upper()
            if n_clean in rule["incompatible_with"]:
                segregation_passed = False
                segregation_conflicts.append(n_clean)

    is_compliant = prefix_compliant and segregation_passed

    if not prefix_compliant:
        reason = f"Location '{loc}' is not rated for {rule['label']}. Must be located in a '{required_prefix}' rated containment bay."
    elif not segregation_passed:
        reason = f"Segregation breach: {rule['label']} cannot be co-located with {', '.join(segregation_conflicts)}."
    else:
        reason = "Location and chemical segregation fully compliant with OSHA/DOT guidelines."

    return {
        "hazard_class": h_class,
        "target_location": loc,
        "compliant": is_compliant,
        "prefix_compliant": prefix_compliant,
        "segregation_passed": segregation_passed,
        "status_detail": reason,
        "secondary_containment_required": rule["secondary_containment_required"],
        "ventilation_standard": rule["ventilation_required"]
    }
