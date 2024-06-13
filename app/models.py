from dataclasses import dataclass

@dataclass
class SeasonalFlavor:
    id: int
    name: str
    description: str
    availability: str

@dataclass
class Ingredient:
    id: int
    name: str
    quantity: int

@dataclass
class CustomerSuggestion:
    id: int
    flavor_name: str
    customer_name: str
    allergies: str

@dataclass
class Allergen:
    id: int
    name: str

@dataclass
class CartItem:
    id: int
    product_name: str

