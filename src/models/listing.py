from datetime import datetime


class Listing:
    _next_id = 100001  # Starting ID for listings

    def __init__(self, title: str, description: str, price: float, category: str, username: str):
        self.id = Listing._next_id
        Listing._next_id += 1
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.username = username
        self.created_at = datetime.now()

    def to_string(self) -> str:
        """Convert listing to string format as per specification"""
        return f"{self.title}|{self.description}|{self.price:.0f}|{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}|{self.category}|{self.username}" 