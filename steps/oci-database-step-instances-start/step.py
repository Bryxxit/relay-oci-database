#!/usr/bin/env python
import oci

config = oci.config.from_file()

from oci.config import validate_config
validate_config(config)

# initialize the DatabaseClient
database = oci.database.DatabaseClient(config)

instanceIDs = "dfsdfgsfdsdf","fsdxfgsd"

if not instanceIDs:
  print("No instance IDs found")
  exit(0)

print('Starting instances: {}'.format(instanceIDs))
for instanceID in instanceIDs:
  database.db_node_action(instanceID,"START")
