from dataclasses import dataclass
import os


@dataclass
class Config:
    token: str = os.getenv('TELEGRAM_TOKEN')