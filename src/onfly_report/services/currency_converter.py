
"""Conversão de valores para BRL."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP

MONEY_QUANTUM = Decimal("0.01")


def convert_to_brl(
    amount: Decimal,
    currency: str,
    rates: dict[str, Decimal],
) -> Decimal:
    """Converte e arredonda o valor para centavos."""
    rate = rates[currency]
    converted = amount * rate

    return converted.quantize(
        MONEY_QUANTUM,
        rounding=ROUND_HALF_UP,
    )
