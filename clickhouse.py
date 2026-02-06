import clickhouse_connect
import toml

# Load connection info from connections.toml
config = toml.load("connections.toml")
scw = config["scw"]

client = clickhouse_connect.get_client(
    host=scw["host"],
    port=scw["port"],
    username=scw["username"],
    password=scw["password"],
    secure=scw.get("secure", True)
)
query_result = client.query("SHOW DATABASES")
print(query_result.result_set)