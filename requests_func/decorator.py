from functools import wraps
import logging
import traceback
import sys
import re
import itertools

def errorCheck(original_function):
    
    # logging Handler
    log = logging.getLogger('Error')
    log.setLevel(logging.DEBUG)
    log.propagate = True
    formatter = logging.Formatter("Error : %(asctime)s;\n%(message)s", "[%Y/%m/%d] %H:%M:%S")
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    log.addHandler(streamHandler)
    
    # Decorator
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        
        try :
            return original_function(*args, **kwargs)
        
        except Exception as e :
            exc_type, exc_obj, tb = sys.exc_info()
            formatted_lines = traceback.format_exc().splitlines()
            num = ([idx for idx , i 
                    in enumerate(formatted_lines) 
                    if re.search(" line ", i) is not None ][-1])
            s  = [line.split(",") for line in formatted_lines[num:]]
            
            merged = list(itertools.chain(*s))
            finalerror = "\n".join([string.strip() for string in merged])
            func_name = original_function.__name__
            
            errors =  traceback.extract_stack()
            errors = ("".join(
                [f"Where : {str(i).split('FrameSummary file ')[1].split(',')[0]} \n Line : {str(i).split('FrameSummary file ')[1].split(',')[1]}\n {'--'*30} \n" 
                 for i in errors[:-1]]))
            print(f"{'='*15} Code Detail Inf {'='*15} \n {errors}")
            log.error(f"{'=='*20}\n{finalerror}\n{'=='*20}")
            sys.exit(1)
            
    return wrapper