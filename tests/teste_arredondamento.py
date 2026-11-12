
from decimal import Decimal, ROUND_HALF_UP

valores = [
    Decimal("61335.804"),
    Decimal("64662.894"),
    Decimal("45991.094"),
]

total_geral = sum(valores, Decimal("0"))

total_mensal = sum(
    (valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
     for valor in valores),
    Decimal("0.00"),
)

total_arredondado = total_geral.quantize(
    Decimal("0.01"),
    rounding=ROUND_HALF_UP,
)

print("Total geral:", total_arredondado)
print("Soma mensal:", total_mensal)
print("Diferença:", total_mensal - total_arredondado)
