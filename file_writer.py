from os.path import exists

class File_Writer:
    def write_to_file(self, path: str, filename: str, content) -> None:
        full_path = "{}/{}".format(path, filename)

        file = open(full_path, "a")
        file.write(content)
        file.close()

    def check_if_file_exists(self, path: str, filename: str) -> bool:
        full_path = "{}/{}".format(path, filename)

        if exists(full_path):
            return True

        return False

    def overwrite_file(self, path: str, filename: str, content):
        full_path = "{}/{}".format(path, filename)

        file = open(full_path, "w")
        file.write(content)
        file.close()

    def read_file(self, path: str, filename: str) -> str:
        full_path = "{}/{}".format(path, filename)

        file = open(full_path)
        data = file.read()

        file.close()
        return data
         
