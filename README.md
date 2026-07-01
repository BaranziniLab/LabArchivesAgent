# LabArchivesAgent

MCP access to LabArchives electronic lab notebook metadata and entries, with read-first notebook inspection and confirmation-gated API requests.

This repository follows the BioRouter `.brxt` extension convention used by `SPOKEAgent` and `UCSFOMOPAgent`: a root `manifest.json`, Python package under `src/`, and optional bundled skills under `skills/`.

## Tools

- `get_labarchivesagent_status`: report configured environment variables without revealing secrets.
- `get_labarchivesagent_request_plan`: explain whether an API request is read-only or requires explicit mutation approval.
- `call_labarchivesagent_api`: call a platform API endpoint with write methods blocked unless `allow_mutation=true`.
- `summarize_labarchivesagent_resource`: summarize a JSON export or API payload without making a network call.

## Configuration

| Variable | Required | Secret | Purpose |
|---|---:|---:|---|
| `LABARCHIVES_API_KEY` | true | true | LabArchives API key or token |
| `LABARCHIVES_BASE_URL` | false | false | LabArchives API base URL |
| `LABARCHIVES_LOG_LEVEL` | false | false | Logging level |


## Build

```bash
uv sync
scripts/build_brxt.sh
```

The bundle is written to `dist/labarchivesagent.brxt`.

## Install in BioRouter

```bash
biorouter extension install dist/labarchivesagent.brxt
```

Add the required secrets with `--secret KEY=value` or configure them in the BioRouter UI.

## License

Apache-2.0. See `LICENSE`.
