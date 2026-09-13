#!/usr/bin/env python3
"""Practice 10 and its absence dual, enforced mechanically (2026-09-13).

Every path that a hashed row of tubitak/docs/evidence/MANIFEST.md names must resolve in the
index being committed. Run by scripts/hooks/pre-commit on every commit; takes no arguments
(tubitak/tests/_guard.py convention: refuses any). Exit 1 lists the rows whose file is not
in the index. Reads the STAGED manifest (git show :path) and the STAGED file list
(git ls-files --cached), never the working tree, so it judges the commit and not the disk.

Origin: corrections-log entries 35 and 48. The 260 raster rows pointed at paths that did not
exist from 27 August (6750978 reverted the prefix 284571b had applied) until 13 September,
and nothing noticed, because the manifest was a document and not a check.
"""
import re, subprocess, sys
MANIFEST = "tubitak/docs/evidence/MANIFEST.md"
ROW = re.compile(r"^\| `([^`]+)`[^|]*\| `[0-9a-f]{64}` \| [\d,]+ \|")

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True)

def main():
    if len(sys.argv) > 1:
        sys.exit("manifest_paths_check.py takes no arguments")
    top = git("rev-parse", "--show-toplevel")
    if top.returncode != 0:
        sys.exit("manifest_paths_check.py: not inside a git repository")
    staged = git("show", f":{MANIFEST}")
    if staged.returncode != 0:
        in_head = git("cat-file", "-e", f"HEAD:{MANIFEST}").returncode == 0
        if in_head:
            sys.exit(f"manifest check: {MANIFEST} is in HEAD but not in the index; a commit that removes the manifest is refused")
        print("manifest check: no manifest in the index, nothing to check"); return
    index = set(git("ls-files", "--cached", "-z").stdout.split("\0"))
    rows = [ROW.match(l).group(1) for l in staged.stdout.splitlines() if ROW.match(l)]
    missing = [p for p in rows if f"tubitak/docs/evidence/{p}" not in index]
    if not rows:
        sys.exit("manifest check: the staged manifest has no hashed rows; refusing to certify an empty manifest")
    if missing:
        print(f"manifest check: {len(missing)} of {len(rows)} manifest rows name a path that is not in the index:")
        for p in missing[:10]:
            print(f"  tubitak/docs/evidence/{p}")
        if len(missing) > 10:
            print(f"  ... and {len(missing) - 10} more")
        sys.exit(1)
    print(f"manifest check: {len(rows)} of {len(rows)} manifest rows resolve in the index")

if __name__ == "__main__":
    main()
