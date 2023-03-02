import argparse
import sys
from bin import get_omniprocesses, get_omnielements, reformat_csv_result, run_sf_query, delete_records
import os
from bin.bcolors import bcolors as clr


def check_dir():
    if not os.path.exists("bin/temp"):
        os.mkdir("bin/temp")


def add_args():
    parser = argparse.ArgumentParser(
        prog='Vlocity Clean Versions',
        description='Clean unused versions from Org and keep -n only',
    )

    parser.add_argument("-u", "--user",
                        help="Target Org username or sfdx alias",
                        required=True)
    parser.add_argument("-t", "--type",
                        help="which elements will you remove the version, \'os\' \'ip\' \'all\' ",
                        required=True)
    parser.add_argument("-c", "--count",
                        help="how many versions to leave on target Org excluding Activated Version",
                        required=True)

    return parser


def get_args(parser):
    result_args = {}
    args = parser.parse_args()
    result_args['user'] = args.user
    result_args['type'] = args.type
    result_args['count'] = args.count

    return result_args


def main():
    parser = add_args()
    args = get_args(parser)  # get arguments from user command input
    check_dir()  # check directory where csv results will be saved

    get_omniprocesses.retrieve_data(args)  # get omniprocess records from target Org
    reformat_csv_result.reformat(args)  # analyse which versions leave to delete
    get_omnielements.retrieve_data(args)  # get omniprocesselements records from target Org

    delete_records.delete(args)  # delete records from csv files with IDs

    print(clr.OKGREEN + ">> Deleting Versions from Org ended successful" + clr.ENDC)


if __name__ == '__main__':
    main()
