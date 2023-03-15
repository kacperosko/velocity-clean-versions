import sys
import os
import pandas as pd
import pandas.core.frame as pd_frame
import pandas.errors as pd_errors
from typing import overload

import pandas.errors

from _settings import TEMP_CSV_DIR, clr
from simple_salesforce import Salesforce


class SalesforceCommands:

    def __init__(self, username: str, password: str, security_token: str, domain: str = None):
        """
        Parse login credential to Org You want to clean from vlocity versions. Domain is optional but
        You have to parse 'test' if You want to authorize sandbox Org

        :param username:
        :param password:
        :param security_token:
        :param domain:
        """
        try:
            clr.print_info(f">> Authorizing an Org {username}")
            self.sf = Salesforce(
                username=username,
                password=password,
                security_token=security_token,
                domain=domain if domain else None,
            )
            clr.print_success(">> Org authorized successful")
        except Exception as e:
            clr.print_error(">> Error during authorizing an Org")
            clr.print_error(f">> {e}")
            sys.exit()

    def get_bulk(self, query: str, s_object: str) -> pd_frame.DataFrame:
        clr.print_info(f">> Running bulk query for {s_object} object")
        try:
            fetch_results = self.sf.bulk.__getattr__(s_object).query(query, lazy_operation=True)
        except Exception as e:
            clr.print_error(f">> {e}")
            return None

        data = []
        df = pd.DataFrame()
        for list_results in fetch_results:
            data.extend(list_results)
        if len(data) > 0:
            df = pd.DataFrame.from_records(data).drop('attributes', axis=1)
        else:
            clr.print_info(">> There is no records matching query")

        df.to_csv(os.path.join(TEMP_CSV_DIR, f"{s_object}_get_bulk.csv"), index=False)

        clr.print_success(f">> Query ended successful with {len(df.index)} rows")
        return df

    def delete_bulk(self, s_object: str, dataframe: pd_frame.DataFrame = None, path: str = "generate_from_temp",
                    batch_size: int = 10000, use_serial: bool = True) -> bool:

        if dataframe is None:
            if path == "generate_from_temp":
                path = os.path.join(TEMP_CSV_DIR, f"{s_object}_get_bulk.csv")
            elif not os.path.isfile(path):
                clr.print_error(f">> There is no file in the given path {path}")
                return False
            clr.print_info(">> Running bulk delete from CSV file")
            try:
                dataframe = pd.read_csv(filepath_or_buffer=path)
            except pd_errors.EmptyDataError:
                clr.print_error(">> Temp CSV file is empty")
                return False
            except Exception as e:
                clr.print_error(f">> {e}")
                return False
        else:
            clr.print_info(">> Running bulk delete from Pandas DataFrame")

        data = dataframe[['Id']].to_dict('records')
        data.append({'Id': '0013H00000XYAX8123'})
        print(data)

        # def delete_bulk(self, s_object, data, batch_size, use_serial):
        try:
            result = self.sf.bulk.__getattr__(s_object).delete(data, batch_size=batch_size, use_serial=use_serial)
        except Exception as e:
            clr.print_error(f">> {e}")
            return
        success, failure = 0, 0
        for res in result:
            if res['success']:
                success += 1
            else:
                failure += 1
        clr.print_info(f">> Succesfully deleted {success} records" + " {failure} failed" if failure > 0 else "")
        clr.print_success(">> Deleting ended succesful")
        return True


if __name__ == '__main__':
    sf = SalesforceCommands(
        username='katarzyna.rutkowska@enxooddfaprod.com.devkaosk',
        password='nLSWaBiDuZIVcL24qsvm',
        security_token='O5FwHw3jPwFHEdePKfiZ5GMN',
        domain="test"
    )
    df = sf.get_bulk(query="SELECT Id, Name FROM Account WHERE Id ='0013H00000XYAX8QAP'", s_object="Account")
    sf.delete_bulk(s_object="Account")
    # sf.get_bulk(query="SELECT Id, Name FROM OmniProcess", s_object="OmniProcess")
