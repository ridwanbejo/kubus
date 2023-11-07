import argparse

from libs.cores.scanner import KubusScanner


def main():
    parser = argparse.ArgumentParser(
        prog="Kubus",
        description="Kubus is Kubernetes security scanner based on CIS Benchmark",
        epilog="This is just a demo project for PyCon ID 2023",
    )
    parser.add_argument(
        "--dist",
        type=str,
        dest="distribution",
        help="Distribution of your Kubernetes cluster (e.g. Minikube)",
    )
    parser.add_argument(
        "--target", type=str, dest="target", help="Node target for scanning"
    )

    args = parser.parse_args()

    scanner = KubusScanner(distribution=args.distribution, node_target=args.target)
    scanner.run()


if __name__ == "__main__":
    main()
