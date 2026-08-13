#!/usr/bin/env bash
# Run every example and write TEST_REPORT.md in this directory.

cd "$(dirname "$0")" || exit 1

OUT="TEST_REPORT.md"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Prefer the repo virtual environment, then $PYTHON, then python3.
if [ -x "../.venv/bin/python" ]; then
  PY="../.venv/bin/python"
elif [ -n "$PYTHON" ]; then
  PY="$PYTHON"
else
  PY="python3"
fi

if ! "$PY" -c "import pipeshub_sdk, dotenv" 2>/dev/null; then
  echo "$PY cannot import pipeshub_sdk and python-dotenv."
  echo "Install them first:  uv venv && uv pip install -e .. python-dotenv"
  exit 1
fi

if [ ! -f ".env" ]; then
  echo "No .env in this directory. Copy .env.example to .env first."
  exit 1
fi

export PYTHONUNBUFFERED=1

FILES=$(find . -name '*.py' -not -path './.venv/*' | sed 's|^\./||' | sort)

PASS=0
FAIL=0
GROUP=""

echo "# Example test report" > "$OUT"
echo "" >> "$OUT"
echo "$(date '+%Y-%m-%d %H:%M:%S')" >> "$OUT"
echo "" >> "$OUT"

for f in $FILES; do
  printf '%-46s ' "$f"

  timeout 180 "$PY" "$f" > "$TMP/out" 2> "$TMP/err"
  code=$?

  # Every example raises on failure, so the exit code is the verdict.
  if [ $code -eq 0 ]; then
    status="PASS"
    PASS=$((PASS + 1))
  else
    status="FAIL"
    FAIL=$((FAIL + 1))
  fi
  echo "$status"

  g=$(dirname "$f")
  if [ "$g" != "$GROUP" ]; then
    echo "" >> "$OUT"
    echo "## $g" >> "$OUT"
    echo "" >> "$OUT"
    GROUP="$g"
  fi

  if [ "$status" = "PASS" ]; then
    echo "- [x] $(basename "$f") — PASS" >> "$OUT"
  else
    echo "- [ ] $(basename "$f") — FAIL" >> "$OUT"
    echo "" >> "$OUT"
    echo '  ```' >> "$OUT"
    if [ $code -eq 124 ]; then
      echo "  timed out after 180s" >> "$OUT"
    fi
    grep -v '^[[:space:]]*$' "$TMP/err" | tail -n 20 | sed 's/^/  /' >> "$OUT"
    echo '  ```' >> "$OUT"
    echo "" >> "$OUT"
  fi
done

echo "" >> "$OUT"
echo "**$PASS passed, $FAIL failed**" >> "$OUT"

echo ""
echo "$PASS passed, $FAIL failed"
echo "report: $OUT"
