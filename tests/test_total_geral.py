
from decimal import Decimal
from onfly_report.repositories.csv_reservation_repository import RawRow
from onfly_report.services.report_builder import ReportBuilder



class FakeReservationRepository:
    def read(self):
        reservas = [
            {
                "reservation_id": "R001",
                "traveler_name": "Pessoa Teste",
                "company_id": "C01",
                "hotel_id": "H01",
                "hotel_name": "Hotel Teste",
                "city": "Belo Horizonte",
                "country": "Brazil",
                "checkin_date": "2025-01-10",
                "checkout_date": "2025-01-12",
                "rooms": "1",
                "status": "CONFIRMED",
                "amount": "100.00",
                "currency": "BRL",
                "payment_method": "CARD",
            },
            {
                "reservation_id": "R002",
                "traveler_name": "Pessoa Teste 2",
                "company_id": "C01",
                "hotel_id": "H02",
                "hotel_name": "Hotel Teste 2",
                "city": "São Paulo",
                "country": "Brazil",
                "checkin_date": "2025-02-10",
                "checkout_date": "2025-02-12",
                "rooms": "1",
                "status": "CONFIRMED",
                "amount": "200.00",
                "currency": "BRL",
                "payment_method": "CARD",
            },
        ]

        return [
            RawRow(values=reserva, line_number=i)
            for i, reserva in enumerate(reservas, start=2)
        ]


class FakeRateRepository:
    def read(self):
        return {"BRL": Decimal("1.000000")}


def test_total_geral_corresponde_a_soma_mensal():
    builder = ReportBuilder(
        reservation_repository=FakeReservationRepository(),
        rate_repository=FakeRateRepository(),
    )

    relatorio = builder.build()

    total_mensal = sum(
        (
            Decimal(mes["total_brl"])
            for mes in relatorio["by_month"]
        ),
        Decimal("0.00"),
    )

    total_geral = Decimal(
        relatorio["summary"]["total_amount_brl"]
    )

    assert total_geral == total_mensal
