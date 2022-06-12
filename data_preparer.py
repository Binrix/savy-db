class Data_Preparer:
    def str_to_arr(self, data: str | list[str]) -> list[str]:
        delimiter = ";"
        
        if type(data) == str:
            if "," in data:
                delimiter = ","

            data = data.split(delimiter)

        data = [entry.strip(" ") for entry in data]

        return data

        
        


