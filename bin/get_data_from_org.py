import os


def check_dir():
    if not os.path.exists("bin/temp"):
        os.mkdir("bin/temp")


def retrieve_data(args):
    from bin.run_sf_query import run_query
    if args['type'] == 'all':
        OMNIPROCESSTYPE = '\'OmniScript\', \'Integration Procedure\''
    if args['type'] == 'os':
        OMNIPROCESSTYPE = '\'OmniScript\''
    if args['type'] == 'ip':
        OMNIPROCESSTYPE = '\'Integration Procedure\''

    check_dir()

    QUERY = f"SELECT Id, Name, Type, VersionNumber, IsActive FROM Omniprocess WHERE OmniProcessType IN ({OMNIPROCESSTYPE})"

    run_query(query=QUERY, user=args['user'], result_path=os.path.join("./", "bin", "temp", "omniprocess_records.csv"))


if __name__ == "__main__":
    get_data_from_org(args)
