from ninja import Router
from .models import WaitlistEntry
from .schemas import (
    ErrorWaitlistEntryCreateSchema,
    WaitlistEntryListSchema,
    WaitlistEntryDetailSchema,
    WaitlistEntryCreateSchema,
    WaitlistEntryUpdateSchema,
)
from typing import List
from django.shortcuts import get_object_or_404
from ninja_jwt.authentication import JWTAuth
import helpers
from .forms import WaitlistEntryCreateForm
import json


router = Router()


def allow_annon(request):
    if not request.user.is_authenticated:
        return True


# /api/waitlists/
@router.get(
    "", response=List[WaitlistEntryListSchema], auth=helpers.api_auth_user_required
)
def list_waitlist_entries(request):
    return WaitlistEntry.objects.filter(user=request.user)


@router.get(
    "{entry_id}/",
    response=WaitlistEntryDetailSchema,
    auth=helpers.api_auth_user_required,
)
def get_waitlist_entries(request, entry_id: int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id, user=request.user)
    return obj


# /api/waitlists/
@router.post(
    "",
    response={201: WaitlistEntryDetailSchema, 400: ErrorWaitlistEntryCreateSchema},
    auth=helpers.api_auth_user_or_annon,
)
def create_waitlist_entry(request, data: WaitlistEntryCreateSchema):
    form = WaitlistEntryCreateForm(data.dict())

    ## Can do this validation using pydantic and that is a better way of doing it and we don't need to use the form.
    if not form.is_valid():
        # cleaned_data = form.cleaned_data
        # obj = WaitlistEntry.objects.create(**cleaned_data)
        form_errors = json.loads(form.errors.as_json())
        return 400, form_errors
    obj = form.save(commit=False)
    if request.user.is_authenticated:
        obj.user = request.user
    obj.save()
    return 201, obj


@router.put(
    "{entry_id}/",
    response=WaitlistEntryDetailSchema,
    auth=helpers.api_auth_user_required,
)
def update_waitlist_entries(request, entry_id: int, payload: WaitlistEntryUpdateSchema):
    obj = get_object_or_404(WaitlistEntry, id=entry_id, user=request.user)
    for k, v in payload.dict().items():
        setattr(obj, k, v)
    obj.save()
    return obj


@router.delete(
    "{entry_id}/delete",
    response=WaitlistEntryDetailSchema,
    auth=helpers.api_auth_user_required,
)
def delete_waitlist_entries(request, entry_id: int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id, user=request.user)
    obj.delete()
    return obj
