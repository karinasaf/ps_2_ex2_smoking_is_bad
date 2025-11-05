from pathlib import Path
import pandas as pd

def load_data(filename: str) -> pd.DataFrame:
    """
    Load a CSV file from the 'data' directory using pathlib for portability.

    Parameters
    ----------
    filename : str
        Name of the CSV file (e.g. 'my_data.csv').

    Returns
    -------
    pd.DataFrame
        The loaded DataFrame.
    """
    try:
        base_path = Path(__file__).parent.parent
    except NameError:
        base_path = Path.cwd()

    data_path = base_path / 'data' / filename

    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    return pd.read_csv(data_path)
