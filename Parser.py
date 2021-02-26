import sys  
import os
#import dentro de la carpeta parsers
sys.path.append(os.path.abspath(os.path.join("parsers")))

from AFD import AFD

class Parser:
    """
    Factory model for the parser, calls get_parser which decides which method to be called
    """
    def parse(self, tokenArr, format):
        parser = get_parser(format)
        return parser(tokenArr)
"""
receives format or method for interpreting(?) the RegEx
"""
def get_parser(format):
    if format == "AFD":
        afd = AFD()
        return afd.afd_parser
    elif format == "Thompson":
        return thompson_parser
    elif format == "subset":
        return subset
    else:
        raise ValueError(format)    


