# 설치 안내

## 준비물

- 대상 일본판 GBA ROM
- `xdelta3`
- 저장소 루트의 `Summon_Night_Craft_Sword_Monogatari_Hajimari_no_Ishi_KO.xdelta`

원본 ROM은 이 저장소에서 제공하지 않습니다.

## 원본 확인

```powershell
Get-FileHash "Summon Night - Craft Sword Monogatari - Hajimari no Ishi (Japan).gba" -Algorithm SHA256
```

정상 원본은 크기 `33,554,432 bytes`, SHA-256 `39bc4cf448106aa4b8cdde235632ffb57432c4b1919c8843510b70b3787fad2d`입니다. 해시가 다르면 적용하지 마십시오.

## 자동 적용과 검증

```powershell
python scripts/apply_patch.py "Summon Night - Craft Sword Monogatari - Hajimari no Ishi (Japan).gba"
```

기본 출력은 `summon_night_craft_sword_hajimari_no_ishi_ko.gba`입니다. 출력 경로와 xdelta 실행 파일을 직접 지정할 수도 있습니다.

```powershell
python scripts/apply_patch.py "원본.gba" "내 폴더/시작의 돌 한국어.gba" `
  --xdelta "C:\Tools\xdelta3.exe"
```

## 직접 적용

```powershell
xdelta3 -d -s "Summon Night - Craft Sword Monogatari - Hajimari no Ishi (Japan).gba" `
  "Summon_Night_Craft_Sword_Monogatari_Hajimari_no_Ishi_KO.xdelta" `
  "summon_night_craft_sword_hajimari_no_ishi_ko.gba"
```

## 결과 확인

```powershell
Get-FileHash "summon_night_craft_sword_hajimari_no_ishi_ko.gba" -Algorithm SHA256
```

- 크기: `33,554,432 bytes`
- SHA-256: `8d7efa27855099ab9e47cd5bbe8786aba009ef04e7eaabdf99d796823555012f`

기존 일본판 세이브를 사용하기 전에는 별도 백업을 권장합니다. 기존 패치 결과 ROM에 다시 적용하지 말고, 항상 위 해시의 깨끗한 일본판 원본에 `v1.0.2` 패치를 적용하십시오.

## 이전 버전에서 업데이트

새 패치를 깨끗한 일본판 원본에 적용한 뒤 일반 세이브를 백업하고 새 ROM과 같은 기본 파일명으로 연결하십시오. 이전 ROM의 세이브스테이트는 불러오지 말고, 새로 부팅해 게임 내 저장 데이터를 로드하십시오.
