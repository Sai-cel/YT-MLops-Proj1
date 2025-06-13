from src.exception import MyException
from src.logger import logging 
import sys

try:
    a=1+"z"
    
except Exception as e:
    logging.info(e)
    raise MyException(e,sys)