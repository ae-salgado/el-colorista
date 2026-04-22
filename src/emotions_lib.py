# emotions_lib.py

# We use ranges based on the 360-degree HLS color wheel
color_library = {
    "reds": {
        "emotions": ["passion", "urgency", "danger", "energy"],
        "vibe": ["intense", "dynamic", "bold"],
        "hue-range": [0, 20],
    },
    "oranges": {
        "emotions": ["creativity", "friendly", "youthful", "enthusiasm"],
        "vibe": ["vibrant", "inviting", "stimulating"],
        "hue-range": [21, 50],
    },
    "yellows": {
        "emotions": ["optimism", "clarity", "warmth", "attention"],
        "vibe": ["radiant", "uplifting", "illuminating"],
        "hue-range": [51, 80],
    },
    "greens": {
        "emotions": ["growth", "health", "nature", "prosperity"],
        "vibe": ["balanced", "refreshing", "harmonious"],
        "hue-range": [81, 160],
    },
    "blues": {
        "emotions": ["trust", "security", "calm", "intelligence"],
        "vibe": ["professional", "composed", "reliable"],
        "hue-range": [161, 260],
    },
    "purples": {
        "emotions": ["luxury", "mystery", "spiritual", "wisdom"],
        "vibe": ["sophisticated", "enigmatic", "elevated"],
        "hue-range": [261, 320],
    },
    "pinks/magentas": {
        "emotions": ["romance", "compassion", "playful"],
        "vibe": ["delicate", "tender", "expressive"],
        "hue-range": [321, 359],
    }
}