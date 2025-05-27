from appwrite.client import Client
from appwrite.services.storage import Storage
import os
import io
import csv
from datetime import datetime

def main(context):
    try:
        weight = context.req.body_json

        client = (Client()
            .set_endpoint(os.environ["APPWRITE_FUNCTION_API_ENDPOINT"])
            .set_project(os.environ["APPWRITE_FUNCTION_PROJECT_ID"])
            .set_key(context.req.headers["x-appwrite-key"]))
        storage = Storage(client)

        bucket_id = '682f27500032586773f2'
        file_id = '682f2804000a730d6bba'

         # === 2. Download CSV ===
        file_response = storage.get_file_download(bucket_id, file_id)
        csv_text = file_response.decode('utf-8')
        input_stream = io.StringIO(csv_text)
        reader = csv.reader(input_stream)
        rows = list(reader)

        # === 3. Add New Row ===
        current_date = datetime.now().strftime('%Y-%m-%d')
        num_columns = len(rows[0]) if rows else 2
        new_row = [current_date, str(weight)] + [''] * (num_columns - 2)
        rows.append(new_row)

        # === 4. Prepare Modified CSV ===
        output_stream = io.StringIO()
        writer = csv.writer(output_stream)
        writer.writerows(rows)
        modified_csv = output_stream.getvalue()

        # === 5. Delete Old File ===
        storage.delete_file(bucket_id, file_id)

        # === 6. Recreate File with Same ID and Name ===
        # You must provide the original filename again (or set as desired)
        storage.create_file(
            bucket_id,
            file_id,
            file=InputFile.from_string(modified_csv, filename='weight.csv')  # Use original filename if you want
        )

        context.log(context.req.body_json)
        return context.res.json({"message": "hello world"})
    except Exception as error:
        return context.res.json({"errorType": type(error).__name__,"error": error})