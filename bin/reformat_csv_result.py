import pandas as pd
import sys
import os


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
        sys.stderr.write(f'There is no file \'/temp/{file_name}\' with Omniprocess records\n')
        sys.exit()

    return omniprocess


def reformat(args):
    N_VERSIONS_TO_LEAVE = int(args['count'])

    omniprocess = get_file("omniprocess_records.csv")

    for col in ['Name', 'Type', 'VersionNumber', 'IsActive']:
        if col not in omniprocess:
            sys.stderr.write(
                f'There is no column \'{col}\' in file \'/temp/omniprocess_records.csv\' with Omniprocess records\n')
            sys.exit()

    omniprocess['Name'] = omniprocess['Type'] + omniprocess['Name']

    omniprocess_name = pd.DataFrame.copy(omniprocess)
    omniprocess_name = omniprocess_name['Name'].unique()  # creates array with names

    result_df = pd.DataFrame(columns=['Id'])  # create dataframe with Id's to delete from Org

    for name in omniprocess_name:
        df_temp = leave_n_versions(omniprocess[omniprocess['Name'] == name],
                                   N_VERSIONS_TO_LEAVE)  # give dataframe with one element only and all its versions
        if not isinstance(df_temp, type(None)):
            result_df = pd.concat([result_df, df_temp], ignore_index=True)

    result_df.to_csv(os.path.join("./", "bin", "temp", "omniprocess_records_ids.csv"), index=False)


if __name__ == "__main__":
    reformat({'count': "1"})
