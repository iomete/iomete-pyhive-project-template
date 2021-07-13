from pyhive import hive


def create_connection(account_number: str, warehouse_name: str, database: str, user_name: str, password: str):
    return hive.connect(host=f"{warehouse_name}-{account_number}-dwh.iomete.com", port=443, database=database,
                        username=user_name, password=password, auth='CUSTOM', transport_mode='https')


if __name__ == '__main__':

    # Change the following values to your values
    connection = create_connection(
        account_number="<account-number>",
        warehouse_name="<warehouse_name>",
        database="<db_name>",
        user_name="<user_name>",
        password="<password>")

    query = "select * from <your_table> limit 20"
    cursor = connection.cursor()
    cursor.execute(query)
    result_set = cursor.fetchall()

    print(result_set)
