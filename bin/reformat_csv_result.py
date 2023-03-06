import pandas as pd
import sys
import os
from bin.bcolors import bcolors as clr

OMNIPROCESS_RECORDS_LEN = None


def leave_n_versions(df, n_rows):
    df = df.sort_values(by=['VersionNumber'], ascending=False)  # sort dataframe to get highest version on top
    df = df.drop(df[df.IsActive == True].index)  # remove activated version, we don't count this one

    if len(df.index) <= n_rows:
        return None
    else:
        df.drop(df.index[0: n_rows], axis=0, inplace=True)

        return df[['Id']]


def get_file(file_name):
    try:
        omniprocess = pd.read_csv("./bin/temp/" + file_name)
    except FileNotFoundError:
        print(clr.FAIL + f'There is no file \'/temp/{file_name}\' with Omniprocess records\n' + clr.ENDC)
        sys.exit()

    return omniprocess


def reformat(count=None):
    print(clr.OKBLUE + ">> Analysing versions to delete" + clr.ENDC)
    try:
        N_VERSIONS_TO_LEAVE = int(count)
    except ValueError:
        print(clr.FAIL +
              f' \'count\' value must be a number greater than or equal to 0' + clr.ENDC)
        sys.exit()

    if N_VERSIONS_TO_LEAVE < 0:
        print(clr.FAIL +
              f'\'count\' value must be greater than or equal to 0' + clr.ENDC)
        sys.exit()

    omniprocess_df = get_file("omniprocess_records.csv")

    for col in ['Name', 'Type', 'VersionNumber', 'IsActive']:
        if col not in omniprocess_df:
            sys.stderr.write(
                f'There is no column \'{col}\' in file \'/temp/omniprocess_records.csv\' with Omniprocess records\n')
            sys.exit()

    if len(omniprocess_df.index) == 0:
        print(clr.FAIL +
              f'There\'s no OmniProcess records' + clr.ENDC)
        sys.exit()

    omniprocess_df['Name'] = omniprocess_df['Type'] + omniprocess_df['Name']

    omniprocess_name_df = pd.DataFrame.copy(omniprocess_df)
    omniprocess_name_df = omniprocess_name_df['Name'].unique()  # creates array with names

    result_df = pd.DataFrame(columns=['Id'])  # create dataframe with Id's to delete from Org

    for name in omniprocess_name_df:
        temp_df = leave_n_versions(omniprocess_df[omniprocess_df['Name'] == name],
                                   N_VERSIONS_TO_LEAVE)  # give dataframe with one element only and all its versions
        if not isinstance(temp_df, type(None)):
            result_df = pd.concat([result_df, temp_df], ignore_index=True)

    result_df.to_csv(os.path.join("./", "bin", "temp", "omniprocess_records_ids.csv"), index=False)

    global OMNIPROCESS_RECORDS_LEN
    OMNIPROCESS_RECORDS_LEN = len(result_df.index)
    print(clr.OKGREEN + f">> Analyse ended successfully ({OMNIPROCESS_RECORDS_LEN} verions to delete)" + clr.ENDC)


if __name__ == "__main__":
    reformat({'count': "1"})
