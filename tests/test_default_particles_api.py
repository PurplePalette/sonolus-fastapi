# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_particle_list_response import GetParticleListResponse  # noqa: F401
from src.models.get_particle_response import GetParticleResponse  # noqa: F401
from src.models.particle import Particle  # noqa: F401


def test_add_particle(client: TestClient) -> None:
    """Test case for add_particle

    Add a particle
    """
    particle = {
        "descriptionEn": "No description",
        "updatedTime": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
        "description": "No description",
        "title": "title",
        "version": 1,
        "subtitleEn": "subtitleEn",
        "userId": "userId",
        "titleEn": "titleEn",
        "subtitle": "subtitle",
        "name": "name",
        "createdTime": 0,
        "authorEn": "authorEn",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/particles",
        headers=headers,
        json=particle,
    )

    assert response.status_code != 500


def test_delete_particle(client: TestClient) -> None:
    """Test case for delete_particle

    Delete a particle
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/particles/{particleName}".format(particleName="particle_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_edit_particle(client: TestClient) -> None:
    """Test case for edit_particle

    Edit a particle
    """
    particle = {
        "descriptionEn": "No description",
        "updatedTime": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "texture": {"type": "LevelData", "hash": "hash", "url": "url"},
        "description": "No description",
        "title": "title",
        "version": 1,
        "subtitleEn": "subtitleEn",
        "userId": "userId",
        "titleEn": "titleEn",
        "subtitle": "subtitle",
        "name": "name",
        "createdTime": 0,
        "authorEn": "authorEn",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PATCH",
        "/particles/{particleName}".format(particleName="particle_name_example"),
        headers=headers,
        json=particle,
    )

    assert response.status_code != 500


def test_get_particle(client: TestClient) -> None:
    """Test case for get_particle

    Get a particle
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/particles/{particleName}".format(particleName="particle_name_example"),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_particle_list(client: TestClient) -> None:
    """Test case for get_particle_list

    Get particle list
    """
    params: Dict[str, str] = {
        "localization": "en",
        "page": "0",
        "keywords": "Chino",
        "sort": "updated_time",
        "order": "desc",
        "status": "any",
        "author": "any",
        "random": "0",
    }
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/particles/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
