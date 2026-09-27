import argparse
import sys

from .transpiler import compile_sunda, transpile


def main():
    parser = argparse.ArgumentParser(
        prog="sunda",
        description="SundaPy — jalankeun program basa Sunda (dumasar Python).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="Jalankeun file .sun langsung")
    run_p.add_argument("file", help="Path ka file .sun")

    compile_p = sub.add_parser("compile", help="Robah file .sun jadi file .py")
    compile_p.add_argument("file", help="Path ka file .sun")
    compile_p.add_argument("-o", "--output", help="Path file .py output")

    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: file '{args.file}' teu kapendak.", file=sys.stderr)
        sys.exit(1)

    if args.command == "run":
        try:
            code_obj = compile_sunda(source, filename=args.file)
        except SyntaxError as e:
            print(f"Syntax error: {e}", file=sys.stderr)
            sys.exit(1)
        exec(code_obj, {"__name__": "__main__"})

    elif args.command == "compile":
        python_code = transpile(source)
        out_path = args.output or (
            args.file.rsplit(".", 1)[0] + ".py" if "." in args.file else args.file + ".py"
        )
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(python_code)
        print(f"Disimpen di: {out_path}")


if __name__ == "__main__":
    main()
