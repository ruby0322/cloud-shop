class User:
    def __init__(self, username: str):
        self.username = username.lower()  # Store username in lowercase for case-insensitive comparison
        self.listings = []  # List of listing IDs created by this user

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username.lower() == other.username.lower()

    def __hash__(self):
        return hash(self.username.lower()) 