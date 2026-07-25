# MCP App

CIEL Lab exposes an MCP server and an interactive web widget so an AI client can
help find concepts and prepare review work without receiving authority to
silently change OCL.

## Trust boundary

The central rule is:

> The language model prepares a preview; a human reviews and commits through
> the CIEL Lab interface.

MCP tools do not persist OCL mutations. They can search, resolve, and propose
worklists or bulk changes. The widget displays the proposal and requires the
authenticated user to approve the final application action.

## Authentication layers

| Credential | Purpose | Lifetime |
| --- | --- | --- |
| CIEL Lab personal access token | Authenticates the AI/MCP client | Until revoked |
| Widget session JWT | Authenticates the embedded browser session | Short-lived; approximately 30 minutes in the observed configuration |
| Personal OCL API token | Authorizes the final OCL write | Stored encrypted by CIEL Lab |

Generate the CIEL Lab personal access token in Settings. It is displayed once.
Use a secret field in the client configuration.

## Typical workflow

1. The AI client calls the CIEL Lab MCP endpoint.
2. It searches CIEL HEAD, a released version, or available worklists.
3. It proposes a worklist or bulk-edit preview.
4. CIEL Lab resolves names to stable identifiers.
5. The web widget renders the proposal and server-owned view state.
6. The user checks each concept, mapping, and operation.
7. The user commits with the browser session and personal OCL authorization.

Server-sent events keep the widget synchronized with server-side view state.

## Available capabilities

The codebase includes capabilities for:

- connectivity checks;
- listing CIEL versions;
- searching concepts;
- listing and retrieving worklists;
- proposing a worklist preview;
- listing and retrieving custom worklists;
- preparing mapping candidates and bulk-edit previews.

The exact tool catalog can evolve. Let the MCP client discover tools from the
server instead of hard-coding a stale list.

## Sources and freshness

MCP retrieval can target:

- the latest released CIEL version;
- HEAD from the Valkey mirror, with live OCL fallback;
- a fixed released version;
- stored worklists and custom worklists.

If HEAD results are missing after a cache reset, restore the regular HEAD
refresh and indexing chain before recreating work.

Implementation and cache behavior are also tracked in
[OpenConceptLab/ocl_issues#2535](https://github.com/OpenConceptLab/ocl_issues/issues/2535).

## Safety checklist

- verify every source, code, display, and map type;
- treat vector results as candidates;
- never paste credentials into a prompt;
- keep MCP tokens user-specific and revocable;
- use a worklist to preserve provenance;
- commit only from the human review widget.

