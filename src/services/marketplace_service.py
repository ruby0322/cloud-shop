from collections import defaultdict
from typing import Dict, List, Optional

from ..models.listing import Listing
from ..models.user import User


class MarketplaceService:
    def __init__(self):
        self.users: Dict[str, User] = {}  # username -> User
        self.listings: Dict[int, Listing] = {}  # listing_id -> Listing
        self.category_listings: Dict[str, List[int]] = defaultdict(list)  # category -> [listing_ids]

    def register_user(self, username: str) -> str:
        """Register a new user"""
        if username.lower() in self.users:
            return "Error - user already existing"
        
        self.users[username.lower()] = User(username)
        return "Success"

    def create_listing(self, username: str, title: str, description: str, price: float, category: str) -> str:
        """Create a new listing"""
        if username.lower() not in self.users:
            return "Error - unknown user"

        listing = Listing(title, description, price, category, username)
        self.listings[listing.id] = listing
        self.users[username.lower()].listings.append(listing.id)
        self.category_listings[category].append(listing.id)
        
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
            
        # Find category with most listings
        top_category = max(
            self.category_listings.items(),
            key=lambda x: len(x[1])
        )[0]
        
        return top_category 