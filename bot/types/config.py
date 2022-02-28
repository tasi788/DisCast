from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Config:
    @dataclass_json
    @dataclass
    class Bot:
        token: str = field(default=None, repr=True)

    bot: Bot = Bot
    