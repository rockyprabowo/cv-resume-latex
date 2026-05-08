#!/usr/bin/env python3
"""Generate next date-based tag in YYYYMMDD-N format.

Rules:
- Only considers tags matching today's date prefix: YYYYMMDD-N
- Bumps N by 1 from the highest existing value for today
- Starts at N=1 when no tag exists for today
"""

from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys


def get_tags() -> list[str]:
    proc = subprocess.run(
        ["git", "tag", "--list"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def main() -> int:
    today = dt.date.today().strftime("%Y%m%d")
    pattern = re.compile(rf"^{today}-(\d+)$")

    max_n = 0
    for tag in get_tags():
        match = pattern.match(tag)
        if match:
            max_n = max(max_n, int(match.group(1)))

    print(f"{today}-{max_n + 1}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
