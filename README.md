# 서몬나이트 크래프트 소드 이야기 ~시작의 돌~ 한국어 패치

> **v1.0.2 — 문자 처리 및 누락 번역 수정**

게임보이 어드밴스 일본판 `Summon Night - Craft Sword Monogatari - Hajimari no Ishi`용 비공식 한국어 현지화 패치 배포 저장소입니다.

- 게임 코드: `B3CJ`
- 지원 원본 크기: `33,554,432 bytes`
- 지원 원본 SHA-256: `39bc4cf448106aa4b8cdde235632ffb57432c4b1919c8843510b70b3787fad2d`
- 버전·태그: `v1.0.2`
- 저장소: `TeamLimRyan/SUMMON_NIGHT_CRAFT_SWORD_MONOGATARI_HAJIMARI_NO_ISHI_KOREAN_LOCALIZATION_RELEASE`

## 포함 범위

- 정본 텍스트 43,101행과 별도 PSI 문자열 1,769행, 총 44,870행 빌드 반영
- 고정 길이 위치명 필드 136건을 추가 발굴해 메뉴 하단 일본어와 후행 깨짐 제거
- 이미지 대상 149건 중 한국어 이미지 143건 반영, 사용자 결정에 따라 6건 원본 유지
- 현대 한글 완성형 11,172자와 한글 자모 51자 글리프
- 조합식 한글 이름 입력과 한글 자모 키보드
- 용어집, 제어 코드, 포인터, 압축 문자열, 팔레트와 이미지 재삽입 정적 검증
- v1.0.2: 기존 세이브 새 부팅, 로드 확인·목록, 메뉴, 아이템·귀중품, 도감 실행 검증
- v1.0.1에서 확인한 초반 대화·파트너 정보·`임라이언` 입력 이력은 이전 버전 검증 기록으로 보존

## 다운로드

이번 버전은 문자 코드 충돌과 동적 아이템명 깨짐을 수정하고, 누락·부분 추출 필드 1,185개를 보완했습니다. 세이브 목록 지명·선택지·귀중품·도감 화면을 새 부팅으로 확인했습니다. [변경 내역](RELEASE_NOTES.md)과 [검증 한계](COMPATIBILITY_KO.md)를 함께 확인하십시오.

최신 패치는 [GitHub Releases의 v1.0.2](https://github.com/TeamLimRyan/SUMMON_NIGHT_CRAFT_SWORD_MONOGATARI_HAJIMARI_NO_ISHI_KOREAN_LOCALIZATION_RELEASE/releases/tag/v1.0.2)에서 받으십시오.

- 패치: `Summon_Night_Craft_Sword_Monogatari_Hajimari_no_Ishi_KO.xdelta`
- 패치 크기: `5,336,845 bytes`
- 패치 SHA-256: `26b8da47a3d3e45f2838115140023fca588f44c90c78bde48fbf06bd1cbc7c01`

이 저장소와 GitHub Release에는 원본 ROM, 완성 ROM, BIOS, 세이브 데이터를 포함하지 않습니다.

## 설치

Python 3과 `xdelta3`가 준비되어 있으면 저장소 루트에서 다음 명령으로 원본 확인, 패치 적용, 결과 검증을 한 번에 수행할 수 있습니다.

```powershell
python scripts/apply_patch.py "Summon Night - Craft Sword Monogatari - Hajimari no Ishi (Japan).gba"
```

직접 적용할 때는 다음 명령을 사용합니다.

```powershell
xdelta3 -d -s "Summon Night - Craft Sword Monogatari - Hajimari no Ishi (Japan).gba" `
  "Summon_Night_Craft_Sword_Monogatari_Hajimari_no_Ishi_KO.xdelta" `
  "summon_night_craft_sword_hajimari_no_ishi_ko.gba"
```

자세한 절차는 [설치 안내](INSTALL_KO.md), 지원 범위와 검증 한계는 [호환성](COMPATIBILITY_KO.md)을 확인하십시오.

## 결과 무결성

- 결과 크기: `33,554,432 bytes`
- 결과 SHA-256: `8d7efa27855099ab9e47cd5bbe8786aba009ef04e7eaabdf99d796823555012f`

배포 xdelta를 지원 원본에 역적용한 결과가 최종 검증 ROM과 바이트 단위로 일치합니다. 전체 체크섬은 [SHA256SUMS.txt](SHA256SUMS.txt)에 있습니다.

## 오류 제보

[지원 안내](SUPPORT_KO.md)에 따라 원본·패치·출력 해시, xdelta 버전, 운영체제, 에뮬레이터 정보와 재현 순서를 Issues에 남겨 주십시오. ROM·BIOS·세이브 파일은 첨부하지 마십시오.

## 권리

이 프로젝트는 비공식 팬메이드 한국어 패치입니다. 게임, 상표, 로고와 원본 데이터의 권리는 각 권리자에게 있습니다. 사용자는 정당하게 보유한 대상 일본판 ROM을 직접 준비해야 합니다.
