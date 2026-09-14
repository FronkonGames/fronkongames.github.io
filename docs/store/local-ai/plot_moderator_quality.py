"""HateCheck F1 by language for Local AI: Moderator docs."""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

MAIN = "#dee2e6"
ACCENT = "#f8c85c"
OUTPUT = Path(r"F:\FronkonGames\Web\content\store\local-ai\moderator_quality.png")

# HateCheck + MHC (2026-09-14), shipped Uint8 model, GPUCompute.
ROWS = [
    ("HateCheck", 0.869, True),
    ("French", 0.880, False),
    ("Dutch", 0.874, False),
    ("Portuguese", 0.872, False),
    ("Spanish", 0.870, False),
    ("Italian", 0.870, False),
    ("German", 0.865, False),
    ("Polish", 0.865, False),
    ("English", 0.860, False),
]

names = [row[0] for row in ROWS]
scores = [row[1] for row in ROWS]
colors = [ACCENT if row[2] else MAIN for row in ROWS]
y = list(range(len(names) - 1, -1, -1))

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 13,
    "text.color": MAIN,
    "axes.labelcolor": MAIN,
    "xtick.color": MAIN,
    "ytick.color": MAIN,
    "axes.edgecolor": MAIN,
})

fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=160)
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)

ax.barh(y, scores, color=colors, height=0.62, zorder=2)

for yi, score, accent in zip(y, scores, (row[2] for row in ROWS)):
    ax.text(
        score + 0.003,
        yi,
        f"{score:.2f}",
        color=ACCENT if accent else MAIN,
        va="center",
        fontsize=12,
        fontweight="bold" if accent else "normal",
    )

ax.set_yticks(y)
ax.set_yticklabels(names)
ax.get_yticklabels()[0].set_color(ACCENT)
ax.get_yticklabels()[0].set_fontweight("bold")
ax.set_xlim(0.80, 0.92)
ax.set_xlabel("F1")
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.02))
ax.set_title("HateCheck + Multilingual HateCheck", color=MAIN, fontsize=16, pad=12, loc="left")

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color(MAIN)
ax.spines["bottom"].set_color(MAIN)
ax.tick_params(length=0)
ax.grid(axis="x", color=MAIN, alpha=0.18, zorder=0)
ax.set_axisbelow(True)

fig.tight_layout()
fig.savefig(OUTPUT, transparent=True, bbox_inches="tight", pad_inches=0.15)
print(OUTPUT)
