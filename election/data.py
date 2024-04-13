from django.db import connection
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
settings.configure()



def execute_sql_script(file_path):
    # Read the SQL commands from the file
    with open(file_path, 'r') as f:
        sql_commands = f.read()

    # Execute the SQL commands
    with connection.cursor() as cursor:
        cursor.execute(sql_commands)
    connection.commit()

if __name__ == "__main__":
    # Specify the path to your SQL file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sql_file_path = os.path.join(current_dir, 'sql_commands', 'database_commands.sql')
    execute_sql_script(sql_file_path)