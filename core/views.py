from pathlib import Path

from django.http import FileResponse, HttpResponse
from django.views.decorators.http import require_GET

def home(request):
    return HttpResponse("Hello from my Django app!")


@require_GET
def imagetest(request):
    image_path = Path(__file__).resolve().parent / "images" / "rainier.jpg"
    return FileResponse(
        image_path.open("rb"),
        content_type="image/jpeg",
        filename="rainier.jpg",
        as_attachment=False,
    )
