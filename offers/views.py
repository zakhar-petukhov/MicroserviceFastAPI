from typing import List, Union

from fastapi import APIRouter

from common import utils as common_utils

from . import models, schemes

router = APIRouter()


@router.post("/create", status_code=201, response_model=schemes.Offer)
async def create_offer(offer: schemes.CreateOffer):
    with common_utils.insert_model():
        return await models.Offer.create(**offer.dict())


@router.post("/", response_model=Union[schemes.Offer, List[schemes.Offer]])
async def get_offer(offer_request: schemes.OfferRequest):
    if offer_request.offer_id is not None:
        return await common_utils.get_model(models.Offer, offer_request.offer_id)
    if offer_request.user_id is not None:
        return await models.Offer.query.where(
            models.Offer.user_id == offer_request.user_id
        ).gino.all()
