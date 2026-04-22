# image_parser.py

from colorthief import ColorThief

class ImageParser:

    @staticmethod
    def get_palette(image_path: str, count: int = 6) -> list[str]:
        """Extract N real colors from the image as hex codes"""
        ct = ColorThief(image_path)
        palette = ct.get_palette(color_count=count, quality=1)
        return ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in palette]