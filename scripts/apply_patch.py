#!/usr/bin/env python3
"""Apply the supported xdelta patch and verify all relevant hashes."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATCH = ROOT / "Summon_Night_Craft_Sword_Monogatari_Hajimari_no_Ishi_KO.xdelta"
SOURCE_SIZE = 33_554_432
SOURCE_SHA256 = "39bc4cf448106aa4b8cdde235632ffb57432c4b1919c8843510b70b3787fad2d"
PATCH_SIZE = 3_294_629
PATCH_SHA256 = "ee5794cf6b4d5aeb6c7e055d3287e144d20b839418ccc267a374002988b281bb"
TARGET_SIZE = 33_554_432
TARGET_SHA256 = "26bed95bc2b9eb640f573384b4b84417f400b251324af4570f3a80ab688a80b7"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_file(path: Path, size: int, digest: str, label: str) -> None:
    if not path.is_file():
        raise SystemExit(f"{label} 파일이 없습니다: {path}")
    actual_size = path.stat().st_size
    actual_digest = sha256_file(path)
    if actual_size != size or actual_digest != digest:
        raise SystemExit(
            f"{label} 검증 실패\n"
            f"  경로: {path}\n"
            f"  크기: {actual_size} (예상 {size})\n"
            f"  SHA-256: {actual_digest}\n"
            f"  예상값: {digest}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="서몬나이트 크래프트 소드 이야기 ~시작의 돌~ 한국어 xdelta 적용기")
    parser.add_argument("source", type=Path, help="지원 대상 일본판 원본 ROM")
    parser.add_argument("output", type=Path, nargs="?", default=Path("summon_night_craft_sword_hajimari_no_ishi_ko.gba"))
    parser.add_argument("--xdelta", default="xdelta3", help="xdelta3 실행 파일 또는 경로")
    parser.add_argument("--force", action="store_true", help="기존 출력 파일 덮어쓰기")
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output.resolve()
    candidate = Path(args.xdelta)
    xdelta = shutil.which(args.xdelta) or (str(candidate.resolve()) if candidate.is_file() else None)
    if xdelta is None:
        raise SystemExit("xdelta3를 찾을 수 없습니다. PATH에 추가하거나 --xdelta로 경로를 지정하십시오.")
    if output.exists() and not args.force:
        raise SystemExit(f"출력 파일이 이미 있습니다: {output}\n덮어쓰려면 --force를 사용하십시오.")

    require_file(source, SOURCE_SIZE, SOURCE_SHA256, "원본 ROM")
    require_file(PATCH, PATCH_SIZE, PATCH_SHA256, "xdelta 패치")
    output.parent.mkdir(parents=True, exist_ok=True)

    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(prefix=output.name + ".", suffix=".tmp", dir=output.parent, delete=False) as handle:
            temp_path = Path(handle.name)
        subprocess.run([xdelta, "-f", "-d", "-s", str(source), str(PATCH), str(temp_path)], check=True)
        require_file(temp_path, TARGET_SIZE, TARGET_SHA256, "패치 결과")
        os.replace(temp_path, output)
        temp_path = None
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"xdelta3 적용 실패: 종료 코드 {exc.returncode}") from exc
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)

    print(f"PASS: {output}")
    print(f"SIZE: {TARGET_SIZE}")
    print(f"SHA-256: {TARGET_SHA256}")


if __name__ == "__main__":
    main()
