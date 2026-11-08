"""
Pattern course test runner.

  python practice.py                 # progress across every pattern
  python practice.py 3               # test your answers for pattern 3
  python practice.py 3 --solutions   # see the model solutions pass for pattern 3
  python practice.py 3 --reset       # blank c_practice.py for pattern 3 (your old answers are kept in c_practice_backup.py)
"""
import importlib.util
import shutil
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).parent / "patterns"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def pattern_dirs():
    return sorted(p for p in ROOT.iterdir()
                  if p.is_dir() and p.name[:2].isdigit() and (p / "f_tests.py").exists())


def run_pattern(folder, use_solutions=False, quiet=False):
    """Run every test_* function in f_tests.py against c_practice.py (or d_solutions.py)."""
    code_file = folder / ("d_solutions.py" if use_solutions else "c_practice.py")
    tests = load(folder / "f_tests.py", f"tests_{folder.name}")
    try:
        code = load(code_file, f"code_{folder.name}")
    except Exception as e:
        if not quiet:
            print(f"  Could not load {code_file.name}: {type(e).__name__}: {e}")
        return 0, len([n for n in dir(tests) if n.startswith("test_")])

    names = [n for n in vars(tests) if n.startswith("test_")]
    passed = 0
    for n in names:
        label = n[5:]
        try:
            getattr(tests, n)(code)
            passed += 1
            if not quiet:
                print(f"  PASS  {label}")
        except AssertionError:
            if not quiet:
                frame = traceback.extract_tb(sys.exc_info()[2])[-1]
                print(f"  FAIL  {label}   (f_tests.py line {frame.lineno}: {frame.line})")
        except Exception as e:
            if not quiet:
                print(f"  ERR   {label}   {type(e).__name__}: {e}")
    return passed, len(names)


def title(folder):
    lesson = folder / "a_lesson.md"
    if lesson.exists():
        first = lesson.read_text().splitlines()[0]
        return first.lstrip("# ").split(" (")[0].strip()
    return folder.name


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    use_solutions = "--solutions" in sys.argv
    folders = pattern_dirs()

    if args:
        number = int(args[0])
        match = [f for f in folders if int(f.name[:2]) == number]
        if not match:
            print(f"No pattern {number}. Run `python practice.py` to see them all.")
            return
        folder = match[0]
        if "--reset" in sys.argv:
            shutil.copy(folder / "c_practice.py", folder / "c_practice_backup.py")
            shutil.copy(folder / "g_blank.py", folder / "c_practice.py")
            print(f"{title(folder)}: c_practice.py is blank again.")
            print("Your previous answers are in practice_backup.py. Now write them from memory.")
            return
        print(f"{title(folder)}  ({'solutions' if use_solutions else 'your answers'})\n")
        passed, total = run_pattern(folder, use_solutions)
        print(f"\n{passed}/{total} tests passed")
        if passed == total and not use_solutions:
            print(f"All passing. Tomorrow, run `python practice.py {number} --reset` and write them again from memory.")
        return

    print("Your progress (tests passing in each c_practice.py)\n")
    for folder in folders:
        passed, total = run_pattern(folder, use_solutions, quiet=True)
        bar = "#" * passed + "." * (total - passed)
        done = "  done" if total and passed == total else ""
        print(f"  {title(folder):<44} {bar:<6} {passed}/{total}{done}")
    print("\nTest one pattern:  python practice.py <number>")


if __name__ == "__main__":
    main()
