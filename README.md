# django_practice
practicing Django

## Deploy
```aiignore
python manage.py migrate && python -m gunicorn config.asgi:application -k uvicorn_worker.UvicornWorker --bind 0.0.0.0:10000
```

## create super user
```python manage.py createsuperuser ```

## Image endpoint

Start Django with `python manage.py runserver`, then open
`http://localhost:8000/imagetest/`. This GET endpoint returns the sample image in
`core/images/imagetest.svg` with an `image/svg+xml` content type. The response is
the image itself, rather than JSON containing an image URL.

Display it from a separate Vue app:

```vue
<template>
  <img src="http://localhost:8000/imagetest/" alt="Django test image" />
</template>
```

A normal `<img>` can display this cross-origin image without CORS configuration.
If you want to read the response using JavaScript `fetch` or Axios instead,
configure CORS for your Vue origin in Django, or use your Vue development server's
API proxy. With a proxy mapping `/api` to `http://localhost:8000` and stripping
the `/api` prefix, you can use `/api/imagetest/` as the image URL as well.

To serve your own PNG or JPEG, replace the image path, filename, and content type
in `core/views.py` (for example, `image/png` for a `.png` file).

## Run locally:

With Python 3.12 installed, run these commands from the project directory:

1. Create a virtual environment (first time only): `python3.12 -m venv .venv`
2. Activate it (each new terminal session): `source .venv/bin/activate`
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`
