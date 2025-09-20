# Reason of creating ----> here I am creating main router and role of this main router will Be inculude both endpoint detech.py and test.py
from fastapi import APIRouter
# we now import detech and test py which Is I am already created:
from service.api.endpoint.detect import detect_router
from service.api.endpoint.test import test_router


# next things will Be create main router
main_router=APIRouter()

main_router.include_router(detect_router)
main_router.include_router(test_router)