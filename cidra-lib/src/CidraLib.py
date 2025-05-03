
class CidraDataset:
    """
    A class representing a dataset in the Cidra library.
    Attributes:
        name (str): The name of the dataset.
        path (str): The path to the dataset.
        description (str): A description of the dataset.
        data (any): Pandas dataset.
    """
    def __init__(self,  data, name="", description=""):
        self.name = name
        self.description = description
        self.data = data

    def __repr__(self):
        return f"CidraDataset(name={self.name}, path={self.path}, description={self.description}, data={self.data})"
    


class CidraKeyValue:
    """
    A class representing a key-value pair in the Cidra library.
    Attributes:
        key (str): The key of the key-value pair.
        value (any): The value of the key-value pair.
    """
    def __init__(self, key, value, name="", description=""):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"CidraKeyValue(key={self.key}, value={self.value})"