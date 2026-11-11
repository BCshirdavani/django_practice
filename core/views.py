from pathlib import Path

from django.http import FileResponse, HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_GET

from .image_catalog import IMAGES

IMAGE_DIR = Path(__file__).resolve().parent / "images"

def home(request):
    return HttpResponse("Hello from my Django app!")


@require_GET
def image_list(request):
    return JsonResponse({
        "images": [
            {"id": image_id, "name": image["name"], "label": image["label"]}
            for image_id, image in IMAGES.items()
        ]
    })


@require_GET
def image_detail(request, image_id):
    image = IMAGES.get(image_id)
    if image is None:
        raise Http404("Image not found")

    try:
        image_file = (IMAGE_DIR / image["name"]).open("rb")
    except FileNotFoundError:
        raise Http404("Image file not found")

    return FileResponse(
        image_file,
        content_type=image["content_type"],
        filename=image["name"],
        as_attachment=False,
    )


@require_GET
def imagetest(request):
    image_path = Path(__file__).resolve().parent / "images" / "rainier.jpg"
    return FileResponse(
        image_path.open("rb"),
        content_type="image/jpeg",
        filename="rainier.jpg",
        as_attachment=False,
    )
