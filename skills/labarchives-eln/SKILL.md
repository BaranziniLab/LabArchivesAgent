---
name: labarchives-eln
description: Use LabArchivesAgent when working with LabArchives platform data, API resources, provenance, or reproducibility checks from inside BioRouter.
license: Apache-2.0
user-invocable: false
---

# LabArchivesAgent Skill

Use this extension to inspect LabArchives notebooks and entries, preserving notebook provenance and avoiding write actions unless explicitly confirmed.

## Operating rules

- Start with `get_labarchivesagent_status` to confirm whether credentials and base URLs are configured.
- Use `get_labarchivesagent_request_plan` before any endpoint that may create, update, launch, upload, or delete a resource.
- Prefer read-only `GET` requests through `call_labarchivesagent_api` while exploring.
- Do not pass `allow_mutation=true` unless the user has explicitly approved the exact operation, target resource, and expected side effect.
- Preserve platform IDs, versions, owners/authors, timestamps, and URLs in any report.
- Never print API tokens, passwords, bearer headers, or session cookies.

## Useful starting endpoints

- `/notebooks`
- `/entries`
- `/folders`
