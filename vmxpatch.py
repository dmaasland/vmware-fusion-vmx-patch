#!/usr/bin/env python3

import logging
from argparse import ArgumentParser, Namespace
from pathlib import Path, PurePath
from shutil import copy
from time import time
from typing import Callable, Dict, List, Optional, Tuple


class VmxEncryptedError(Exception):
    pass


def parse_args() -> Namespace:
    logging.debug("Grabbing arguments")

    parser = ArgumentParser()
    parser.add_argument(
        "vm_dir",
        metavar="<vm dir>",
        type=str,
        nargs="+",
        help="Path to the virtual machine directory.",
    )
    parser.add_argument(
        "-t",
        metavar="tweaks",
        type=str,
        help="Path to .vmx file containing tweaks",
        default=PurePath(PurePath(__file__).parent, "tweaks.vmx"),
    )

    args = parser.parse_args()
    logging.debug(f"VM directory is: {args.vm_dir}")
    return args


def find_vmx(vm_dir: str) -> Optional[Path]:
    vmx_files = Path(vm_dir).glob("*.vmx")
    vmx = next(vmx_files, None)

    if vmx == None:
        logging.warning(f"No .vmx files found in folder {vm_dir}")

    if next(vmx_files, None) is not None:
        logging.warning(f"Multiple .vmx files found in folder {vm_dir}")

    return vmx


def backup_vmx(vmx: Path) -> None:
    backup_file = PurePath(vmx.parent, f"{vmx.name}.{int(time())}.backup")
    logging.info(f"Creating backup file {backup_file}")
    copy(vmx, backup_file)


def patch_vmx(args: Namespace) -> None:
    for vm_dir in args.vm_dir:
        logging.debug(f"Processing directory {vm_dir}")

        vmx = find_vmx(vm_dir)

        if vmx is None:
            continue

        logging.info(f"Processing VMX {vmx}")

        backup_vmx(vmx)

        try:
            logging.debug(f"Parsing VMX {vmx}")
            parsed_vmx = parse_vmx(vmx)

        except VmxEncryptedError:
            continue

        logging.debug(f"Parsing tweaks {args.t}")
        tweaks = parse_vmx(args.t)

        logging.debug("Updating vmx")
        parsed_vmx.update(tweaks)

        logging.info("Writing new vmx")
        with open(str(vmx), "w") as f:

            for i in parsed_vmx.items():
                option = str(f"{i[0]} = {i[1]}\n")
                logging.debug(f"Setting option {option.strip()}")
                f.write(option)


def parse_vmx(vmx: Path) -> Dict[str, str]:
    parsed_vmx: Dict[str, str] = {}

    with open(vmx, "r") as f:
        for line in f:

            if line.startswith("#"):
                continue

            vmx_kv: Callable[[List[str]], Tuple[str, str]] = lambda x: (
                x[0].strip(),
                "=".join(x[1:]).strip(),
            )

            vmx_key, vmx_value = vmx_kv(line.split("="))
            parsed_vmx.update({vmx_key: vmx_value})

    if "encryption.data" in parsed_vmx:
        logging.critical(f"VMX file {vmx} is encrypted, impossible to patch!")
        raise VmxEncryptedError

    return parsed_vmx


def main() -> None:
    args = parse_args()
    patch_vmx(args)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
    main()
