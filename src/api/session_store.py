class SessionStore:
    def __init__(self):
        self.repositories = {}

    def save(self, session_id, engine):
        self.repositories[session_id] = engine

    def get(self, session_id):
        return self.repositories.get(session_id)