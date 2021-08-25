from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Train:
    sort_index: str = field(init=False, repr=False)
    departure_time: str
    direction_id: int
    destination: str
    train_number: int
    status: str
    track: str = "TBD"

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.departure_time)

    def __str__(self) -> str:
        return f"Departure Time: {self.departure_time} \n" \
               f"Destination: {self.destination} \n" \
               f"Train #: {self.train_number} \n" \
               f"Status: {self.status} \n" \
               f"Track: {self.track} \n"