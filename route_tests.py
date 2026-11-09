import sys
import subprocess

TESTS = {
    "pricing.py": "tests/test_pricing.py",
    "inventory.py": "tests/test_inventory.py",
    "cart.py": "tests/test_cart.py",
}

changed_files = sys.argv[1:]

if not changed_files:
    selected = list(TESTS.values())
else:
    selected = sorted({
        TESTS[file.split("/")[-1]]
        for file in changed_files
        if file.split("/")[-1] in TESTS
    })

if not selected:
    selected = list(TESTS.values())

subprocess.run([sys.executable, "-m", "pytest", "-v", *selected], check=True)
