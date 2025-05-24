from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd


def main():
    gnp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_df = load("life_expectancy_years.csv")

    # drop NA from data
    combined = pd.DataFrame({
        "GNP": gnp_df["1900"],
        "Life": life_df["1900"]
    }).dropna()

    x = combined["GNP"].tolist()
    y = combined["Life"].tolist()

    plt.scatter(x, y)
    plt.xscale("log")

    ax = plt.gca()
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(
            lambda x, _: f'{x/1_000:.0f}k'
        ))

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.savefig("output.png")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
