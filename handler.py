import pymysql
from datetime import datetime
from pytz import timezone

endpoint = 'endpint'
username = 'user'
password = 'pass'
database_name = 'name'

connection = pymysql.connect(host=endpoint, user=username,
                             password=password, db=database_name)


def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name'] 
    key = event['Records'][0]['s3']['object']['key'] 
    
    chile = timezone('America/Santiago')
    chileDate = datetime.now(chile)
    final = chileDate.strftime('%d/%m/%Y %H:%M')
    print(final)
    
    actualDate = datetime.now()
    date = datetime.strftime(actualDate, '%d/%m/%Y %H:%M')
    print(date)
    
    sniffer = key.split('/')[0]

    cursor = connection.cursor()
    cursor.execute('INSERT INTO h_RebornTelemetry_t_datacheckups (check_file_name, creation_date, sniffer) VALUE (%s, %s, %s)',(key, date, sniffer))
 
    
    connection.commit()
# Function
    


    


