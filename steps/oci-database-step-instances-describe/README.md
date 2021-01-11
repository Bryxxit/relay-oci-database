# oci-compute-step-instances-describe

This [OCI Compute](https://www.oracle.com/cloud/compute/) step container lists the instances
in an AWS region and sets an output, `instances`, to an array containing
information about them.

Optionally add filters to narrow the list of returned instances based on filter
criteria.

## Example output `instances`

```json
[
   {
   "agent_config": {
      "is_management_disabled": false,
      "is_monitoring_disabled": false
   },
   "availability_config": {
      "recovery_action": "RESTORE_INSTANCE"
   },
   "availability_domain": "QEoU:EU-FRANKFURT-1-AD-1",
   "compartment_id": "ocid1.compartment.oc1..aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
   "dedicated_vm_host_id": null,
   "defined_tags": {
      "Oracle-Tags": {
         "CreatedBy": "oracleidentitycloudservice/user@example.com",
         "CreatedOn": "2020-11-30T10:25:29.929Z"
      },
      "customer-billing": {
         "customer-charge": "no"
      }
   },
   "display_name": "exampleVM",
   "extended_metadata": {},
   "fault_domain": "FAULT-DOMAIN-3",
   "freeform_tags": {},
   "id": "ocid1.instance.oc1.eu-frankfurt-1.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
   "image_id": "ocid1.image.oc1.eu-frankfurt-1.aaaaaaaaf6gm7xvn7rhll36kwlotl4chm25ykgsje7zt2b4w6gae4yqfdfwa",
   "instance_options": {
      "are_legacy_imds_endpoints_disabled": false
   },
   "ipxe_script": null,
   "launch_mode": "NATIVE",
   "launch_options": {
      "boot_volume_type": "PARAVIRTUALIZED",
      "firmware": "UEFI_64",
      "is_consistent_volume_naming_enabled": true,
      "is_pv_encryption_in_transit_enabled": false,
      "network_type": "PARAVIRTUALIZED",
      "remote_data_volume_type": "PARAVIRTUALIZED"
   },
   "lifecycle_state": "RUNNING",
   "metadata": {
      "ssh_authorized_keys": "ssh-rsa AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA example"
   },
   "region": "eu-frankfurt-1",
   "shape": "VM.Standard2.1",
   "shape_config": {
      "gpu_description": null,
      "gpus": 0,
      "local_disk_description": null,
      "local_disks": 0,
      "local_disks_total_size_in_gbs": null,
      "max_vnic_attachments": 2,
      "memory_in_gbs": 15.0,
      "networking_bandwidth_in_gbps": 1.0,
      "ocpus": 1.0,
      "processor_description": "2.0 GHz Intel\u00ae Xeon\u00ae Platinum 8167M (Skylake)"
   },
   "source_details": {
      "boot_volume_size_in_gbs": null,
      "image_id": "ocid1.image.oc1.eu-frankfurt-1.aaaaaaaaf6gm7xvn7rhll36kwlotl4chm25ykgsje7zt2b4w6gae4yqfdfwa",
      "kms_key_id": null,
      "source_type": "image"
   },
   "system_tags": {},
   "time_created": "2020-11-30T10:25:30.732000+00:00",
   "time_maintenance_reboot_due": null
   }
]
```
