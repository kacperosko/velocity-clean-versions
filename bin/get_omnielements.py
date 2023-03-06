import pandas as pd
import os
from bin.reformat_csv_result import get_file
from bin.run_sf_query import run_query


def retrieve_data(user=None):
    omniprocess = get_file("omniprocess_records_ids.csv")
    omniprocess_ids = tuple(omniprocess['Id'].values.tolist())

    QUERY = f"SELECT Id FROM OmniProcessElement WHERE OmniProcessId IN {omniprocess_ids}"

    run_query(query=QUERY, user=user, result_path=os.path.join("./", "bin", "temp", "omniprocesselement_records_ids.csv"))


if __name__ == "__main__":
    retrieve_data()