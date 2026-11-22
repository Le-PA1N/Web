from django.http import JsonResponse

from .models import Note


def note_list(request):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    notes = Note.objects.order_by("-created_at").values(
        "id",
        "title",
        "content",
        "is_done",
        "created_at",
    )

    return JsonResponse({"notes": list(notes)}, status=200)
