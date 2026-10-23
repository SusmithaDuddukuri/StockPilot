"""Cold chain temperature monitoring, climate excursions, and containment workflows."""
from .validation import ValidationError

ZONE_TEMPERATURE_PROFILES = {
    "frozen": {
        "label": "Frozen Storage",
        "min_temp": -25.0,
        "max_temp": -15.0,
        "warning_buffer": 1.5,
    },
    "refrigerated": {
        "label": "Refrigerated (2°C - 8°C)",
        "min_temp": 2.0,
        "max_temp": 8.0,
        "warning_buffer": 1.0,
    },
    "controlled_room_temperature": {
        "label": "Controlled Room Temp (15°C - 25°C)",
        "min_temp": 15.0,
        "max_temp": 25.0,
        "warning_buffer": 2.0,
    }
}


def evaluate_temperature_reading(zone_type, temperature_celsius):
    """Evaluate reading against storage profile standards."""
    try:
        temp = float(temperature_celsius)
    except (TypeError, ValueError):
        raise ValidationError("Temperature must be a valid numeric value.")

    key = str(zone_type).strip().lower().replace("-", "_").replace(" ", "_")
    profile = ZONE_TEMPERATURE_PROFILES.get(key)
    if not profile:
        raise ValidationError(f"Unknown zone type: {zone_type}. Valid types: {', '.join(ZONE_TEMPERATURE_PROFILES.keys())}")

    min_t = profile["min_temp"]
    max_t = profile["max_temp"]
    buf = profile["warning_buffer"]

    if min_t <= temp <= max_t:
        if (temp - min_t) <= buf or (max_t - temp) <= buf:
            severity = "Warning"
            status = "Within limits but near excursion threshold"
            action = "Increase monitoring frequency and verify refrigeration compressors"
        else:
            severity = "Optimal"
            status = "Nominal climate compliance"
            action = "Continue standard scheduled logging"
    elif temp < min_t:
        severity = "Critical Low Excursion"
        variance = round(min_t - temp, 2)
        status = f"Sub-threshold chill: {variance}°C below minimum safe storage limit"
        action = "Initiate immediate thermal barrier check and quarantine sensitive items"
    else:
        severity = "Critical High Excursion"
        variance = round(temp - max_t, 2)
        status = f"Thermal breach: {variance}°C above maximum safe storage limit"
        action = "Halt inbound receiving into zone and quarantine affected SKUs immediately"

    return {
        "zone_type": key,
        "profile_label": profile["label"],
        "target_range": f"{min_t}°C to {max_t}°C",
        "recorded_temperature": temp,
        "severity": severity,
        "is_excursion": "Critical" in severity,
        "status_detail": status,
        "recommended_action": action
    }
