from decouple import config

MIN_NUMBER = config('MIN_NUMBER', default=1, cast=int)
MAX_NUMBER = config('MAX_NUMBER', default=100, cast=int)
MAX_ATTEMPTS = config('MAX_ATTEMPTS', default=5, cast=int)
INITIAL_EQUITY = config('INITIAL_EQUITY', default=0, cast=int)
