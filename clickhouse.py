# Install deps
pip install clickhouse-connect python-dotenv

# Run with default profile
python clickhouse_app.py

# Run with prod profile
python clickhouse_app.py --profile prod

# Ad-hoc query
python clickhouse_app.py --sql "SELECT version() AS ver"

# With parameters (named placeholders in SQL)
python clickhouse_app.py --sql "SELECT number FROM system.numbers LIMIT {limit}" --param limit=5

# Override any key via env (highest priority)
export CLICKHOUSE__prod__password='supersecret'
python clickhouse_app.py --profile prod