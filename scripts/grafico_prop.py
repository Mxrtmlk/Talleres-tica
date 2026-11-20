import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

csv, out = sys.argv[1], sys.argv[2]
c = pd.read_csv(csv)

g = c.groupby("r3")["pobreza_multi"].agg(n="size", pobres=lambda s: (s == "Pobre").sum())
g["pct"] = g["pobres"] / g["n"] * 100
orden = ["No indígena", "Indígena"]
g = g.loc[orden]
total_pct = (c["pobreza_multi"] == "Pobre").mean() * 100


def miles(x):
    return f"{x:,.0f}".replace(",", ".")


fig, ax = plt.subplots(figsize=(8.5, 5.2), dpi=130)
colores = ["#8fb3d9", "#e8a77a"]
barras = ax.bar(
    [f"{k}\n(n = {miles(g.loc[k, 'n'])})" for k in orden],
    g["pct"], color=colores, width=0.55,
)
for b, k in zip(barras, orden):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() - 1.0,
            f"{g.loc[k, 'pct']:.1f} %".replace(".", ","), ha="center", va="top",
            fontsize=14, fontweight="bold", color="#111111")

ax.axhline(total_pct, color="#555555", linestyle="--", linewidth=1)
ax.text(0.5, total_pct + 0.5, f"Total: {total_pct:.1f} %".replace(".", ","), ha="center",
        fontsize=10, color="#555555")

ax.set_ylim(0, 30)
ax.set_ylabel("Registros en pobreza multidimensional (%)", fontsize=11)
ax.set_title("Porcentaje en pobreza multidimensional\nsegún pertenencia a pueblo indígena (r3)",
             fontsize=13, fontweight="bold")
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f} %"))
ax.grid(axis="y", color="#dddddd")
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, "Fuente: Casen 2024, dataset del curso (212.471 registros).",
         fontsize=8, color="#666666")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(out, facecolor="white")
print(g.round(2).to_string())
print("total", round(total_pct, 2))
