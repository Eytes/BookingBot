import datetime

from BookingBot.src.backend.repositories.reservation import ReservationRepository
from src.backend.schemas.reservation import (
    CreateReservationSchema,
    UpdateReservationSchema,
)


def test_create_reservation(since_datetime, until_datetime):
    return ReservationRepository.create(
        CreateReservationSchema(
            **{
                "since_datetime": since_datetime,
                "until_datetime": until_datetime,
            }
        )
    )


def test_update_reservation(resevation_id, since_datetime, until_datetime):
    return ReservationRepository.update(
        resevation_id,
        UpdateReservationSchema(
            **{
                "since_datetime": since_datetime,
                "until_datetime": until_datetime,
            }
        ),
    )


def test_get_all_reservations():
    return ReservationRepository.get_all()


def test_get_one_reservation(reservation_id):
    return ReservationRepository.get_one(reservation_id)


def test_delete_one_reservation(reservation_id):
    return ReservationRepository.delete_one(reservation_id)


test_create_reservation(
    datetime.datetime(2020, 10, 17, 10, 15),
    datetime.datetime(2020, 10, 17, 10, 15),
)
print(test_get_all_reservations())
print(test_get_one_reservation("0a2dd684-e416-4cb0-b3f2-271fc429a7d3"))
print(
    test_update_reservation(
        "0a2dd684-e416-4cb0-b3f2-271fc429a7d3",
        datetime.datetime(2020, 10, 17, 10, 15),
        datetime.datetime(3000, 10, 17, 10, 15),
    )
)
print(test_delete_one_reservation("0a2dd684-e416-4cb0-b3f2-271fc429a7d3"))
