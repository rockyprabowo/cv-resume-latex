#!/usr/bin/env python3
"""Generate next date-based tag in YYYYMMDD-N format.

Rules:
- Considers tags matching YYYYMMDD-N
- Uses effective date = max(local today, latest tagged date)
- Bumps N by 1 from the highest existing value on the effective date
- Starts at N=1 when no tag exists on the effective date
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
    pattern = re.compile(r"^(\d{8})-(\d+)$")

    by_date: dict[str, int] = {}
    for tag in get_tags():
        match = pattern.match(tag)
        if match:
            date_part = match.group(1)
            seq = int(match.group(2))
            by_date[date_part] = max(by_date.get(date_part, 0), seq)

    latest_tag_date = max(by_date.keys()) if by_date else today
    effective_date = max(today, latest_tag_date)
    next_seq = by_date.get(effective_date, 0) + 1

    print(f"{effective_date}-{next_seq}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
