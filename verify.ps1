$ErrorActionPreference = "Stop"
python -m pytest tests -q
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python -X utf8 -m genvm_linter.cli contracts/scope_sentinel.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Push-Location frontend
try {
  npm test
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
  npm run build
  exit $LASTEXITCODE
} finally { Pop-Location }
