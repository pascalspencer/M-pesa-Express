from flask import Flask, request
import sqlalchemy
from sqlalchemy import MetaData
import os
import pymysql



app = Flask(__name__)


# Collecting payment information for database/csv
@app.route('/call_back', methods=['POST'])
def call_back():
    data = request.get_json()
    mpesa_data = data['Body']['stkCallback']['CallbackMetadata']['Item']
    payment_response = data['Body']['stkCallback']["ResultDesc"]

    amount = mpesa_data[0]['Value']
    mpesa_receipt_number = mpesa_data[1]['Value']
    transaction_date = mpesa_data[3]['Value']
    phone_number = mpesa_data[4]['Value']


    # Dealing with the database variables
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    metadata = MetaData()

    
    # Connecting to the database
    engine = sqlalchemy.create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", echo=False)

    payment_data = sqlalchemy.Table('payment_data', metadata, autoload_with=engine)

    insert_data = payment_data.insert().values(
        Amount = amount,
        MpesaReceiptNumber = mpesa_receipt_number,
        TransactionDate = transaction_date,
        PhoneNumber = phone_number
    )


    # Adding data to database
    conn = engine.connect()
    try:
        conn.execute(insert_data)

        conn.commit()
        print('Success')
        print(payment_response)
    except Exception as e:
        print(f'{payment_response}: {e}')

    finally:
        conn.close()
    
    return 'OK'
