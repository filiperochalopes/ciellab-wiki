# MCP configuration

Connect an MCP client to CIEL Lab with a personal access token generated in
**Settings**. The token is shown only once; replace the placeholder below and
keep it in the client's secret configuration.

```json
{
  "mcpServers": {
    "ciellab": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://ciellab.filipelopes.med.br/api/v2/mcp/",
        "--header",
        "Authorization:Bearer ciel_pat_YOUR_TOKEN_HERE"
      ]
    }
  }
}
```

Replace `ciel_pat_YOUR_TOKEN_HERE` with the personal access token for the
CIEL Lab account. Do not commit the completed configuration or paste the token
into a prompt.

## Approval boundary

MCP can stage a proposal for review, but cannot silently apply it to OCL. A
signed-in user reviews the rows and submits the final changes through the
CIEL Lab widget; submitting queues the selected edits for background processing.

## Propose names and descriptions

The bulk-edit tool can propose **Insert**, **Update**, or **Retire** operations
for names and descriptions. Each proposal contains only one resource type and
one operation; use separate proposals for, for example, updating names and
retiring descriptions. Review the current concept and proposed values before
sending each page of edits.

For an update or retirement, identify the existing active name or description
from the current concept. A target rule must resolve to exactly one active item;
zero or multiple matches reject that item. Retirement requires a reason. Inspect
per-item outcomes after submission and confirm the resulting state in OCL.
See [issue #2792](https://github.com/OpenConceptLab/ocl_issues/issues/2792).

## Search and review mappings

Use the MCP search surface to narrow concepts by mapping system, map type, or
mapping code before proposing a review set. A mapping identifier can be used to
locate an existing mapping when it is known. Search results and review grids use
the OCL inline mapping form so the relationship remains readable across the
application.

Locale filters are **exact** by default: `pt` does not silently include `pt-BR`.
Use an explicit language-family option only when the question is genuinely about
coverage across regional variants. This prevents a bulk-edit target or a review
set from changing a regional name merely because it shares a language prefix.

A proposed mapping change remains a review item. **Update** and **Retire**
operations refer to an existing mapping identifier; **Insert** proposes a new
mapping and therefore has no identifier yet. Review the current mapping, the
proposed fields, and the affected concept before selecting **Send edits** in the
human-facing app.

!!! warning "External display names can arrive later"

    A mapping code and source are the authoritative identity shown immediately.
    An external terminology display name may be resolved asynchronously. A missing
    display name must not be treated as a missing mapping or as permission to
    replace the code with a guess.
