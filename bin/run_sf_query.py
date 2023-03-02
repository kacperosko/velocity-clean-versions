import os


def run_query(query="None", user="", result_path="result.csv"):

    os.system(f"sf data query -q \"{query}\" -r=csv --target-org=\'{user}\' > " + result_path)


if __name__ == "__main__":
    run_query()