from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def popToInt(lst: list) -> list:
    """converts population from string to int"""
    d = {
        'k': 1000,
        'M': 1000000,
    }

    result = []
    for text in lst:
        num, magnitude = text[:-1], text[-1]
        result.append(int(float(num) * d[magnitude]))
    return result


def plot_country(df, country: str):
    """plots country data"""
    data = df[df["country"] == country].drop(columns="country")
    if data.empty:
        raise Exception(f"No data found for country: {country}")
    x = data.columns.astype(int).tolist()
    y = popToInt(data.values.flatten().tolist())
    plt.plot(x, y, label=country)


def main():
    df = load("population_total.csv")

    # data looks like this:
    #
    # country	1800	1801	1802	<- columns names
    # France	34.0	32.3	36.1	<- values

    plot_country(df, "Singapore")
    plot_country(df, "France")

    ax = plt.gca()
    ax.set_xlim([1800, 2050])       # set x axis limits
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(
            lambda x, _: f'{x/1_000_000:.0f}M'
        ))      # set y axis to use 'M' instead of 1e7

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.savefig("output.png")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
