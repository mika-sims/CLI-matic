class Weather:
    """
    Class to represent weather object
    
    Attributes
    ----------
    data : JSON object converted to dictionary to iterate over
    
    get_value(): Retrieves the values by iterating through
                 the list of dictionaries
    """
    def __init__(self, json_data):
        """
        Initialize the weather object

        Args:
            json_data (list): Json object (list of dictionaries)
        """        
        data = dict(json_data)   

        for key, val in data.items():
            setattr(self, key, self.get_attr_value(val))

    def get_attr_value(self, value):
        """
        Gets values from data attribute
        
        Note: Since the JSON object is a list of dictionaries, 
        iterate over the JSON object and get the value of list or dictionary.

        Args:
            value (str): Value to be retrieved

        Returns:
            str: Returns the list item or dictionary values as value
        """        
        if isinstance(value, list):
            return [self.get_attr_value(x) for x in value]
        elif isinstance(value, dict):
            return Weather(value)
        else:
            return value
    
