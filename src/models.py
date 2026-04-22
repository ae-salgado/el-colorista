# models.py

from pydantic import BaseModel, Field

class ColorModel(BaseModel):
    hex_code: str = Field(..., pattern=r'^#[A-Fa-f0-9]{6}$')
    hls: tuple[float, float, float]
    emotions: list[str]
    vibe: list[str]

class PaletteResult(BaseModel):
    image_path: str
    colors: list[ColorModel]
    description: str | None = None  # only populated with --vibe