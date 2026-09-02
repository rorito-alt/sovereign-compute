"""Command-line interface for SovereignCompute prototype."""

import argparse
import time
import random
from datetime import datetime


def estimate_energy(duration_seconds: int, workload: str) -> float:
    """Very rough energy estimate in Wh (placeholder for real measurement)."""
    # Base power draw assumptions (Watts)
    base = {
        "climate": 45,
        "science": 55,
        "ai-inference": 70,
        "general": 40,
    }.get(workload, 40)
    # Add some variation
    power = base * (0.9 + random.random() * 0.2)
    return (power * duration_seconds) / 3600  # Wh


def contribute(duration: int, workload: str):
    """Simulate contributing idle compute for a public-good workload."""
    print("\n🌱 SovereignCompute — Contribution Session")
    print("=" * 50)
    print(f"Workload type   : {workload}")
    print(f"Duration        : {duration} seconds")
    print(f"Started at      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Privacy mode    : LOCAL ONLY (no data leaves this machine)")
    print("=" * 50)
    print("\nSimulating contribution... (this is a prototype)\n")

    steps = max(1, duration // 5)
    for i in range(steps):
        time.sleep(min(5, duration / steps))
        progress = int(((i + 1) / steps) * 100)
        print(f"  [{progress:3d}%] Processing public-good workload...", end="\r")

    energy = estimate_energy(duration, workload)
    print("\n\n✅ Contribution complete.")
    print(f"Estimated energy used : {energy:.2f} Wh")
    print("Thank you for contributing to the compute commons.")
    print("Your device stayed under your control the entire time.\n")


def main():
    parser = argparse.ArgumentParser(
        prog="sovereign-compute",
        description="SovereignCompute — citizen-powered, privacy-first distributed compute toolkit",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # contribute command
    contrib = subparsers.add_parser("contribute", help="Contribute idle compute to a public-good workload")
    contrib.add_argument(
        "--duration", type=int, default=30,
        help="How many seconds to contribute (default: 30)"
    )
    contrib.add_argument(
        "--workload", choices=["climate", "science", "ai-inference", "general"],
        default="climate",
        help="Type of public-good workload (default: climate)"
    )

    # version command
    subparsers.add_parser("version", help="Show version")

    args = parser.parse_args()

    if args.command == "contribute":
        contribute(args.duration, args.workload)
    elif args.command == "version":
        from sovereign_compute import __version__
        print(f"SovereignCompute v{__version__}")


if __name__ == "__main__":
    main()
