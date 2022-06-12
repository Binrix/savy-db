class Validator:
    def has_input_datatype(self, column: str) -> bool:
        column_with_type = column.split(":")

        if len(column_with_type) == 2:
            return True

        return False 