import os
import logging
from pathlib import Path
import pandas as pd
import json
import yaml
from typing import Union

def read_in_file(filename: str, directory=None, **kwargs):

    # TODO: review function (written by me some times ago, but could be refactored in meantime); covert this function to a class
    # TODO: covert this function to a class, can be extended for different file types
    if os.path.isabs(filename):
        if directory is not None:
            logging.info(f'File {filename} is an absolute path, ignoring specified directory {directory}')

    else:
        if directory is None:
            raise Exception(f'File {filename} is not an absolute path, but no directory was specified')
        else:
            filename = os.path.join(directory, filename)

    if not os.path.exists(filename):
        raise Exception(f'File {filename} does not exist')

    logging.info(f'Start loading file {filename}')

    ext = Path(filename).suffix

    if ext == ".parquet":
        df = pd.read_parquet(filename, engine='pyarrow')
    elif ext == ".txt":
        #df = pd.read_csv(filename, sep='\t', encoding='unicode_escape')
        f = open(filename)
        df = f.read()
        f.close()
    elif ext == ".xlsx":
        if kwargs:
            logging.info(f"Loading {kwargs['sheet_name']} sheet")
            df = pd.read_excel(filename, **kwargs)
        else:
            df = pd.ExcelFile(filename)
    elif ext == ".yml" or ext == ".yaml":
        with open(filename, 'r') as stream:
            df = yaml.safe_load(stream)
    elif ext == ".json":
        f = open(filename)
        df = json.load(f)
        f.close()

    logging.info(f'Finished loading file {filename}')

    return df

def write_out_file(data: Union[pd.DataFrame, dict], filename: str, directory=None) -> None:

    # TODO: review function (written by me some times ago, but could be refactored in meantime); 
    # TODO: covert this function to a class, can be extended for different file types
    if os.path.isabs(filename):
        if directory is not None:
            logging.WARN(f'File {filename} is an absolute path, ignoring specified directory {directory}')

    else:
        if directory is None:
            raise Exception(f'File {filename} is not an absolute path, but no directory was specified')
        else:
            filename = os.path.join(directory, filename)

    logging.info(f'Saving output file: {filename}')

    ext = Path(filename).suffix

    if ext == ".csv":
        data.to_csv(filename, sep=";", decimal=",", index=False)
    elif ext == ".parquet":
        datetime_columns = data.select_dtypes(include=["datetime64[ns]"]).columns
        if len(datetime_columns) > 0:
            for column in datetime_columns:
                logging.info(f'Converting column {column} from datetime to date')
            data[column] = pd.to_datetime(data[column]).dt.date
            data.to_parquet(filename, engine='pyarrow', coerce_timestamps='us', allow_truncated_timestamps=True)
    elif ext == ".yml":
        with open(filename, 'w') as outfile:
            yaml.dump(data, outfile, sort_keys=False)
    elif ext == ".txt":
        with open(filename, 'w') as f:
            df_to_str = data.to_string(header=True, index=False)
            f.write(df_to_str)

    logging.info(f'Finished saving output file: {filename}')

def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent