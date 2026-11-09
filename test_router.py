from pathlib import PurePosixPath
import sys

# Each source area is linked to the tests that cover it.
TEST_MAP = {
    "src/pricing.py": ["tests/test_pricing.py"],
    "src/cart.py": ["tests/test_cart.py"],
    "src/inventory.py": ["tests/test_inventory.py"],
}


def select_tests(changed_files):
    selected = set()

    for changed_file in changed_files:
        path = PurePosixPath(changed_file)

        # Run all tests when shared configuration or tests change.
        if path.parts[0] in {"tests", ".github"} or path.name in {
            "requirements.txt",
            "pytest.ini",
        }:
            return ["tests/"]

        selected.update(TEST_MAP.get(changed_file, []))

    # Unknown files may affect anything, so run the full suite.
    return sorted(selected) if selected else ["tests/"]


if __name__ == "__main__":
    changed = sys.argv[1:]
    if not changed:
        changed = ["src/pricing.py"]

    print("Changed files:", ", ".join(changed))
    print("Selected tests:", ", ".join(select_tests(changed)))