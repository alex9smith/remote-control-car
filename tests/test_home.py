import pytest
from flask import Flask
from app import create_app


@pytest.fixture
def app() -> Flask:
    return create_app("test")


@pytest.fixture
def client(app: Flask) -> Flask.test_client:
    return app.test_client()


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_has_video_feed(client):
    response = client.get("/")
    assert b'<img src="/video-stream" width="100%">' in response.data
