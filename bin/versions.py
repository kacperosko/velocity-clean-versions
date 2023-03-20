import os
import sys

import simple_salesforce
import bin.sfdx
from bin._settings import clr, TEMP_CSV_DIR
from bin.reformat_csv_result import reformat



def get_omniprocesselements(sf, dataframe):
    # omniprocess = get_file("Omniprocess_get_bulk.csv")
    omniprocess_ids = tuple(dataframe['Id'].values.tolist())
    if len(omniprocess_ids) == 0:
        clr.print_info(">> No parent Omniprocesses to query OmniProcessElement")
        return False

    QUERY = f"SELECT Id FROM OmniProcessElement WHERE OmniProcessId IN {omniprocess_ids}"

    df = sf.get_bulk(query=QUERY, s_object="OmniProcessElement",
                     file_name="omniprocesselement_records_ids.csv")
    return df


def get_omniprocesses(element_type=None, sf: bin.sfdx.SalesforceCommands = None, count=3):
    if element_type == 'all':
        OMNIPROCESS_TYPE = '\'OmniScript\', \'Integration Procedure\''
    elif element_type == 'os':
        OMNIPROCESS_TYPE = '\'OmniScript\''
    elif element_type == 'ip':
        OMNIPROCESS_TYPE = '\'Integration Procedure\''
    else:
        print(clr.FAIL + f'invalid value for \'type\': {element_type}' + clr.ENDC)
        sys.exit()

    QUERY = f"SELECT Id, Name, Type, VersionNumber, IsActive FROM Omniprocess WHERE OmniProcessType IN ({OMNIPROCESS_TYPE})"

    result = sf.get_bulk(query=QUERY, s_object="Omniprocess")
    if result is None:
        clr.print_error(">> No records retrieved")
        sys.exit()
    df = reformat(count=count)  # analyse which versions leave to delete
    return df


def delete_omniprocesses(sf: bin.sfdx.SalesforceCommands):
    metadata = {"OmniProcess": "omniprocess_records_ids.csv"}

    print(clr.OKBLUE + ">> Starting deleting record process" + clr.ENDC)
    for Sobject, file in metadata.items():
        sf.delete_bulk(s_object=Sobject, path=os.path.join(TEMP_CSV_DIR, file))


def delete_omniprocesselements(sf: bin.sfdx.SalesforceCommands):
    metadata = {"OmniProcessElement": "omniprocesselement_records_ids.csv"}

    print(clr.OKBLUE + ">> Starting deleting record process" + clr.ENDC)
    for Sobject, file in metadata.items():
        sf.delete_bulk(s_object=Sobject, path=os.path.join(TEMP_CSV_DIR, file))


if __name__ == "__main__":
    get_data_from_org({})
