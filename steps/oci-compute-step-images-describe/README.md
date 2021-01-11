# oci-compute-step-images-describe

This [OCI Compute](https://www.oracle.com/cloud/compute/) step container lists the images
in an OCI region that are owned by my account and sets an output, `images`, to an
array containing information about them.

## Example output `images`

```json
[
   {
   "agent_features": null,
   "base_image_id": null,
   "compartment_id": null,
   "create_image_allowed": true,
   "defined_tags": {},
   "display_name": "Oracle-Linux-7.9-2020.10.26-0",
   "freeform_tags": {},
   "id": "ocid1.image.oc1.eu-frankfurt-1.aaaaaaaaoryxmxvdjbbkuexacfomno4vb5zdoxuecx4wb3mbj5diisuui5ia",
   "launch_mode": "NATIVE",
   "launch_options": {
      "boot_volume_type": "PARAVIRTUALIZED",
      "firmware": "UEFI_64",
      "is_consistent_volume_naming_enabled": true,
      "is_pv_encryption_in_transit_enabled": true,
      "network_type": "PARAVIRTUALIZED",
      "remote_data_volume_type": "PARAVIRTUALIZED"
   },
   "lifecycle_state": "AVAILABLE",
   "operating_system": "Oracle Linux",
   "operating_system_version": "7.9",
   "size_in_mbs": 47694,
   "time_created": "2020-10-27T06:33:38.068000+00:00"
   }
]
```
