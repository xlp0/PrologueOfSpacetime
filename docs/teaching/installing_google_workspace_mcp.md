---
title: 'Installing the Google Workspace MCP Server'
date: 2026-07-07
tags: [MCP, Google-Workspace, Setup-Guide, OpenCode, Seven-Liberal-Arts]
type: note
sources: ['https://github.com/taylorwilsdon/google_workspace_mcp', 'https://workspacemcp.com/quick-start']
status: stable
liberal_art: Trivium-Grammar
---

# Installing the Google Workspace MCP Server

> A reproducible setup guide for wiring [`taylorwilsdon/google_workspace_mcp`](https://github.com/taylorwilsdon/google_workspace_mcp) into OpenCode, so any agent in the vault can read/write Gmail, Drive, Calendar, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat on behalf of an authenticated user.

## Objective

By the end of this guide, a contributor will be able to ask any OpenCode agent questions like *"what's on my calendar today?"* or *"create a Doc with..."* and have the agent answer by calling Google Workspace APIs through a locally-running MCP server, with OAuth tokens cached on disk so consent only happens once.

Verified working 2026-07-07 on macOS (Darwin) against `henrykoo1230@gmail.com`.

## Prerequisites

| Requirement | Why | Check |
|:---|:---|:---|
| **Python 3.10+** | Server runtime | `python3 --version` |
| **[uv](https://github.com/astral-sh/uv) / uvx** | Launches the server in an isolated env | `uv --version` |
| **OpenCode** (or any MCP client) | Consumes the server | `opencode --version` |
| **A Google account** | The user the server impersonates | — |
| **A Google Cloud project** | Where the OAuth client lives | [console.cloud.google.com](https://console.cloud.google.com/) |

No Google Workspace paid plan is required — a free Gmail account works.

## Phases

### Phase 1: Create the Google Cloud OAuth Client

- **Goal:** Obtain a `GOOGLE_OAUTH_CLIENT_ID` and (optional) `GOOGLE_OAUTH_CLIENT_SECRET`.
- **Steps:**
  1. Open the [Google Cloud Console](https://console.cloud.google.com/) → create or pick a project.
  2. **Google Auth Platform** → *Clients* → **Create OAuth client ID**.
  3. Application type: **Desktop app** (simplest for local stdio use; no redirect URIs to configure).
  4. Name it anything (e.g. `teachers`). Note: the name is internal-only.
  5. **Copy the Client ID and Client Secret immediately** — the secret is only shown once.
- **Success criteria:** You have two strings that look like:
  - Client ID: `952073235739-xxxxx.apps.googleusercontent.com`
  - Client Secret: `GOCSPX-xxxxxxxxxxxxxxxxxxxx`

### Phase 2: Enable the APIs You'll Use

- **Goal:** The OAuth client has scopes for the services you want to call.
- **Steps:** In the same Google Cloud project, go to *APIs & Services → Library* and enable each service you'll touch. Direct links:
  - [Gmail](https://console.cloud.google.com/flows/enableapi?apiid=gmail.googleapis.com)
  - [Drive](https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com)
  - [Calendar](https://console.cloud.google.com/flows/enableapi?apiid=calendar-json.googleapis.com)
  - [Docs](https://console.cloud.google.com/flows/enableapi?apiid=docs.googleapis.com)
  - [Sheets](https://console.cloud.google.com/flows/enableapi?apiid=sheets.googleapis.com)
  - [Slides](https://console.cloud.google.com/flows/enableapi?apiid=slides.googleapis.com)
  - [Forms](https://console.cloud.google.com/flows/enableapi?apiid=forms.googleapis.com)
  - [Tasks](https://console.cloud.google.com/flows/enableapi?apiid=tasks.googleapis.com)
  - [Chat](https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com) — needs extra Chat-app config, see repo README
  - [People (Contacts)](https://console.cloud.google.com/flows/enableapi?apiid=people.googleapis.com)
  - [Apps Script](https://console.cloud.google.com/flows/enableapi?apiid=script.googleapis.com)
  - [Custom Search](https://console.cloud.google.com/flows/enableapi?apiid=customsearch.googleapis.com)
- **Success criteria:** Each enabled API shows "API enabled" in the Library.

### Phase 3: Add Yourself as a Test User (if app is in Testing mode)

- **Goal:** Allow your Google account to grant consent before the app is published.
- **Steps:** Google Auth Platform → *OAuth consent screen* → *Test users* → **ADD USERS** → add the Gmail address you'll authenticate as.
- **Alternative:** Publish the app (OAuth consent screen → *Publishing* → *Push to production*). Publishing avoids the test-user restriction but Google may request verification if you request sensitive scopes.
- **Success criteria:** Your email appears in the Test users list, OR the app is in production.

### Phase 4: Export Credentials to Your Shell

- **Goal:** The MCP server can read the OAuth client ID/secret from the environment.
- **Steps:** Append to `~/.zshrc` (or `~/.bashrc`):

  ```sh
  # Google Workspace MCP (taylorwilsdon/google_workspace_mcp)
  export GOOGLE_OAUTH_CLIENT_ID="your-client-id.apps.googleusercontent.com"
  export GOOGLE_OAUTH_CLIENT_SECRET="GOCSPX-your-secret"
  export OAUTHLIB_INSECURE_TRANSPORT=1   # allows http://localhost callback; safe for local stdio
  ```

  Then reload: `source ~/.zshrc` (or open a new terminal).
- **Success criteria:** `echo $GOOGLE_OAUTH_CLIENT_ID` prints the client ID.

### Phase 5: Register the MCP Server in OpenCode

- **Goal:** OpenCode spawns the server as a local MCP subprocess.
- **Steps:** Add a `google-workspace` entry to the `mcp` object in `~/.config/opencode/opencode.json`:

  ```json
  {
    "mcp": {
      "google-workspace": {
        "type": "local",
        "command": ["uvx", "workspace-mcp", "--tool-tier", "core"],
        "enabled": true,
        "env": {
          "GOOGLE_OAUTH_CLIENT_ID": "{env:GOOGLE_OAUTH_CLIENT_ID}",
          "GOOGLE_OAUTH_CLIENT_SECRET": "{env:GOOGLE_OAUTH_CLIENT_SECRET}",
          "OAUTHLIB_INSECURE_TRANSPORT": "{env:OAUTHLIB_INSECURE_TRANSPORT}"
        }
      }
    }
  }
  ```

  Notes:
  - `{env:VAR}` is OpenCode's interpolation syntax (the shell-style `${VAR}` is **not** substituted).
  - Tool tiers: `core` (essential) → `extended` → `complete` (all tools). Start with `core`, bump later.
  - To cherry-pick services instead of using tiers: `["uvx", "workspace-mcp", "--tools", "gmail", "drive", "calendar"]`.
- **Success criteria:** `opencode.json` validates (`$schema` is `https://opencode.ai/config.json`).

### Phase 6: Restart OpenCode and Authenticate

- **Goal:** OpenCode loads the new MCP server and the user completes OAuth consent.
- **Steps:**
  1. **Quit and restart OpenCode** from a shell that sourced `~/.zshrc`. Config is loaded once at startup; hot-reload is not supported.
  2. In an OpenCode session, ask the agent to call any google-workspace tool with the email you added as a test user. Example natural-language prompt: *"list my Google calendars for henrykoo1230@gmail.com"*.
  3. The agent will call `list_calendars`, the MCP server will detect no cached token, and **open a browser tab** to Google's consent screen. If it doesn't auto-open, the tool error returns the auth URL — paste it into Chrome.
  4. Pick the matching Google account → click **Continue** / **Allow** on the consent screen (it lists every scope the server requested).
  5. The browser will redirect to `http://localhost:8000/oauth2callback?...` and show **"Authentication Successful — credentials have been securely saved."**
  6. Tell the agent to retry — the tool should now return real data.
- **Success criteria:** Tokens cached at `~/.google_workspace_mcp/credentials/` and the tool returns data instead of an auth URL.

## Verification

Run any google-workspace tool. Two good smoke tests:

| Test | Tool | Example call |
|:---|:---|:---|
| List calendars | `google-workspace_list_calendars` | `user_google_email=you@gmail.com` |
| Search unread Gmail | `google-workspace_search_gmail_messages` | `user_google_email=you@gmail.com`, `query="is:unread"`, `max_results=5` |

If either returns real data, the install is end-to-end working.

## Troubleshooting

| Symptom | Cause | Fix |
|:---|:---|:---|
| Tool keeps returning auth URL | OAuth roundtrip never completed | Open the URL in the error manually in Chrome, complete consent, watch for the `localhost:8000/oauth2callback` redirect to succeed |
| `redirect_uri_mismatch` | Wrong OAuth client type, or redirect URI not in allowed list | Use a **Desktop app** client (no redirect URIs to configure); for Web app clients, add `http://localhost:8000/oauth2callback` to authorized redirect URIs |
| `state mismatch` / `state expired` | OAuth state token timed out before you completed consent | Trigger a fresh tool call to get a new URL |
| `access_denied` / `not a test user` | App is in Testing mode and your email isn't on the test-user list | Add your email under *OAuth consent screen → Test users*, OR publish the app |
| `invalid_client` / `invalid_grant` | Wrong client ID/secret, or env vars not exported in the shell that launched OpenCode | `source ~/.zshrc` then restart OpenCode; verify with `echo $GOOGLE_OAUTH_CLIENT_ID` |
| Browser auto-open doesn't fire | Headless environment, or browser-opening disabled | Copy the auth URL from the tool error into a browser manually |
| Tools missing (e.g. `manage_event` not found) | Tool tier filters them out | Bump `--tool-tier core` to `extended` or `complete` in `opencode.json` and restart |

## Security Notes

- **Credentials never enter git.** They live in `~/.zshrc`, `~/.config/opencode/opencode.json`, and `~/.google_workspace_mcp/credentials/` — all outside the repo. The repo `.gitignore` also blocks `.env*`, `client_secret*.json`, `credentials*.json`, `oauth*.json`, `*.pem`, `*.key` defensively.
- **The server sends data only to Google's APIs** using your own OAuth client. No telemetry, no third-party services. See the [Security & Compliance section of the repo README](https://github.com/taylorwilsdon/google_workspace_mcp#security--compliance).
- **Rotate the client secret if it was ever shared.** Google Cloud Console → Auth Platform → Clients → reset. Then update `~/.zshrc` and re-authenticate.
- **Never commit `opencode.json` if it contains inline secrets.** The pattern above uses `{env:VAR}` interpolation, so the file itself is safe — but double-check before committing.

## Timeline

| Phase | Effort | Notes |
|:---|:---|:---|
| 1 — OAuth Client | ~5 min | One-time per Google Cloud project |
| 2 — Enable APIs | ~5 min | One-time per service you'll use |
| 3 — Test User | ~1 min | Skip if app is published |
| 4 — Shell env | ~2 min | One-time per machine |
| 5 — OpenCode config | ~2 min | One-time per machine |
| 6 — Restart + auth | ~3 min | One-time per Google account |

**Total: ~20 minutes for a fresh install.**

## Dependencies

- [[AGENTS]] §8.1 (Tooling — Search/qmd) and §8.2 (Slides — Marp) describe the broader MCP-friendly toolchain this server plugs into.
- [[local_model_demo_setup]] — workshop-scope doc that picked this MCP server for the school-Dell hands-on day, along with `Qwen2.5-3B-Instruct` as the local model. This guide is the verified install procedure; that doc is the workshop plan.
- [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) — the upstream project.
- [workspacemcp.com/quick-start](https://workspacemcp.com/quick-start) — official quick start with screenshots.
- OpenCode config reference: <https://opencode.ai/config.json>.

## Risks

- **OAuth scopes are broad.** The default core tier requests read/write access to Gmail, Drive, Calendar, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat. For least-privilege setups, use `--read-only` or `--permissions service:level` (e.g. `gmail:readonly drive:full`) — see [Granular Permissions in the repo README](https://github.com/taylorwilsdon/google_workspace_mcp#-granular-permissions).
- **Multi-user / hosted deployments** require OAuth 2.1 (`MCP_ENABLE_OAUTH21=true`) and `streamable-http` transport, not stdio. Out of scope for this guide — see the repo README.
- **Google may rate-limit** aggressive usage. Start with `--tool-tier core` and only escalate when needed.
