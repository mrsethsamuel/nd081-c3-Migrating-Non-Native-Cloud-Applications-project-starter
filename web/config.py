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
    SECRET_KEY = 'RHwuWf610XSIsOGMgqUIN/SAWXjkX7sVdp7LkWE/gYw='
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://techservicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=RHwuWf610XSIsOGMgqUIN/SAWXjkX7sVdp7LkWE/gYw=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    #SENDGRID_API_KEY = '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' 
    #SENDGRID_API_KEY = "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"
    
    SENDGRID_API_KEY = "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"
    #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
