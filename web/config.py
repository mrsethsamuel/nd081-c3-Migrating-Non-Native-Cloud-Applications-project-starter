import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="techconfdbserver.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="techadmin@techconfdbserver" #TODO: Update value
    POSTGRES_PW="SamB0os123456"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'mn3n+8ykeL9KPMXCq8EKQVRyj9pilBVG7YwoJAlKd3c='
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://notificationqueue.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=mn3n+8ykeL9KPMXCq8EKQVRyj9pilBVG7YwoJAlKd3c=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
