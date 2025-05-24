from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("life_expectancy_years.csv")

    country = "Singapore"
    data = df[df["country"] == country]		# Filter df to get country
    if data.empty:
        raise Exception(f"No data found for country: {country}")

    # data looks like this:
    #
    # country	1800	1801	1802	<- columns names
    # France	34.0	32.3	36.1	<- values

    data = data.drop(columns="country")         # Drop 'country' column
    x = data.columns.astype(int).tolist()	    # Assign column names to x
    y = data.values.flatten()		        # Assign values to y, make it 1D array

    plt.plot(x, y)
    plt.title(country + " Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.savefig("output.png")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
