# oci-database-step-versions-describe

This [OCI database](https://www.oracle.com/database/) step container lists the database versions
in an OCI region that are owned by my account and sets an output, `versions`, to an
array containing information about them.

## Example output `versions`

```json
[
   {
   "is_latest_for_major_version": true,
   "is_preview_db_version": null,
   "is_upgrade_supported": null,
   "supports_pdb": false,
   "version": "11.2.0.4"
   }
]
```
