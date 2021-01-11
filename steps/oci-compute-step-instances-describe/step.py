#!/usr/bin/env python
import oci

config = oci.config.from_file()

from oci.config import validate_config
validate_config(config)

# initialize the ComputeClient
compute = oci.core.ComputeClient(config)

compartment_id = "ocid1.compartment.oc1..aaaaaaaa5av46cvfltbu6jqhwctvvy7hdnpd4alhguhsmvj7j63rnn5fpceq"

if not compartment_id:
  compartment_id = config["tenancy"]

instances = compute.list_instances(compartment_id).data
if not instances:
  print("No instances found")
  exit(0)

for instance in instances:
  print("{:<30} {:<30} {:<30}".format(instance.id, instance.lifecycle_state, instance.shape))

print('\nAdding {0} instance(s) to the output `instances`'.format(len(instances)))