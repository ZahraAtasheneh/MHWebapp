from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_messages():
    response = client.get("/api/messages")
    assert response.status_code == 200
 

def test_create_message():
    response = client.post("/api/messages", json={
        "type": "therapist",
        "messageText": "New message",
        "codes": ["New code"]
    })
    assert response.status_code == 200
    assert response.json() == {
        "type": "therapist",
        "messageText": "New message",
        "codes": ["New code"]
    }
 
def test_update_message():
    response = client.put("/api/messages/0", json={
        "type": "patient",
        "messageText": "Updated message",
        "codes": ["Updated code"]
    })
    assert response.status_code == 200
    assert response.json() == {
        "type": "patient",
        "messageText": "Updated message",
        "codes": ["Updated code"]
    }


def test_delete_message():
    response = client.delete("/api/messages/0")
    assert response.status_code == 200
 
 
