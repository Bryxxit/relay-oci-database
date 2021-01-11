#!/usr/bin/env python
import oci

config = oci.config.from_file()

from oci.config import validate_config
validate_config(config)

# initialize the ComputeClient
compute = oci.core.ComputeClient(config)

instanceIDs = ["dfsdfgsfdsdf","fsdxfgsd"]

if not instanceIDs:
  print("No instance IDs found")
  exit(0)

print('Terminateing instances: {}'.format(instanceIDs))
for instanceID in instanceIDs:
  compute.terminate_instance(instanceID)
