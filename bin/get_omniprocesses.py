import os
from bin.run_sf_query import run_query


def retrieve_data(args):
    if args['type'] == 'all':
        OMNIPROCESS_TYPE = '\'OmniScript\', \'Integration Procedure\''
    if args['type'] == 'os':
        OMNIPROCESS_TYPE = '\'OmniScript\''
    if args['type'] == 'ip':
        OMNIPROCESS_TYPE = '\'Integration Procedure\''

    QUERY = f"SELECT Id, Name, Type, VersionNumber, IsActive FROM Omniprocess WHERE OmniProcessType IN ({OMNIPROCESS_TYPE})"

    run_query(query=QUERY, user=args['user'], result_path=os.path.join("./", "bin", "temp", "omniprocess_records.csv"))


if __name__ == "__main__":
    get_data_from_org(args)
