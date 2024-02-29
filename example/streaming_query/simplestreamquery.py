from proton_driver import client

c = client.Client(host='127.0.0.1', port=8463, password='proton')

# create a random stream if not exist
c.execute("CREATE RANDOM STREAM IF NOT EXISTS"
          " devices("
          " device string default 'device'||to_string(rand()%4), "
          " temperature float default rand()%1000/10"
          ")")
# query the stream and return in a iterator
rows = c.execute_iter(
    "SELECT device, count(*), min(temperature), max(temperature) "
    "FROM devices GROUP BY device",
)
for row in rows:
    print(row)
