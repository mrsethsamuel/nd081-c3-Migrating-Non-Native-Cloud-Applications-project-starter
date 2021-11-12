import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="techconfdbserver.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="techconfadmin@techconfdbserver" #TODO: Update value
    POSTGRES_PW="SamB0os123456"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'X/VCRJMCYLR1klPeX8UtVGUDY+MGQKcEpZGKgV7X6O8='
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://techservicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=jX+rHF3ZsXivADHIE0pMW7m/osD9O7EunqgR0XS8vLw=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
