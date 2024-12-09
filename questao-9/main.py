class SocialNetwork:
    def __init__(self):
        self.user_profiles = {}

    def add_user(self, username, profile_info):
        self.user_profiles[username] = profile_info

    def get_user_profile(self, username):
        return self.user_profiles.get(username, "Perfil não encontrado")

network = SocialNetwork()
network.add_user("alice", {"name": "Alice", "age": 30, "location": "Wonderland"})
network.add_user("bob", {"name": "Bob", "age": 25, "location": "Builderland"})

print(network.get_user_profile("alice"))  
print(network.get_user_profile("charlie")) 
