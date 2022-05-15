from dataclasses import dataclass

@dataclass(init=True, repr=True)
class Review:
    title: str
    rating: float
    body: str
