from database import SessionLocal
from app.models.conversation_state import ConversationState

db = SessionLocal()


def get_state(user_id):

    conversation = db.get(ConversationState, user_id)

    if conversation:
        return conversation.state

    return None


def set_state(user_id, state):

    conversation = db.get(ConversationState, user_id)

    if conversation is None:

        conversation = ConversationState(
            user_id=user_id,
            state=state
        )

        db.add(conversation)

    else:

        conversation.state = state

    db.commit()


def clear_state(user_id):

    conversation = db.get(ConversationState, user_id)

    if conversation:

        conversation.state = None
        db.commit()