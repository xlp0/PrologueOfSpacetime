---
name: opencode-cli
description: "Use when the user says 'opencode-cli', 'install opencode cli', 'install opencode command line', 'add opencode to PATH', 'opencode not found', 'opencode command not found', or '/opencode-cli'. Installs the opencode CLI globally so it is accessible from any terminal/directory. Handles macOS, Linux, and Windows. Checks if opencode is already installed, installs if missing, ensures it is on PATH globally, and verifies it works from any directory. Use when participants have opencode Desktop but need the CLI version too."
---

# opencode-cli — Install opencode CLI Globally

Installs the opencode CLI so `opencode` works from any terminal, any directory. Participants already have opencode Desktop — this adds the command-line version.

## What this skill does

1. Checks if `opencode` is already on PATH
2. If not, installs it using the official installer
3. Ensures it's on PATH globally (shell profile)
4. Verifies it works from any directory

## Phase 1 — Detect OS and check if opencode is installed

### Step 1.1 — Detect OS

```bash
# macOS
uname -s    # "Darwin"

# Linux
uname -s    # "Linux"

# Windows (PowerShell)
$env:OS     # "Windows_NT"
```

### Step 1.2 — Check if opencode is already on PATH

```bash
# macOS / Linux
which opencode 2>/dev/null && opencode --version

# Windows (PowerShell)
Get-Command opencode -ErrorAction SilentlyContinue
opencode --version
```

If `opencode --version` returns a version string, opencode CLI is already installed. Skip to Phase 3 (verify global access). If not found, proceed to Phase 2.

## Phase 2 — Install opencode CLI

### macOS / Linux

```bash
curl -fsSL https://opencode.ai/install | bash
```

This downloads opencode to `~/.opencode/bin/opencode` and adds `~/.opencode/bin` to the shell profile (`.zshrc` for zsh, `.bashrc` for bash).

### Windows (PowerShell)

```powershell
irm https://opencode.ai/install.ps1 | iex
```

This downloads opencode to `%USERPROFILE%\.opencode\bin\opencode.exe` and adds it to the user PATH.

> **Windows:** The participant must restart their terminal after install for PATH to take effect.

## Phase 3 — Ensure global PATH access

### Step 3.1 — Check PATH includes opencode bin directory

**macOS / Linux:**

```bash
# Check if ~/.opencode/bin is in PATH
echo $PATH | grep -q ".opencode/bin" && echo "PATH OK" || echo "PATH MISSING"
```

If PATH is missing, add it to the shell profile:

```bash
# Detect shell
SHELL_NAME=$(basename "$SHELL")

# zsh (default on macOS)
if [ "$SHELL_NAME" = "zsh" ]; then
  echo 'export PATH="$HOME/.opencode/bin:$PATH"' >> ~/.zshrc
  source ~/.zshrc
fi

# bash
if [ "$SHELL_NAME" = "bash" ]; then
  echo 'export PATH="$HOME/.opencode/bin:$PATH"' >> ~/.bashrc
  source ~/.bashrc
fi
```

**Windows (PowerShell):**

```powershell
# Check if opencode bin is in user PATH
$path = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($path -notlike "*\.opencode\bin*") {
    $newPath = "$env:USERPROFILE\.opencode\bin;$path"
    [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
    Write-Host "Added opencode to PATH. Restart your terminal."
}
```

### Step 3.2 — Verify from a different directory

```bash
# Change to home directory and test
cd ~
opencode --version
```

If this prints a version, opencode is globally accessible. If not, see troubleshooting.

## Phase 4 — Report

Tell the participant:

> *"opencode CLI is installed and globally accessible.*
> *Version: [version]*
> *Location: [path to opencode binary]*
> *PATH: [confirmed working from any directory]*
>
> *You can now run `opencode chat` from any terminal, any directory.*
> *Your opencode Desktop is still there too — both work."*

## Troubleshooting

### `opencode: command not found` after install

**macOS:**
1. Check if `~/.opencode/bin/opencode` exists: `ls -la ~/.opencode/bin/`
2. If it exists, the PATH wasn't updated. Manually add it:
   ```bash
   echo 'export PATH="$HOME/.opencode/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```
3. If `~/.opencode/` doesn't exist, the install failed. Re-run:
   ```bash
   curl -fsSL https://opencode.ai/install | bash
   ```

**Windows:**
1. Check if `%USERPROFILE%\.opencode\bin\opencode.exe` exists
2. If it exists, restart the terminal (PATH changes need a new session)
3. If the folder doesn't exist, re-run: `irm https://opencode.ai/install.ps1 | iex`

### `opencode` works in one terminal but not another

The PATH was set in the shell profile but the other terminal was opened before the change. Close and reopen the terminal, or run `source ~/.zshrc` (macOS) / restart PowerShell (Windows).

### Permission denied (macOS/Linux)

```bash
chmod +x ~/.opencode/bin/opencode
```

### Corporate proxy / firewall blocking curl

Try with proxy:
```bash
curl -fsSL --proxy http://your-proxy:port https://opencode.ai/install | bash
```

Or download manually from https://opencode.ai and place the binary in `~/.opencode/bin/`.

## What this skill does NOT do

- Does NOT install GLM 5.2 or configure the API key (use the `glm-setup` or `ai-setup` skill for that)
- Does NOT install opencode Desktop (the participant already has it)
- Does NOT configure MCP servers (use `ai-setup` Stage 2)
- Does NOT create an Obsidian vault (use the `onboarding` skill)

## Related skills

- **glm-setup** — configures GLM 5.2 API key for opencode (run AFTER this skill)
- **ai-setup** — full two-stage onboarding (GLM + all tools). This skill is a subset of Stage 1.
- **prereq-checker** — scans machine for all required tools including opencode

## References

- [opencode official site](https://opencode.ai)
- [opencode install guide (this repo)](../../docs/opencode-setup-guide.md)
- [opencode OKF doc](../../okf/tech-stack/opencode.md)
