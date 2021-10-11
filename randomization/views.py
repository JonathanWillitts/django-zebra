from django.http import HttpResponse

from randomization.models import Slot, get_random_site


def create_slots(request, number_of_slots):
    created_slots = []
    for count in range(0, number_of_slots):
        s = Slot()
        s.save()
        created_slots.append(s.sid)

    if created_slots:
        if len(created_slots) == 1:
            response_text = (
                f"Created {len(created_slots)} slot with SID: {created_slots[0]}"
            )
        else:
            response_text = f"Created {len(created_slots)} slots with from {min(created_slots)} to {max(created_slots)}"

    else:
        response_text = "No slots created"
    return HttpResponse(response_text)
