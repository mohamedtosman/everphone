import pytest
from gift_planner import app, model


@pytest.fixture
def client():
    return app.test_client()

def assign_gift(client, name):
    return client.post('/gifts/' + name)

def test_gift_assigned_successfully(client):
    """
    Test gift assigned to that specific employee successfully
    :param client:
    :return:
    """
    res = assign_gift(client, 'oliver')
    gift = model.Gift.query.filter_by(name="netflix card").first()

    assert gift.employee_name == "oliver"
    assert gift.name == "netflix card"
    assert res.status_code == 200

def test_gift_already_assigned(client):
    """
    Test gift already assigned to employee
    :param client:
    :return:
    """
    res = assign_gift(client, 'oliver')

    assert res.status_code == 403

def test_employee_not_exist(client):
    """
    Test employee does not exist
    :param client:
    :return:
    """
    res = assign_gift(client, 'NotAnEmployee')

    assert res.status_code == 404