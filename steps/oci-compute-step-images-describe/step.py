#!/usr/bin/env python
import oci
from relay_sdk import Interface, Dynamic as D

relay = Interface()

config = oci.config.from_file()

# config = {
#     "user": relay.get(D.oci.connection.userOCID),
#     "key_content": relay.get(D.oci.connection.keyContent),
#     "fingerprint": relay.get(D.oci.connection.fingerprint),
#     "tenancy": relay.get(D.oci.connection.tenancy),
#     "region": relay.get(D.oci.region)
# }

from oci.config import validate_config
validate_config(config)

# initialize the ComputeClient
compute = oci.core.ComputeClient(config)

# compartment_id = relay.get(D.oci.compartment_id)

compartment_id = "ocid1.compartment.oc1..aaaaaaaa5av46cvfltbu6jqhwctvvy7hdnpd4alhguhsmvj7j63rnn5fpceq"

if not compartment_id:
  compartment_id = config["tenancy"]

images = compute.list_images(compartment_id).data
if not images:
  print("No images found")
  exit(0)

for image in images:
  print('Found the following images: {}'.format(image.id))

print('Adding {} image(s) to the output `images`'.format(len(images)))
relay.outputs.set('images', images)