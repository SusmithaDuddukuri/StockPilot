"""Landed cost calculations, freight apportionment, and customs duty allocation."""
from .validation import ValidationError


def compute_landed_unit_cost(
    base_unit_cost,
    quantity,
    total_freight_charge=0.0,
    customs_duty_pct=0.0,
    cargo_insurance_pct=0.0,
    drayage_handling_fee=0.0
):
    """Compute fully absorbed landed unit cost and overhead apportionment."""
    try:
        base_cost = float(base_unit_cost)
        units = int(quantity)
        freight = float(total_freight_charge)
        duty_pct = float(customs_duty_pct)
        ins_pct = float(cargo_insurance_pct)
        handling = float(drayage_handling_fee)
    except (TypeError, ValueError) as exc:
        raise ValidationError("Numeric parameters are required for landed cost calculation.") from exc

    if units <= 0:
        raise ValidationError("Quantity must be greater than zero.")
    if base_cost < 0 or freight < 0 or duty_pct < 0 or ins_pct < 0 or handling < 0:
        raise ValidationError("Cost and surcharge inputs cannot be negative.")

    total_base_value = base_cost * units
    unit_freight = round(freight / units, 4)
    unit_duty = round(base_cost * (duty_pct / 100.0), 4)
    unit_insurance = round(base_cost * (ins_pct / 100.0), 4)
    unit_handling = round(handling / units, 4)

    total_surcharges_per_unit = unit_freight + unit_duty + unit_insurance + unit_handling
    final_landed_unit_cost = round(base_cost + total_surcharges_per_unit, 2)
    total_landed_shipment_value = round(final_landed_unit_cost * units, 2)
    markup_pct = round((total_surcharges_per_unit / base_cost) * 100, 2) if base_cost > 0 else 0.0

    return {
        "quantity_units": units,
        "base_unit_cost": base_cost,
        "apportioned_unit_freight": round(unit_freight, 2),
        "apportioned_unit_customs_duty": round(unit_duty, 2),
        "apportioned_unit_insurance": round(unit_insurance, 2),
        "apportioned_unit_handling": round(unit_handling, 2),
        "total_overhead_per_unit": round(total_surcharges_per_unit, 2),
        "final_landed_unit_cost": final_landed_unit_cost,
        "total_landed_shipment_value": total_landed_shipment_value,
        "overhead_markup_percentage": markup_pct
    }
