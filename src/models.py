import csv


class YACC(object):
    '''
        Schema will be a dictionary that defines the header of a csv file.
        This will take the format of {headerName: datatype}, where datatype provides
        a reference to a function available in the generator class.
    '''
    def __init__(self, schema=None, generator=None, filename=None, delimiter=None,\
                        quote=None,stream=True):
        
        schema = {} if schema is None else schema
        filename = "output" if filename is None else filename
        quote = '"' if quote is None else quote
        delimiter = "|" if delimiter is None else delimiter

        self.schema = schema
        self.stream = stream
        self.generator = generator
        self.f = open(filename+'.csv', 'w', newline='\n')
        
        self.writer = csv.DictWriter(self.f,  fieldnames=schema.keys(), delimiter=delimiter, quotechar=quote) 

    def generate(self, lines):
        if self.stream:
            self.writer.writeheader()
            for i in range(0,lines):
                d = {}
                for (name, data) in self.schema.items():
                    d[name] = data()    
                self.writer.writerow(d)
                
    def close(self):
        self.f.close()
