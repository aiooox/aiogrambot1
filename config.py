import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = str(os.getenv('TOKEN'))
admins = [
    5506281762
]

GROUPID = -1001761995571
GROUPLINK = 't.me/testcallback'

CHATLINK = 't.me/areaa24'

ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASS = str(os.getenv('PGPASS'))
DB = str(os.getenv('DB'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASS}@{ip}/{DB}'
