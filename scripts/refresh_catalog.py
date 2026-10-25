"""Refresh GitHub metadata in data/catalog.json: stars, last push month and archived status.

A repo that is gone or no longer public is marked "unavailable" and hidden on the site.
Usage: GITHUB_TOKEN=... python scripts/refresh_catalog.py
"""
import json, os, sys, urllib.error, urllib.request
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "data" / "catalog.json"
TOKEN = os.environ.get("GITHUB_TOKEN")


def get_repo(full_name):
    req = urllib.request.Request(f"https://api.github.com/repos/{full_name}", headers={"Accept": "application/vnd.github+json", "User-Agent": "starter-kit-refresh"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (404, 451):
            return None
        raise


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    changed, gone = 0, []
    for it in data["items"]:
        if not it.get("repo"):
            continue
        r = get_repo(it["repo"])
        if r is None or r.get("private") or r.get("visibility", "public") != "public":
            if not it.get("unavailable"):
                it["unavailable"] = True
                gone.append(it["repo"])
                changed += 1
            continue
        new = {"stars": r["stargazers_count"], "updated": (r.get("pushed_at") or "")[:7] or None, "archived": bool(r.get("archived"))}
        if it.pop("unavailable", None):
            changed += 1
        for k, v in new.items():
            if it.get(k) != v:
                it[k] = v
                changed += 1
    if changed:
        PATH.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"fields changed: {changed}")
    if gone:
        print("now unavailable (hidden on the site):", ", ".join(gone))


if __name__ == "__main__":
    sys.exit(main())
