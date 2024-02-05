"""
Followed https://stackoverflow.com/questions/65881106/how-to-pytest-a-flask-endpoint and https://flask.palletsprojects.com/en/3.0.x/testing/
"""

import pytest
from server.app import app


@pytest.fixture()
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_get_images(client):
    response = client.get('/api/images')
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert isinstance(data, list)

def test_react_to_image(client):
    image = Image(url='https://images.unsplash.com/photo-1486395130845-ec128138002e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjN8fG9wZW4lMjBzb3VyY2V8ZW58MHx8MHx8fDA%3D')
    db.session.add(image)
    db.session.commit()

    reaction_data = {'image_id': image.id, 'thumbs_up': 1, 'thumbs_down': 0}
    response = client.post('/api/react', json=reaction_data)
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert data['message'] == 'Reaction recorded successfully'
