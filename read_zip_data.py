import pandas as pd
import zipfile
import io

def read_csv_from_zip(zip_file, state=None, year=None):
    """
    Reads a CSV file from a zip file, given a state and year. Returns a Pandas DataFrame.
    
    Parameters:
        - zip_file: The name of the zip file to read from.
        - state: The two-letter state code to read from (e.g. "RJ"). Optional.
        - year: The year to read from (e.g. 2003). Optional.
        
    Returns:
        A Pandas DataFrame containing the contents of the CSV file(s).
    """
    zf = zipfile.ZipFile(zip_file)
    
    if state and year:
        filename = f"ETLSINASC.DNRES_{state}_{year}_t.csv"
        if filename in zf.namelist():
            with zf.open(filename) as f:
                df = pd.read_csv(io.StringIO(f.read().decode()), on_bad_lines='skip')
            return df
        else:
            raise ValueError(f"No file found for state '{state}' and year '{year}'.")
    
    elif state:
        dfs = []
        for file in zf.namelist():
            if file.endswith(".csv") and f"_{state}_" in file:
                year = file.split("_")[-2]
                print(year)
                with zf.open(file) as f:
                    df = pd.read_csv(io.StringIO(f.read().decode()), on_bad_lines='skip')
                dfs.append(df)
        if len(dfs) == 0:
            raise ValueError(f"No files found for state '{state}'.")
        else:
            return pd.concat(dfs, ignore_index=True)
    
    elif year:
        dfs = pd.DataFrame()
        for file in zf.namelist():
            if file.endswith(".csv") and f"_{year}_" in file:
                state = file.split("_")[2]
                with zf.open(file) as f:
                    df = pd.read_csv(io.StringIO(f.read().decode()), on_bad_lines='skip')
                dfs = pd.concat([dfs, df], axis=0, ignore_index=True)
        if len(dfs) == 0:
            raise ValueError(f"No files found for year '{year}'.")
        else:
            return dfs
    
    else:
        raise ValueError("At least one of 'state' and 'year' must be specified.")


zip_path = "data/ETLSINASC.zip"

# df = read_csv_from_zip(zip_path, state="RJ", year=2003)
# df.to_csv("data/2003RJ.csv")
# print(df.shape)

# df = read_csv_from_zip(zip_path, state="RJ")
# print(df.shape)

df = read_csv_from_zip(zip_path, year=2003)
print(df.columns)
print(df.RACACOR.value_counts())
print(df.GRAVIDEZ.value_counts())

