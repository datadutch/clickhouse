# create your virtual environment

python3 -m venv .venv

# activate the venv

source .venv/bin/activate

# install required packages

pip install -r requirements.txt

# set up your ClickHouse

Follow this guide: https://www.scaleway.com/en/data-warehouse-for-clickhouser/

# configuration

rename connectionstoml to connections.toml and update with your ClickHouse credentials

Run clickhouse.py to test the connection.