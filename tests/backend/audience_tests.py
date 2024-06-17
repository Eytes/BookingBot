from BookingBot.src.backend.repositories.audience import AudienceRepository
from src.backend.schemas.audience import (
    CreateAudienceSchema,
    UpdateAudienceSchema,
)


def test_create_audience(capacity, description):
    return AudienceRepository.create(
        CreateAudienceSchema(
            **{
                "capacity": capacity,
                "description": description,
            }
        )
    )


def test_update_audience(audience_id, capacity, description):
    return AudienceRepository.update(
        audience_id,
        UpdateAudienceSchema(
            **{
                "capacity": capacity,
                "description": description,
            }
        ),
    )


def test_get_all_audiences():
    return AudienceRepository.get_all()


def test_get_one_audience(audience_id):
    return AudienceRepository.get_one(audience_id)


def test_delete_one_audience(audience_id):
    return AudienceRepository.delete_one(audience_id)


test_create_audience(
    15,
    "Отличный личный конференц зал для крутых",
)
print(test_get_all_audiences())
print(test_get_one_audience("72410fcb-c537-49eb-b93b-44126c97d1d8"))
print(
    test_update_audience(
        "72410fcb-c537-49eb-b93b-44126c97d1d8",
        12,
        "Отличный личный конференц зал для крутых, изменено так как 3 стула украли",
    )
)
print(test_delete_one_audience("72410fcb-c537-49eb-b93b-44126c97d1d8"))
