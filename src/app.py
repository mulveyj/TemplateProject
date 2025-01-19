"""A simple demonstration FastAPI server."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    """Indicates application health.

    This returns a simple JSON formatted message to indicate that the
    server is running.

    Args:

    Returns:
        dict: standard message
    """
    return {"message": "Application is healthy"}


@app.get("/api/dogs")
def dogs():
    """Provides a list of dogs and their goodness.

    Args:

    Returns:
        dict: list of dogs under the key 'dogs'
    """
    return {
        "dogs": [
            {"name": "fido", "good_doggo": True},
            {"name": "gnasher", "good_doggo": False},
        ]
    }
