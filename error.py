class DatabaseError(Exception):
    message = ""

class TableAlreadyExists(DatabaseError):
    def __init__(self, table) -> None:
        super().__init__(table)

        self.message = "Table {} already exists".format(table)

class ColumnHasNoType(DatabaseError):
    def __init__(self, column) -> None:
        super().__init__(column)

        self.message = "Column {} has no datatype".format(column)

class AmountValuesDoesNotMatch(DatabaseError):
    def __init__(self, amount_values, expected_amount_values) -> None:
        super().__init__(amount_values, expected_amount_values)

        self.message = "The amount of values ({}) does not match with the expected amount of values ({})".format(amount_values, expected_amount_values)

class ColumnNotFound(DatabaseError):
    def __init__(self, column) -> None:
        super().__init__(column)

        self.message = "The column {} was not found".format(column)