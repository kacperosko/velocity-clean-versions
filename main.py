import argparse
import sys
from bin import get_data_from_org, get_omnielements, reformat_csv_result


def add_args():
    parser = argparse.ArgumentParser(
        prog='VlocityCleanVersions',
        description='Clean unused versions from Org and keep -n only',
    )

    parser.add_argument("-u", "--user", help="Target Org username or sfdx alias", required=True)
    parser.add_argument("-t", "--type", help="which elements will you remove the version, \'os\' \'ip\' \'all\' ",
                        required=True)
    parser.add_argument("-c", "--count", help="how many versions to leave on target Org", required=True)

    return parser


def get_args(parser):
    result = {}
    args = parser.parse_args()
    result['user'] = args.user
    result['type'] = args.type
    result['count'] = args.count

    return result


def main():

    parser = add_args()
    args = get_args(parser)

    get_data_from_org.retrieve_data(args)
    reformat_csv_result.reformat(args)
    get_omnielements.retrieve_data(args)


if __name__ == '__main__':
    main()
