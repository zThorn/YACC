class YACC():
    '''
        Schema will be a dictionary that defines the header of a csv file.
        This will take the format of [headerName: datatype] .  Generator expects an instance of a class that is
        capable of generating data.
    '''
    def __init__(self, schema=None, generator=None):
        


    '''
        I'm intending on using faker for this, but this will act as an abstraction away from
        using faker.  Ultimately, I'm going to write methods to just generate data by passing
        in Regex strings for each different data type, but for now I'll settle for generic
        setters to define which methods should be used.
    ''' 

class Generator():
    

