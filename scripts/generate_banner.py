from pathlib import Path

from utils import load_config, ensure_assets
from svg_builder import SVGBuilder
from terminal import draw_terminal

cfg = load_config()
theme = cfg["theme"]["dark"]
layout = cfg["layout"]

ensure_assets()

banner = SVGBuilder(
    layout["width"],
    layout["height"],
)

# ======================================================
# Background
# ======================================================

banner.rect(
    0,
    0,
    layout["width"],
    layout["height"],
    theme["background"],
)

# ======================================================
# Header
# ======================================================

draw_terminal(
    banner,
    cfg,
    theme,
)

# ======================================================
# Portrait
# ======================================================

banner.outlined_rect(
    60,
    90,
    220,
    220,
    "#111827",
    theme["primary"],
    3,
    18,
)

banner.text(
    112,
    205,
    "PORTRAIT",
    18,
    theme["muted"],
    "700",
)

# ======================================================
# Availability
# ======================================================

banner.circle(
    75,
    340,
    6,
    theme["success"],
)

banner.text(
    90,
    346,
    "AVAILABLE",
    14,
    theme["muted"],
)

# ======================================================
# Main Content
# ======================================================

x = 340

banner.text(
    x,
    120,
    cfg["name"],
    42,
    theme["primary"],
    "700",
)

banner.text(
    x,
    165,
    cfg["role"],
    22,
    theme["text"],
)

banner.text(
    x,
    205,
    "📍 " + cfg["location"],
    18,
    theme["muted"],
)

# ======================================================
# Tech Chips
# ======================================================

chip_x = x
chip_y = 230

for tech in cfg["focus"]:

    width = banner.chip(
        chip_x,
        chip_y,
        tech,
        theme["border"],
        theme["primary"],
    )

    chip_x += width + 12

# ======================================================
# Status
# ======================================================

banner.circle(
    x,
    305,
    6,
    theme["success"],
)

banner.text(
    x + 18,
    311,
    cfg["status"],
    18,
    theme["success"],
)

# ======================================================
# Save
# ======================================================

banner.save(
    Path("assets") / "dark.svg"
)

print("✓ Banner generated successfully!")