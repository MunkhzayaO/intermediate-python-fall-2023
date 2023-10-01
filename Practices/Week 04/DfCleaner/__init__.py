
class Cleaner:
    def __init__(self, df):
        self.df = df
    
    def drop_empty(self):
        self.df = self.df.dropna
    
    def fill_empty(self):
        self.df = self.df.fillna
        
    def drop_column(self):
        self.df = self.df
        
    def fix_index(self):
        self.df = self.df.reset_index
        
    def fix_dates(self):
        self.df = self.df.datetime