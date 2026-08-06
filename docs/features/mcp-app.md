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

MCP prepares a preview only. A signed-in user reviews and commits the final
OCL change through CIEL Lab; the MCP client cannot silently persist it.
