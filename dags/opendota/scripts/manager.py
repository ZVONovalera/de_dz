from opendota.scripts.api import fetch_data_from_opendota_api
from airflow.providers.postgres.hooks.postgres import PostgresHook

def fetch_data_from_opendota(entities, **context):
    hook = PostgresHook(postgres_conn_id="pg_conn")
    conn = hook.get_conn()
    cursor = conn.cursor()

    for entity in entities:
        data = fetch_data_from_opendota_api(entity['endpoint'], **context)
        cursor.execute(f"TRUNCATE TABLE public.{entity['name']};")
        fields_count = len(entity["fields"])
        placeholders = ', '.join(['%s'] * fields_count) #сделал адаптивные плейсхолдеры чтоб без бурмалды загружать сразу две сущеости

        for record in data:
            values = [record.get(field) for field in entity['fields']]
            insert_query = f"""
            INSERT INTO public.{entity['name']} ({', '.join(entity['fields'])})
            VALUES ({placeholders})
            """
            cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()
    conn.close()
