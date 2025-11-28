class SessionManager:
    def __init__(self):
        self.sessions = {}
    
    def create_session(self, user_id):
        self.sessions[user_id] = {}
    
    def get_session(self, user_id):
        return self.sessions.get(user_id, {})
