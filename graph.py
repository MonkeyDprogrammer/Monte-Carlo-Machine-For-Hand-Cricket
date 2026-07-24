import matplotlib.pyplot as plt

method = [
    "Fixed number 10 vs Bowler\n(Random bowler)",
    "Fixed number 10 vs Adaptive Bowler\n(60% Chance to repeat previous num)",
    "Adaptive Batsman vs Adaptive Bowler\n(Avoids previous num but fixed 10)",
    "Adaptive Batsman vs Adaptive Bowler\n(Avoids previous num but always\n       greater than previous num)"
]

s = [90.76, 225.643, 125.032, 139.675]
plt.figure(figsize=(10, 6), dpi=150)
b = plt.barh(method, s, color="#4C72B0")

for b, s in zip(b, s):
    plt.text(
        b.get_width() + 3,         
        b.get_y() + b.get_height()/2,
        f"{s:.1f}",
        va='center'
    )
plt.xlabel("Average Score")
plt.title("Hand Cricket Bot And Its Different Iterations (Monte Carlo Machine)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("results_chart.png", dpi=300, bbox_inches='tight')
plt.show()
