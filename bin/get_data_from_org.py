import os


def retrieve_data(args):
    if args['type'] == 'all':
        OMNIPROCESSTYPE = '\'OmniScript\', \'Integration Procedure\''
    if args['type'] == 'os':
        OMNIPROCESSTYPE = '\'OmniScript\''
    if args['type'] == 'ip':
        OMNIPROCESSTYPE = '\'Integration Procedure\'',
    os.mkdir("temp")
    QUERY = f"SELECT Id, Name, Type, VersionNumber, IsActive FROM Omniprocess WHERE OmniProcessType IN ({OMNIPROCESSTYPE})"

    os.system(f"sfdx force:data:soql:query -q  \"{QUERY}\" -r=csv -u=\'{args['user']}\' > " + os.path.join("./", "bin",
                                                                                                           "temp",
                                                                                                           "omniprocess_records.csv"))


if __name__ == "__main__":
    get_data_from_org(args)
