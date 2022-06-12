import this
import error
from data_preparer import Data_Preparer
from file_writer import File_Writer
from validator import Validator

class Database:
    file_writer: File_Writer
    validator: Validator
    data_preparer: Data_Preparer

    path = "./data"
    indexer_file = "./data/"
    metadata = {}
    metadata_file_name = "metadata.txt"

    def __init__(self) -> None:
        self.file_writer = File_Writer()
        self.validator = Validator()
        self.data_preparer = Data_Preparer()

    def overwrite_path(self, path) -> None:
        self.path = path

    def create_table(self, table: str, columns: str | list[str]) -> None:
        if self.file_writer.check_if_file_exists(self.path, "{}.txt".format(table)):
            raise error.TableAlreadyExists(table)

        columns_arr = self.data_preparer.str_to_arr(columns)

        if "Id" not in columns_arr or "id" not in columns_arr:
            columns_arr.insert(0, "Id")

        string_to_add = ";".join(columns_arr) + "\n"
        metadata_file_content = "{};{}".format(table, string_to_add)
        table_index_content = "0"

        self.file_writer.write_to_file(self.path, "{}.txt".format(table), string_to_add)
        self.file_writer.write_to_file(self.path, "{}_index.txt".format(table), table_index_content)
        self.file_writer.write_to_file(self.path, "metadata.txt", metadata_file_content)
    
    def insert_into(self, table: str, columns: str | list[str], values: str | list[str]) -> None:
        metadata = self.file_writer.read_file(self.path, "metadata.txt").splitlines()
        columns_arr = self.data_preparer.str_to_arr(columns)
        values_arr = self.data_preparer.str_to_arr(values)

        if len(columns_arr) != len(values_arr):
            raise error.AmountValuesDoesNotMatch(len(columns_arr), len(values_arr))

        if self.file_writer.check_if_file_exists(self.path, "{}_indexing.txt".format(table)):
            indexing_data = self.file_writer.read_file(self.path, "{}_indexing.txt".format(table)).splitlines()
            index = 0

            for column in columns_arr:
                if indexing_data[index] == column:
                    column_as_ascii = 0

                    for char in column:
                        column_as_ascii += ord(char)

                    indexing_data.append()

                    break
                index += 1



        for entry in metadata:
            entry_splitted = entry.split(";")

            if entry_splitted[0] == table:
                current_id = self.file_writer.read_file(self.path, "{}_index.txt".format(table))
                new_id = str(int(current_id) + 1)

                values_arr.insert(0, new_id)
                string_to_add = ";".join(values_arr) + "\n"

                self.file_writer.write_to_file(self.path, "{}.txt".format(table), string_to_add)
                self.file_writer.overwrite_file(self.path, "{}_index.txt".format(table), new_id)
                break
            

        pass

    def select_table(self, table: str, columns):
        pass

    def set_column_as_index(self, table: str, column: str) -> None:
        metadata = self.file_writer.read_file(self.path, self.metadata_file_name).splitlines()
        column_was_found = False

        for entry in metadata:
            entry_splitted = entry.split(";")

            if entry_splitted[0] == table:
                for col in entry_splitted:
                    if col == column:
                        column_was_found = True
                        break

        if column_was_found == False:
            raise error.ColumnNotFound(column)

        file_name = "{}_indexing.txt".format(table)

        indexing_table_content = "{};pos_in_table".format(column)

        self.file_writer.write_to_file(self.path, file_name, indexing_table_content)

        # hex_val = 0
        # for char in column:
        #     hex_val += ord(char)

                     
        



