"""
linalg_viz.py
Makine Öğrenmesi için Lineer Cebir kursu için paylaşılan çizim yardımcıları.
Bilinçli olarak küçük ve az bağımlılıklı tutulmuştur (yalnızca numpy + matplotlib).
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_vectors_2d(vectors, colors=None, labels=None, ax=None, lim=None):
    """2B vektör kümesini orijinden çıkan oklar olarak çiz.

    vectors : (2,) dizi-benzeri nesnelerden oluşan yinelenebilir
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 5))
    vectors = [np.asarray(v, dtype=float) for v in vectors]
    n = len(vectors)
    colors = colors or [f"C{i}" for i in range(n)]
    for i, v in enumerate(vectors):
        ax.annotate(
            "", xy=(v[0], v[1]), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=colors[i], lw=2),
        )
        if labels:
            ax.text(v[0] * 1.05, v[1] * 1.05, labels[i], color=colors[i], fontsize=12)
    if lim is None:
        m = max(1.0, max(np.abs(np.concatenate(vectors))) * 1.2)
        lim = (-m, m)
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.axhline(0, color="grey", lw=0.8)
    ax.axvline(0, color="grey", lw=0.8)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    return ax


def plot_transformation(A, ax=None, grid_range=3):
    """2x2 bir A matrisinin birim ızgarayı ve birim çemberi nasıl deforme ettiğini göster."""
    A = np.asarray(A, dtype=float)
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 5))

    # bir çizgi ızgarasını dönüştür
    rng = np.arange(-grid_range, grid_range + 1)
    t = np.linspace(-grid_range, grid_range, 50)
    for k in rng:
        # önce dikey sonra yatay çizgiler
        for line in (np.array([np.full_like(t, k), t]),
                     np.array([t, np.full_like(t, k)])):
            out = A @ line
            ax.plot(out[0], out[1], color="C0", lw=0.7, alpha=0.6)

    # birim çember -> elips
    th = np.linspace(0, 2 * np.pi, 200)
    circle = np.array([np.cos(th), np.sin(th)])
    ell = A @ circle
    ax.plot(circle[0], circle[1], "--", color="grey", lw=1, label="birim çember")
    ax.plot(ell[0], ell[1], color="C3", lw=2, label="görüntü")

    ax.axhline(0, color="grey", lw=0.8)
    ax.axvline(0, color="grey", lw=0.8)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend(loc="upper right", fontsize=9)
    return ax


def check(name, mine, reference, atol=1e-8):
    """Sıfırdan elde edilen bir sonuç ile kütüphane sonucu arasındaki karşılaştırmayı düzgün biçimde yazdır."""
    mine = np.asarray(mine)
    reference = np.asarray(reference)
    ok = np.allclose(mine, reference, atol=atol)
    flag = "PASS" if ok else "FAIL"
    err = np.max(np.abs(mine - reference)) if mine.shape == reference.shape else float("nan")
    print(f"[{flag}] {name:<32} max|Δ| = {err:.2e}")
    return ok
