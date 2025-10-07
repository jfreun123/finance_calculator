import matplotlib

matplotlib.use("TkAgg")
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, sim):
        self.__sim = sim
        self.__starting_age = sim.get_starting_age()
        self.__age_axis = range(
            self.__starting_age, sim.get_total_iters() + self.__starting_age + 1
        )

    def prettify_graph(self, ax, title="Results"):
        ax.set_title(title)
        ax.set_xlabel("Age")
        ax.set_ylabel("Net Worth")

        fmt = "${x:,.0f}"
        tick = mtick.StrMethodFormatter(fmt)
        ax.yaxis.set_major_formatter(tick)
        ax.tick_params(axis="x", rotation=25)

    def plot_all(self, number_of_simulations):
        points_gen = self.__sim.many_simulations(number_of_simulations)
        last_numbers = []

        # Create 1 figure with 2 subplots (side by side)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # ----- Left: all simulated paths -----
        self.prettify_graph(ax1, title=f"{number_of_simulations} Simulations")
        for sample in points_gen:
            last_numbers.append(sample[-1])
            ax1.plot(self.__age_axis, sample, alpha=0.3, color="gray")

        ax1.set_title(f"{number_of_simulations} Simulations\n")
        ax1.set_xlabel("Age")
        ax1.set_ylabel("Portfolio Value")
        ax1.grid(True, linestyle="--", alpha=0.4)

        # ----- Right: histogram of final values -----
        counts, bins, patches = ax2.hist(
            last_numbers,
            bins=40,
            color="steelblue",
            edgecolor="black",
            alpha=0.7,
            density=False,  # ← don't normalize
        )

        # Convert to percentages
        counts = counts / len(last_numbers) * 100
        ax2.clear()  # clear the old plot

        ax2.bar(
            (bins[:-1] + bins[1:]) / 2,  # bin centers
            counts,
            width=np.diff(bins),
            color="steelblue",
            edgecolor="black",
            alpha=0.7,
        )

        # Formatting
        ax2.set_ylabel("Percentage of Simulations")
        ax2.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
        fmt = "${x:,.0f}"
        ax2.xaxis.set_major_formatter(mtick.StrMethodFormatter(fmt))

        # Mean and percentile lines
        mean_val = np.mean(last_numbers)
        p5, p50, p95 = np.percentile(last_numbers, [5, 50, 95])
        ax2.axvline(
            mean_val,
            color="darkblue",
            linestyle="--",
            linewidth=2,
            label=f"Mean = {mean_val:,.0f}",
        )
        ax2.axvline(
            p50,
            color="green",
            linestyle="--",
            linewidth=2,
            label=f"Median = {p50:,.0f}",
        )
        ax2.axvline(
            p5, color="red", linestyle=":", linewidth=1.5, label=f"5th %ile = {p5:,.0f}"
        )
        ax2.axvline(
            p95,
            color="red",
            linestyle=":",
            linewidth=1.5,
            label=f"95th %ile = {p95:,.0f}",
        )

        ax2.set_title("Distribution of Final Portfolio Values")
        ax2.set_xlabel("Final Value ($)")
        ax2.legend()
        ax2.grid(True, linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.show()
