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

graceful = False

if graceful:
  print('Gracefully rebooting instances: {}'.format(instanceIDs))
  action = "SOFTRESET"
else:
  print('Rebooting instances: {}'.format(instanceIDs))
  action = "RESET"

for instanceID in instanceIDs:
  database.db_node_action(instanceID,action)
