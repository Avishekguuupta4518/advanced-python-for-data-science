#DEBUGGING

# import pdb 

# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i
        
#     return f    

# pdb.set_trace()

# fact(5)

import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="Day4.log"
    ,filemode="a")

logging.info("THIS IS A INFO")
logging.debug("THIS IS A DEBUG VALUE")
logging.error("THIS IS A ERROR ")
logging.warning("THIS IS A WARNING")
logging.critical("THIS IS A CRITICAL")

# level -- debug, info, warning,error,critical


#mini conda install hw