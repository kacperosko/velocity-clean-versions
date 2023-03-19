# import os
# from bin.run_sf_query import run_query
# from bin.printcolors import PrintColors as clr
#
#
# def retrieve_data(user=None, element_type=None):
#     if element_type == 'all':
#         OMNIPROCESS_TYPE = '\'OmniScript\', \'Integration Procedure\''
#     elif element_type == 'os':
#         OMNIPROCESS_TYPE = '\'OmniScript\''
#     elif element_type == 'ip':
#         OMNIPROCESS_TYPE = '\'Integration Procedure\''
#     else:
#         print(clr.FAIL + f'invalid value for \'type\': {element_type}' + clr.ENDC)
#         sys.exit()
#
#     QUERY = f"SELECT Id, Name, Type, VersionNumber, IsActive FROM Omniprocess WHERE OmniProcessType IN ({OMNIPROCESS_TYPE})"
#
#     run_query(query=QUERY, user=user, result_path=os.path.join("./", "bin", "temp", "omniprocess_records.csv"))
#
#
# if __name__ == "__main__":
#     get_data_from_org({})
