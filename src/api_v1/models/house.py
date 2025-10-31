"""my house model"""

from pydantic import BaseModel

class House(BaseModel):
    """House model"""
    title: str
    city: str
    image_path: str
    available_units: int
    wifi: bool
    laundry: bool


my_houses: dict[id, House] = {
    1: House(
        title="Michas Ferienwohnungen",
        city="Lengerich",
        image_path="somewhere.png",
        available_units=12,
        wifi=True,
        laundry=False
    )
}
