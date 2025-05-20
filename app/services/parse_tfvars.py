import re
from pathlib import Path

def parse_variables_tf(folder_path="infra"):
    var_file = Path(folder_path) / "variables.tf"
    if not var_file.exists():
        return ""

    with open(var_file) as f:
        content = f.read()

    matches = re.findall(r'variable\s+"(.*?)"\s+{[^}]*default\s+=\s+(.*?)[\n}]', content, re.DOTALL)
    results = []
    for name, default in matches:
        results.append(f"- `{name}` = {default.strip()}")
    return "\n".join(results)
