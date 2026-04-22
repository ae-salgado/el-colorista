import argparse
import ollama
from color_parser import ColorParser
from image_parser import ImageParser
from emotions_lib import color_library
from models import ColorModel, PaletteResult
from display import display_palette


def find_emotion(hue: float) -> dict:
    for data in color_library.values():
        low, high = data["hue-range"]
        if low <= hue <= high:
            return data
    return {"emotions": ["neutral"], "vibe": ["chill"]}


def build_palette(image_path: str, count: int = 6) -> PaletteResult:
    parser = ColorParser()
    hex_colors = ImageParser.get_palette(image_path, count=count)

    colors = []
    for hex_code in hex_colors:
        h, l, s = parser.hex_to_hls(hex_code)
        emotion_data = find_emotion(h)
        colors.append(ColorModel(
            hex_code=hex_code,
            hls=(h, l, s),
            emotions=emotion_data["emotions"],
            vibe=emotion_data["vibe"]
        ))

    return PaletteResult(image_path=image_path, colors=colors)


def add_vibe(result: PaletteResult) -> PaletteResult:
    """Optional — call Ollama to describe the palette"""
    color_list = "\n".join(
        f"- {c.hex_code}: {', '.join(c.emotions)}"
        for c in result.colors
    )

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Senior UI Designer and color strategist. "
                    "Given a palette extracted from a real image, describe "
                    "the overall mood, what kind of brand or product it fits, "
                    "and how you'd use these colors in a UI. Be concise and sharp."
                )
            },
            {
                "role": "user",
                "content": f"Here is the palette extracted from an image:\n{color_list}\n\nDescribe the vibe."
            }
        ]
    )

    result.description = response['message']['content']
    return result


def main():
    arg_parser = argparse.ArgumentParser(description="Colorista — extract palette from any image")
    arg_parser.add_argument("image", help="Path to image file")
    arg_parser.add_argument("--count", type=int, default=6, help="Number of colors to extract")
    arg_parser.add_argument("--vibe", action="store_true", help="Add AI description via Ollama")
    args = arg_parser.parse_args()

    print(f"\nReading: {args.image}")
    result = build_palette(args.image, count=args.count)

    if args.vibe:
        print("Asking el colorista...\n")
        result = add_vibe(result)

    display_palette(result)


if __name__ == "__main__":
    main()