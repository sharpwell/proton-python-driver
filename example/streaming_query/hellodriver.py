from proton_driver import connect
with connect("proton://default:proton@localhost:8463/default") as conn:
  with conn.cursor() as cursor:
    cursor.execute("select 1")
    print(cursor.fetchone())
    
