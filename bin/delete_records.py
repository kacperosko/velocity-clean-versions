import os
import sys

from bin.bcolors import bcolors as clr


def delete(args):
    files = ["omniprocess_records_ids.csv", "omniprocesselement_records_ids.csv"]

    for f in files:
        print(
            clr.OKGREEN + ">> Running ->" + clr.ENDC + f"sf data delete bulk --target-org {args['user']} -s Omniprocess -f ./bin/temp/" + f)
        try:
            if os.system(f"sf data delete bulk --target-org {args['user']} -s Omniprocess -f ./bin/temp/" + f) == 0:
                print(clr.OKGREEN + ">> Deleting ended successfully" + clr.ENDC)
            else:
                raise Exception("")
        except Exception as e:
            print(e)
            print(clr.WARNING + ">> Error during deleting records" + clr.ENDC)


if __name__ == "__main__":
    delete({})
