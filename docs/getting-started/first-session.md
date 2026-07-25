# First session

Use this checklist before making a production change.

## 1. Sign in

Open the CIEL Lab URL and sign in with your approved account. New accounts may
require administrator approval before protected tools become available.

## 2. Configure your OCL token

Go to **Settings** and save a personal OCL API token. CIEL Lab encrypts the
token for server-side use and sends mutations to OCL as the current user.

The token determines what you may change. A read-only or insufficiently scoped
token will still allow browsing but will fail on protected writes.

!!! danger

    Never paste an OCL token, CIEL Lab personal access token, database password,
    or service credential into Slack, screenshots, wiki pages, issue comments,
    or an AI prompt.

## 3. Set search preferences

Choose the default:

- search mode: textual or semantic;
- CIEL version: HEAD or a released version;
- semantic suggestions: enabled or disabled.

Use HEAD when reviewing work in progress. Use a fixed release when you need
reproducible historical results.

## 4. Verify freshness

Check the Dashboard and the relevant page timestamp. If data should already
have changed in OCL:

1. try **Reload** first;
2. use **Refresh** only if the cached projection is genuinely stale;
3. wait for the background task to finish before judging the result.

## 5. Start with a reversible workflow

For a first production session:

1. search for an existing concept in [Concept Manager](../features/tools/concept-manager.md);
2. inspect its names and mappings without saving;
3. run or open a QA report;
4. create a worklist checkpoint;
5. review the proposed change before applying it.

## 6. Prepare MCP access only when needed

The MCP App is optional. If an AI client will use CIEL Lab, create a CIEL Lab
personal access token in Settings. It is shown once. Store it in the client's
secret configuration, never in source control.

