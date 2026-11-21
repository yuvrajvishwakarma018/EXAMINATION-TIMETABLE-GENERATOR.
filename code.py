from pathlib import Path
import subprocess, sys, zipfile

out = Path("/mnt/data/restaurant_billing_submission")
code_path = out / "code.py"
source = code_path.read_text(encoding="utf-8")
# Correct newline escape sequences in the Python source for clean console formatting.
source = source.replace(r"\\n", r"\n")
code_path.write_text(source, encoding="utf-8")

cases = {
    "Test 1 – Dosa x2": ("Dosa\n2\ndone\n", ["Dosa x2 added", "160.00"]),
    "Test 2 – Tea x1": ("Tea\n1\ndone\n", ["20.00", "1.00", "21.00"]),
    "Test 3 – invalid inputs": ("Pizza\nDosa\n0\nDosa\nabc\nDosa\n1\ndone\n", ["Item not on the menu", "Quantity must be at least 1", "Invalid quantity"]),
    "Test 4 – discount": ("Thali\n4\nDosa\n2\nTea\n2\ndone\n", ["800.00", "80.00", "36.00", "756.00"]),
}
all_passed = True
for label, (user_input, expected) in cases.items():
    result = subprocess.run([sys.executable, str(code_path)], input=user_input, text=True, capture_output=True)
    passed = result.returncode == 0 and all(value in result.stdout for value in expected)
    all_passed &= passed
    print(f"{label}: {'PASS' if passed else 'FAIL'}")

zip_path = Path("/mnt/data/restaurant_billing_submission.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
    for file in sorted(out.iterdir()):
        archive.write(file, arcname=file.name)

print("\nFinal package refreshed:", zip_path)
print("All tests passed:", all_passed)
