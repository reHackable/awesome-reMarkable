import re
import sys

SHIELDS_TEMPLATE = """  <!-- shields -->

  ![Github stars](https://shields.io/github/stars/{repo}?style=social)
  ![Languages](https://shields.io/github/languages/top/{repo})
  ![License](https://shields.io/github/license/{repo})
  ![Last commit](https://shields.io/github/last-commit/{repo})
  ![Issues](https://shields.io/github/issues/{repo})
  <!-- /shields -->
"""
SHIELDS_RE = re.compile(r"  <!-- shields -->.*?<!-- /shields -->\n", re.DOTALL)
GITHUB_RE = re.compile(r"- \[.*?\]\(https://github.com/([-_.\w]*/[-_.\w]*)")

def insert_shields(filename):
    contents = open(filename, 'r').read()
    contents = SHIELDS_RE.sub('', contents)

    with open(filename, 'w') as f:
        for line in contents.splitlines():
            f.write(line + '\n')
            match = GITHUB_RE.match(line)
            if match:
                f.write(SHIELDS_TEMPLATE.format(repo=match[1]))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} filename")
        sys.exit(1)
    insert_shields(sys.argv[1])
