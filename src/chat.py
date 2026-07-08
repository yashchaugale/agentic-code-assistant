conversation = []


def add_user_message(message):
    conversation.append(
        {
            "role": "user",
            "content": message
        }
    )


def add_ai_message(message):
    conversation.append(
        {
            "role": "assistant",
            "content": message
        }
    )


def get_conversation():
    return conversation