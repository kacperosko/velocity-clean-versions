import os
import simple_salesforce
import bin.sfdx
from bin._settings import clr, TEMP_CSV_DIR
from bin.reformat_csv_result import reformat


def __get_omniprocesses(sf, omniprocess_type, count):
    QUERY = f"SELECT Id, Name, Type, VersionNumber, IsActive FROM Omniprocess WHERE OmniProcessType IN ({omniprocess_type})"

    sf.get_bulk(query=QUERY, s_object="Omniprocess")
    df = reformat(count=count)
    return df


def __get_omniprocesselement(sf, dataframe):
    # omniprocess = get_file("Omniprocess_get_bulk.csv")
    omniprocess_ids = tuple(dataframe['Id'].values.tolist())
    if len(omniprocess_ids) == 0:
        clr.print_info(">> No parent Omniprocesses to query OmniProcessElement")
        return False

    QUERY = f"SELECT Id FROM OmniProcessElement WHERE OmniProcessId IN {omniprocess_ids}"

    df = sf.get_bulk(query=QUERY, s_object="OmniProcessElement",
                     file_name="omniprocesselement_records_ids.csv")
    return df


def get_vlocity_versions(element_type=None, sf: bin.sfdx.SalesforceCommands = None, count=3):
    if element_type == 'all':
        OMNIPROCESS_TYPE = '\'OmniScript\', \'Integration Procedure\''
    elif element_type == 'os':
        OMNIPROCESS_TYPE = '\'OmniScript\''
    elif element_type == 'ip':
        OMNIPROCESS_TYPE = '\'Integration Procedure\''
    else:
        print(clr.FAIL + f'invalid value for \'type\': {element_type}' + clr.ENDC)
        sys.exit()

    omniprocesses = __get_omniprocesses(sf=sf, omniprocess_type=OMNIPROCESS_TYPE, count=count)
    __get_omniprocesselement(sf=sf, dataframe=omniprocesses)


def delete_vlocity_versions(sf: bin.sfdx.SalesforceCommands):
    metadata = {"OmniProcess": "omniprocess_records_ids.csv",
                "OmniProcessElement": "omniprocesselement_records_ids.csv"}
    print(clr.OKBLUE + ">> Starting deleting record process" + clr.ENDC)
    for Sobject, file in metadata.items():
        sf.delete_bulk(s_object=Sobject, path=os.path.join(TEMP_CSV_DIR, file))


if __name__ == "__main__":
    get_data_from_org({})
