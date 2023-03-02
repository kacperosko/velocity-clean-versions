import os
from bin.bcolors import bcolors as clr


def run_query(query="None", user="", result_path="result.csv"):
    print(clr.OKBLUE + ">> Running -> " + clr.ENDC + f"sf data query -q \"{query}\" -r=csv --target-org=\'{user}\' > " + result_path)
    os.system(f"sf data query -q \"{query}\" -r=csv --target-org=\'{user}\' > " + result_path)
    print(clr.OKGREEN + ">> Query ended successfully" + clr.ENDC)


if __name__ == "__main__":
    run_query()