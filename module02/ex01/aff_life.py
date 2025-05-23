from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():
	df = load("life_expectancy_years.csv")
	country = "France"
	data = df[df["country"] == country].drop(columns="country")
	
	x = data.columns
	y = data.values.flatten()

	print(x)
	print(y)

	plt.plot(x, y)
	plt.savefig("output.png")

	# sns.displot(df[df["country"] == country])
	# plt.savefig("output.png")

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(e)