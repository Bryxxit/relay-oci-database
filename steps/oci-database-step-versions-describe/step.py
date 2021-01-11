#!/usr/bin/env python
import oci

config = oci.config.from_file()

from oci.config import validate_config
validate_config(config)

# initialize the DatabaseClient
database = oci.database.DatabaseClient(config)

compartment_id = "ocid1.compartment.oc1..aaaaaaaa5av46cvfltbu6jqhwctvvy7hdnpd4alhguhsmvj7j63rnn5fpceq"

if not compartment_id:
  compartment_id = config["tenancy"]

versions = database.list_db_versions(compartment_id).data
if not versions:
  print("No versions found")
  exit(0)
print(versions)
for version in versions:
  print('Found the following versions: {}'.format(version.version))

print('Adding {} version(s) to the output `versions`'.format(len(versions)))