
import csv

from helpers import BASE, COLUMNS
from onfly_report.repositories.csv_reservation_repository import (
    CsvReservationRepository,
)


def test_repository_reads_all_reservations_and_parses_record_250(tmp_path):
    csv_path = tmp_path / "reservas.csv"

    # Criamos um CSV com 300 reservas identificáveis.
    rows = [
        {**BASE, "reservation_id": f"R-{number}"}
        for number in range(1, 301)
    ]

    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=COLUMNS,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    repository = CsvReservationRepository(csv_path)

    reservations = repository.read()

    # Verifica se todos os registros foram lidos.
    assert len(reservations) == 300

    # Verifica se o registro 250 está presente e foi interpretado.
    assert reservations[249].values["reservation_id"] == "R-250"
