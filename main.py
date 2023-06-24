from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example messages and codes
messages = [
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

class Message(BaseModel):
    type: str
    messageText: str
    codes: list[str]

@app.get("/api/messages")
def get_messages():
    return messages

@app.post("/api/messages")
def create_message(message: Message):
    messages.append(message)
    return message

@app.put("/api/messages/{index}")
def update_message(index: int, message: Message):
    if index >= 0 and index < len(messages):
        messages[index] = message
        return message
    else:
        raise HTTPException(status_code=404, detail="Message not found")

@app.delete("/api/messages/{index}")
def delete_message(index: int):
    if index >= 0 and index < len(messages):
        deleted_message = messages.pop(index)
        return deleted_message
    else:
        raise HTTPException(status_code=404, detail="Message not found")
