---
name: labarchives-eln
description: "Retired with LabArchivesAgent. This skill no longer holds instructions."
---

# labarchives-eln has moved

This skill was bundled with LabArchivesAgent, which is retired. LabArchivesAgent never reached LabArchives: the LabArchives API needs signed requests that the extension did not send. Open your notebooks in LabArchives in the browser instead, and remove LabArchivesAgent from Biorouter.

LabArchivesAgent was retired on 2026-11-22 and no longer calls any service. Why: LabArchives signs every API call with an access key id, an expiry and an HMAC signature on a regional host. This extension sent a plain key instead, so it never worked, and no LabArchives account was available to test a rebuild. Use instead: Open your notebooks in LabArchives in the browser. If your lab needs LabArchives in Biorouter, ask for it in BAAM.
