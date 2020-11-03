import logging

class NewFunctionFilter(logging.Filter):
    def filter(self, record):
        # print(dir(record))
        print(record.oleg_name)
         
        return record.funcName == 'new_fuction'



logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format', 
            'filters': ['new_filter']
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console']
            # 'propagate': False
        }
    },
    
    'filters': {
        'new_filter': {
            '()': NewFunctionFilter  # flters.py > import filters > filters.NewFunctionFilter
        }
    },
    # 'root': {} # '': {}
    # 'incremental': True,
}