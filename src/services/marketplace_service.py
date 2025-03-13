import csv
from collections import defaultdict
from typing import Dict, List, Optional

from ..models.listing import Listing
from ..models.user import User


class MarketplaceService:
    def __init__(self):
        self.users: Dict[str, User] = {}  # username -> User
        self.listings: Dict[int, Listing] = {}  # listing_id -> Listing
        self.category_listings: Dict[str, List[int]] = defaultdict(list)  # category -> [listing_ids]
        self.load_data()

    def load_data(self):
        """Load users and listings from CSV files"""
        try:
            with open('users.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    username = row[0]
                    self.users[username] = User(username)
        except FileNotFoundError:
            pass

        try:
            with open('listings.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    listing_id, title, description, price, category, username = row
                    listing = Listing(title, description, float(price), category, username)
                    listing.id = int(listing_id)
                    self.listings[listing.id] = listing
                    self.users[username.lower()].listings.append(listing.id)
                    self.category_listings[category].append(listing.id)
        except FileNotFoundError:
            pass

    def save_data(self):
        """Save users and listings to CSV files"""
        with open('users.csv', mode='w') as file:
            writer = csv.writer(file)
            for username in self.users:
                writer.writerow([username])

        with open('listings.csv', mode='w') as file:
            writer = csv.writer(file)
            for listing in self.listings.values():
                writer.writerow([listing.id, listing.title, listing.description, listing.price, listing.category, listing.username])

    def register_user(self, username: str) -> str:
        """Register a new user"""
        if username.lower() in self.users:
            return "Error - user already existing"
        
        self.users[username.lower()] = User(username)
        self.save_data()
        return "Success"

    def create_listing(self, username: str, title: str, description: str, price: float, category: str) -> str:
        """Create a new listing"""
        if username.lower() not in self.users:
            return "Error - unknown user"

        listing = Listing(title, description, price, category, username)
        self.listings[listing.id] = listing
        self.users[username.lower()].listings.append(listing.id)
        self.category_listings[category].append(listing.id)
        self.save_data()
        
        return str(listing.id)

    def delete_listing(self, username: str, listing_id: int) -> str:
        """Delete a listing"""
        if listing_id not in self.listings:
            return "Error - listing does not exist"
        
        listing = self.listings[listing_id]
        if listing.username.lower() != username.lower():
            return "Error - listing owner mismatch"

        # Remove from all collections
        self.category_listings[listing.category].remove(listing_id)
        self.users[username.lower()].listings.remove(listing_id)
        del self.listings[listing_id]
        self.save_data()
        
        return "Success"

    def get_listing(self, username: str, listing_id: int) -> str:
        """Get details of a specific listing"""
        if username.lower() not in self.users:
            return "Error - unknown user"
            
        if listing_id not in self.listings:
            return "Error - not found"
            
        return self.listings[listing_id].to_string()

    def get_category(self, username: str, category: str) -> str:
        """Get all listings in a category"""
        if username.lower() not in self.users:
            return "Error - unknown user"
            
        if category not in self.category_listings or not self.category_listings[category]:
            return "Error - category not found"
            
        # Sort listings by creation time (descending)
        sorted_listings = sorted(
            [self.listings[lid] for lid in self.category_listings[category]],
            key=lambda x: x.created_at,
            reverse=True
        )
        
        return "\n".join(listing.to_string() for listing in sorted_listings)

    def get_top_category(self, username: str) -> str:
        """Get category with most listings"""
        if username.lower() not in self.users:
            return "Error - unknown user"
            
        if not self.category_listings:
            return "Error - no categories found"
            
        # Find the maximum number of listings in any category
        max_count = max(len(listings) for listings in self.category_listings.values())
        
        # Find all categories with the maximum number of listings
        top_categories = [category for category, listings in self.category_listings.items() if len(listings) == max_count]
        
        # Sort the categories lexicographically
        top_categories.sort()
        
        return ", ".join(top_categories)