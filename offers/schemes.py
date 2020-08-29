from typing import Optional

from pydantic import root_validator

from common.schemes import BaseModel


class CreateOffer(BaseModel):
    title: str
    text: str
    user_id: int


class Offer(CreateOffer):
    id: int


class OfferRequest(BaseModel):
    user_id: Optional[int]
    offer_id: Optional[int]

    @root_validator(pre=True)
    def ensure_data(cls, values):
        if not ("user_id" in values or "offer_id" in values):
            raise ValueError("Either of user_id, offer_id must be passed")
        return values
