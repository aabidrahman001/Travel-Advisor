class MemoryManager:
    def __init__(self):
        self.user_memory = {}
    
    def save_preference(self, user_id, key, value):
        self.user_memory[user_id] = self.user_memory.get(user_id, {})
        self.user_memory[user_id][key] = value
    
    def get_preferences(self, user_id):
        return self.user_memory.get(user_id, {})
