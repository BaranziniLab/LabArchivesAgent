# LabArchivesAgent

Retired. This extension no longer calls LabArchives and only reports that it is retired. Remove it.

Current version: **0.2.0**

> **Retired.** LabArchivesAgent was retired on 2026-11-22 and no longer calls any service. Why: LabArchives signs every API call with an access key id, an expiry and an HMAC signature on a regional host. This extension sent a plain key instead, so it never worked, and no LabArchives account was available to test a rebuild. Use instead: Open your notebooks in LabArchives in the browser. If your lab needs LabArchives in Biorouter, ask for it in BAAM.

This is the final release of a retired Biorouter extension. It replaces every
earlier tool with one, `labarchives_status`, which shows the notice above. It holds no
credentials, reads no setting and calls no service. Remove the extension in
Biorouter once you no longer need the notice.

## Tools

- `labarchives_status`: shows why LabArchivesAgent was retired and what to use instead. It calls no service.

## Bundled skills

Every skill an earlier release bundled is kept, and each now says where its content
moved. An update never deletes a file an earlier version installed, so keeping the
paths is what replaces the old instructions.

## Develop and release

```bash
uv sync
uv run python -m unittest discover -s tests -v
uv run python scripts/build_brxt.py
```

Do not edit `src/labarchivesagent/_kit/` or `tests/kit_testing/`: they are vendored from the BRXT
adapter kit in the Biorouter repository (`scripts/brxt-adapter-kit/`).

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
