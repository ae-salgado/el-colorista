import colorsys

class ColorParser:

    @staticmethod
    def hex_to_hls(hex_code: str) -> tuple[float, float, float]:
        hex_code = hex_code.lstrip('#')
        r, g, b = tuple(int(hex_code[i:i+2], 16) / 255.0 for i in (0, 2, 4))
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return (h * 360, s * 100, l * 100)