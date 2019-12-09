
class StringParser:
    
    DEFAULT_SEPARATOR = '|'

    @staticmethod
    def split(words, separator = None):
        if words != None:
            tokens = []
            
            for x in words.split(separator or StringParser.DEFAULT_SEPARATOR):
                tokens.append(x.strip())
                
            return tokens

        return None