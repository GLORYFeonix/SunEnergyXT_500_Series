# SunEnergyXT 500 Series

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

## Language / Sprache / 语言

- [English](README.md) (default)
- [中文](README.zh.md)
- [Deutsch](README.de.md)

## Einführung

SunEnergyXT 500 Series ist eine benutzerdefinierte Integration für Home Assistant, mit der Sie SunEnergyXT 500-Serien-Wechselrichter überwachen und steuern können.

## Funktionen

- Überwachung des Echtzeitstatus und der Daten des Wechselrichters
- Steuerung verschiedener Modi und Einstellungen des Wechselrichters
- Anpassung der Parameter des Wechselrichters
- Unterstützung der automatischen Geräteerkennung über Zeroconf

## Installation

### Installation über HACS (empfohlen)

1. Öffnen Sie HACS in Home Assistant
2. Klicken Sie auf "Integrationen"
3. Klicken Sie unten rechts auf "+ Repositories durchsuchen & herunterladen"
4. Suchen Sie nach "SunEnergyXT 500 Series"
5. Klicken Sie auf "Herunterladen"
6. Starten Sie Home Assistant neu

### Manuelle Installation

1. Laden Sie das neueste [Release-Paket](https://github.com/GLORYFeonix/SunEnergyXT_500_Series/releases) herunter
2. Entpacken Sie es in das Verzeichnis `config/custom_components/`
3. Stellen Sie sicher, dass die Verzeichnisstruktur `config/custom_components/sunenergyxt/` ist
4. Starten Sie Home Assistant neu

## Konfiguration

1. Gehen Sie in Home Assistant zu "Konfiguration" > "Geräte & Dienste"
2. Klicken Sie auf "+ Integration hinzufügen"
3. Suchen Sie nach "SunEnergyXT 500 Series"
4. Folgen Sie den Anweisungen, um den Konfigurationsprozess abzuschließen
   - Geben Sie die IP-Adresse des Wechselrichters ein
   - Geben Sie die Seriennummer des Wechselrichters ein

## Entitätsbeschreibung

### Sensor

| Entitäts-ID | Name | Einheit | Beschreibung |
|------------|------|---------|-------------|
| WS | Arbeitsstatus | - | Arbeitsstatus des Wechselrichters |
| WR | Arbeitsmodus | - | Arbeitsmodus des Wechselrichters |
| ST | Systemzeit | - | Systemzeit des Wechselrichters |
| IW | Eingangsleistung | W | Eingangsleistung des Wechselrichters |
| OP | Ausgangsleistung | W | Ausgangsleistung des Wechselrichters |
| PV | PV Gesamtleistung | W | Gesamtphotovoltaische Leistung |
| PV1 | PV String 1 Leistung | W | Leistung des Photovoltaik-Strings 1 |
| PV2 | PV String 2 Leistung | W | Leistung des Photovoltaik-Strings 2 |
| PV3 | PV String 3 Leistung | W | Leistung des Photovoltaik-Strings 3 |
| PV4 | PV String 4 Leistung | W | Leistung des Photovoltaik-Strings 4 |
| II1 | Eingangsstrom 1 | A | Eingangsstrom 1 |
| II2 | Eingangsstrom 2 | A | Eingangsstrom 2 |
| II3 | Eingangsstrom 3 | A | Eingangsstrom 3 |
| II4 | Eingangsstrom 4 | A | Eingangsstrom 4 |
| VP1 | Eingangsspannung 1 | V | Eingangsspannung 1 |
| VP2 | Eingangsspannung 2 | V | Eingangsspannung 2 |
| VP3 | Eingangsspannung 3 | V | Eingangsspannung 3 |
| VP4 | Eingangsspannung 4 | V | Eingangsspannung 4 |
| GP | Netzleistung | W | Netzleistung |
| LP | Lastleistung | W | Lastleistung |
| GD1 | Netzeinspeisung Gesamt | kwh | Gesamtnetzeinspeisung |
| GD2 | Netzeinspeisung Gesamt 2 | kwh | Gesamtnetzeinspeisung 2 |
| LD | Lastverbrauch Gesamt | kwh | Gesamtlastverbrauch |
| SC | Systemstatus | % | Systemstatus |
| SC0 | Systemstatus 0 | % | Systemstatus 0 |
| SC1 | Systemstatus 1 | % | Systemstatus 1 |
| SC2 | Systemstatus 2 | % | Systemstatus 2 |
| SC3 | Systemstatus 3 | % | Systemstatus 3 |
| SC4 | Systemstatus 4 | % | Systemstatus 4 |
| SC5 | Systemstatus 5 | % | Systemstatus 5 |
| ON | Online-Status | - | Online-Status des Wechselrichters |
| ES | Fehlerstatus | - | Fehlerstatus des Wechselrichters |
| BS0 | Batteriestatus 0 | - | Batteriestatus 0 |
| BS1 | Batteriestatus 1 | - | Batteriestatus 1 |
| BS2 | Batteriestatus 2 | - | Batteriestatus 2 |
| BS3 | Batteriestatus 3 | - | Batteriestatus 3 |
| BS4 | Batteriestatus 4 | - | Batteriestatus 4 |
| BS5 | Batteriestatus 5 | - | Batteriestatus 5 |
| AS | Alarmstatus | - | Alarmstatus des Wechselrichters |
| DS | Gerätestatus | - | Gerätestatus |
| SN | Seriennummer | - | Seriennummer des Wechselrichters |
| MS | Hersteller | - | Hersteller des Wechselrichters |

### Number

| Entitäts-ID | Name | Einheit | Bereich | Schritt | Beschreibung |
|------------|------|---------|--------|--------|-------------|
| GS | Netzleistungseinstellung | W | -2400 bis 2400 | 10 | Netzleistungseinstellung |
| IS | Eingangsleistungseinstellung | W | 1 bis 2400 | 10 | Eingangsleistungseinstellung |
| SI | Startladestrom | % | 1 bis 30 | 1 | Startladestrom |
| SA | Ladeendspannung | % | 70 bis 100 | 1 | Ladeendspannung |
| SO | Entladeendspannung | % | 1 bis 30 | 1 | Entladeendspannung |
| PT | Schutzzeit | min | 30 bis 1440 | 1 | Schutzzeit |

### Button

| Entitäts-ID | Name | Beschreibung |
|------------|------|-------------|
| RT | Neustart | Wechselrichter neu starten |

### Switch

| Entitäts-ID | Name | Beschreibung |
|------------|------|-------------|
| LM | Lichtmodus | Lichtmodus-Schalter |
| MM | Stummmodus | Stummmodus-Schalter |
| PM | Strommodus | Strommodus-Schalter |

### Text

| Entitäts-ID | Name | Beschreibung |
|------------|------|-------------|
| MD | Modell | Modell des Wechselrichters |
| TZ | Zeitzone | Zeitzoneinstellung des Wechselrichters |

## Fehlerbehebung

### Gerät nicht gefunden

- Stellen Sie sicher, dass der Wechselrichter eingeschaltet und mit dem Netzwerk verbunden ist
- Stellen Sie sicher, dass Home Assistant und der Wechselrichter im selben Netzwerksegment sind
- Versuchen Sie, die IP-Adresse des Wechselrichters manuell einzugeben

### Datenaktualisierungsprobleme

- Überprüfen Sie, ob die Netzwerkverbindung stabil ist
- Überprüfen Sie, ob der Wechselrichter normal arbeitet
- Versuchen Sie, den Wechselrichter und Home Assistant neu zu starten

## Beitrag

Beiträge sind willkommen! Bitte senden Sie Issues oder Pull Requests auf [GitHub](https://github.com/GLORYFeonix/SunEnergyXT_500_Series).

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - Details finden Sie in der [LICENSE](LICENSE)-Datei.

[releases-shield]: https://img.shields.io/github/release/GLORYFeonix/SunEnergyXT_500_Series.svg
[releases]: https://github.com/GLORYFeonix/SunEnergyXT_500_Series/releases
[commits-shield]: https://img.shields.io/github/commit-activity/y/GLORYFeonix/SunEnergyXT_500_Series.svg
[commits]: https://github.com/GLORYFeonix/SunEnergyXT_500_Series/commits/main
[license-shield]: https://img.shields.io/github/license/GLORYFeonix/SunEnergyXT_500_Series.svg