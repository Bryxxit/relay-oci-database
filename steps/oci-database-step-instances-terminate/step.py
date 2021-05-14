#!/usr/bin/env python
import oci

config = oci.config.from_file()

from oci.config import validate_config
validate_config(config)

# initialize the DatabaseClient
database = oci.database.DatabaseClient(config)

db_system_ids = ["dfsdfgsfdsdf","fsdxfgsd"]

if not db_system_ids:
  print("No instance IDs found")
  exit(0)

print('Terminateing instances: {}'.format(db_system_ids))
for db_system_id in db_system_ids:
  database.terminate_db_system(db_system_ids)
