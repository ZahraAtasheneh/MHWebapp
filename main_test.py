from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_messages():
    response = client.get("/api/messages")
    assert response.status_code == 200
    assert response.json() == {
        "messages": [
            {"type": "therapist", "messageText": "What's on your mind?", "codes": ["Open question"]},
            {"type": "patient", "messageText": "I'm so scared for tonight", "codes": ["Current anxiety", "Event"]},
            {"type": "therapist", "messageText": "Tell me about your childhood", "codes": ["Personal history"]},
            {"type": "patient", "messageText": "I had a traumatic experience when I was young", "codes": ["Trauma", "Personal history"]},
            {"type": "therapist", "messageText": "How does that make you feel?", "codes": ["Emotions"]},
            {"type": "patient", "messageText": "It makes me feel anxious and angry", "codes": ["Anxiety", "Anger", "Emotions"]},
            {"type": "therapist", "messageText": "Have you discussed this with anyone?", "codes": ["Support system"]},
            {"type": "patient", "messageText": "Yes, I've talked to my best friend about it", "codes": ["Support system"]},
            {"type": "therapist", "messageText": "Let's practice some relaxation techniques", "codes": ["Therapeutic intervention"]},
            {"type": "patient", "messageText": "Okay, I'm willing to try", "codes": ["Willingness", "Therapeutic intervention"]}
        ]
    }

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
    assert len(response.json()["messages"]) == 11

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
    assert response.json()["messages"][0]["type"] == "patient"

def test_delete_message():
    response = client.delete("/api/messages/0")
    assert response.status_code == 200
    assert response.json() == {
        "type": "therapist",
        "messageText": "What's on your mind?",
        "codes": ["Open question"]
    }
    assert len(response.json()["messages"]) == 9
