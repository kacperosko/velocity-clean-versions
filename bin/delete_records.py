# import os
# import sys
#
# import bin.sfdx
# from bin._settings import clr, TEMP_CSV_DIR
#
#
# def delete(sf: bin.sfdx.SalesforceCommands):
#     metadata = {"OmniProcess": "omniprocess_records_ids.csv"}#,
#                 #"OmniProcessElement": "omniprocesselement_records_ids.csv"}
#     print(clr.OKBLUE + ">> Starting deleting record process" + clr.ENDC)
#     for Sobject, file in metadata.items():
#         print(
#             clr.OKBLUE + ">> Running ->" + clr.ENDC + f"sf data delete bulk --target-org {user} -s {Sobject} -f ./bin/temp/" + file)
#
#         sf.delete_bulk(s_object=Sobject, path=os.path.join(TEMP_CSV_DIR, file))
        # try:
        #     if os.system(f"sf data delete bulk --target-org {user} -s {Sobject} -f ./bin/temp/" + file) == 0:
        #         print(clr.OKGREEN + ">> Deleting ended successfully" + clr.ENDC)
        #     else:
        #         raise Exception("")
        # except Exception as e:
        #     print(e)
        #     clr.print_error(">> Error during deleting records")
        #     print(clr.WARNING + ">> Error during deleting records" + clr.ENDC)

#
# if __name__ == "__main__":
#     delete({})
