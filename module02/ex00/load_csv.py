import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """Takes a path as argument, writes the dimensions
    of the data set and returns it"""

    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except Exception as e:
        print(e)
        return []
