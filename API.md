# SunEnergyXT 500 Series API Documentation

## Overview

The SunEnergyXT 500 Series inverter provides a simple HTTP API for monitoring and controlling its operations. This document describes the API endpoints, request/response formats, and usage examples.

## API Endpoints

### 1. Read Status Data

**Endpoint:** `/read`

**Method:** `GET`

**Description:** Retrieves the current status and operational data from the inverter.

**Request Example:**

```http
GET http://{inverter_ip}/read
```

**Response Format:**

```json
{
  "state": {
    "reported": {
      "WS": "string",      // Work status
      "WR": "string",      // Work mode
      "ST": "string",      // System time
      "IW": 1234,          // Input power (W)
      "OP": 1200,          // Output power (W)
      "PV": 1234,          // PV total power (W)
      "PV1": 300,          // PV string 1 power (W)
      "PV2": 310,          // PV string 2 power (W)
      "PV3": 315,          // PV string 3 power (W)
      "PV4": 309,          // PV string 4 power (W)
      "II1": 1.5,          // Input current 1 (A)
      "II2": 1.6,          // Input current 2 (A)
      "II3": 1.5,          // Input current 3 (A)
      "II4": 1.6,          // Input current 4 (A)
      "VP1": 200.5,        // Input voltage 1 (V)
      "VP2": 201.0,        // Input voltage 2 (V)
      "VP3": 200.8,        // Input voltage 3 (V)
      "VP4": 201.2,        // Input voltage 4 (V)
      "GP": 100,           // Grid power (W)
      "LP": 1100,          // Load power (W)
      "GD1": 12345,        // Grid generation total (kwh)
      "GD2": 67890,        // Grid generation total 2 (kwh)
      "LD": 54321,         // Load consumption total (kwh)
      "SC": 95,            // System status (%)
      "SC0": 90,           // System status 0 (%)
      "SC1": 92,           // System status 1 (%)
      "SC2": 94,           // System status 2 (%)
      "SC3": 96,           // System status 3 (%)
      "SC4": 98,           // System status 4 (%)
      "SC5": 100,          // System status 5 (%)
      "ON": "online",      // Online status
      "ES": "normal",      // Error status
      "BS0": "normal",     // Battery status 0
      "BS1": "normal",     // Battery status 1
      "BS2": "normal",     // Battery status 2
      "BS3": "normal",     // Battery status 3
      "BS4": "normal",     // Battery status 4
      "BS5": "normal",     // Battery status 5
      "AS": "normal",      // Alarm status
      "DS": "normal",      // Device status
      "SN": "1234567890",  // Serial number
      "MS": "SunEnergyXT", // Manufacturer
      "GS": 1000,           // Grid power setting (W)
      "IS": 500,            // Input power setting (W)
      "SI": 10,             // Start charging current (%)
      "SA": 95,             // Charging termination voltage (%)
      "SO": 20,             // Discharging termination voltage (%)
      "PT": 60,             // Protection time (min)
      "LM": 1,              // Light mode (0=off, 1=on)
      "MM": 0,              // Mute mode (0=off, 1=on)
      "PM": 1,              // Power mode (0=off, 1=on)
      "MD": "SunEnergyXT 500", // Model
      "TZ": "UTC+8"         // Time zone
    }
  }
}
```

### 2. Write Configuration Data

**Endpoint:** `/write`

**Method:** `POST`

**Description:** Writes configuration settings to the inverter.

**Request Format:**

```json
{
  "state": {
    "<parameter_key>": <value>
  }
}
```

**Response Format:**

```json
{
  "status": "success"  // or "error"
}
```

## Supported Parameters

### Read-Only Parameters

| Parameter | Description | Unit |
|-----------|-------------|------|
| WS | Work status | - |
| WR | Work mode | - |
| ST | System time | - |
| IW | Input power | W |
| OP | Output power | W |
| PV | PV total power | W |
| PV1 | PV string 1 power | W |
| PV2 | PV string 2 power | W |
| PV3 | PV string 3 power | W |
| PV4 | PV string 4 power | W |
| II1 | Input current 1 | A |
| II2 | Input current 2 | A |
| II3 | Input current 3 | A |
| II4 | Input current 4 | A |
| VP1 | Input voltage 1 | V |
| VP2 | Input voltage 2 | V |
| VP3 | Input voltage 3 | V |
| VP4 | Input voltage 4 | V |
| GP | Grid power | W |
| LP | Load power | W |
| GD1 | Grid generation total | kwh |
| GD2 | Grid generation total 2 | kwh |
| LD | Load consumption total | kwh |
| SC | System status | % |
| SC0 | System status 0 | % |
| SC1 | System status 1 | % |
| SC2 | System status 2 | % |
| SC3 | System status 3 | % |
| SC4 | System status 4 | % |
| SC5 | System status 5 | % |
| ON | Online status | - |
| ES | Error status | - |
| BS0 | Battery status 0 | - |
| BS1 | Battery status 1 | - |
| BS2 | Battery status 2 | - |
| BS3 | Battery status 3 | - |
| BS4 | Battery status 4 | - |
| BS5 | Battery status 5 | - |
| AS | Alarm status | - |
| DS | Device status | - |
| SN | Serial number | - |
| MS | Manufacturer | - |

### Read-Write Parameters

| Parameter | Description | Unit | Range | Step |
|-----------|-------------|------|-------|------|
| GS | Grid power setting | W | -2400 to 2400 | 10 |
| IS | Input power setting | W | 1 to 2400 | 10 |
| SI | Start charging current | % | 1 to 30 | 1 |
| SA | Charging termination voltage | % | 70 to 100 | 1 |
| SO | Discharging termination voltage | % | 1 to 30 | 1 |
| PT | Protection time | min | 30 to 1440 | 1 |
| LM | Light mode | - | 0 (off) to 1 (on) | - |
| MM | Mute mode | - | 0 (off) to 1 (on) | - |
| PM | Power mode | - | 0 (off) to 1 (on) | - |
| MD | Model | - | String | - |
| TZ | Time zone | - | String | - |
| RT | Restart (trigger) | - | 1 (trigger) | - |

## Usage Examples

### Example 1: Read Inverter Status

**Request:**

```http
GET http://192.168.1.100/read
```

**Response:**

```json
{
  "state": {
    "reported": {
      "WS": "normal",
      "WR": "grid_tie",
      "ST": "2024-01-20 12:00:00",
      "IW": 1500,
      "OP": 1450,
      "PV": 1500,
      "PV1": 375,
      "PV2": 375,
      "PV3": 375,
      "PV4": 375,
      "II1": 1.8,
      "II2": 1.8,
      "II3": 1.8,
      "II4": 1.8,
      "VP1": 208.3,
      "VP2": 208.5,
      "VP3": 208.2,
      "VP4": 208.4,
      "GP": 1450,
      "LP": 0,
      "GD1": 54321,
      "GD2": 123456,
      "LD": 98765,
      "SC": 98,
      "SC0": 95,
      "SC1": 96,
      "SC2": 97,
      "SC3": 98,
      "SC4": 99,
      "SC5": 100,
      "ON": "online",
      "ES": "normal",
      "BS0": "normal",
      "BS1": "normal",
      "BS2": "normal",
      "BS3": "normal",
      "BS4": "normal",
      "BS5": "normal",
      "AS": "normal",
      "DS": "normal",
      "SN": "SEXT-500-12345",
      "MS": "SunEnergyXT",
      "GS": 1000,
      "IS": 500,
      "SI": 10,
      "SA": 95,
      "SO": 20,
      "PT": 60,
      "LM": 1,
      "MM": 0,
      "PM": 1,
      "MD": "SunEnergyXT 500",
      "TZ": "UTC+8"
    }
  }
}
```

### Example 2: Set Grid Power Setting

**Request:**

```http
POST http://192.168.1.100/write
Content-Type: application/json

{
  "state": {
    "GS": 1200
  }
}
```

**Response:**

```json
{
  "status": "success"
}
```

### Example 3: Restart Inverter

**Request:**

```http
POST http://192.168.1.100/write
Content-Type: application/json

{
  "state": {
    "RT": 1
  }
}
```

**Response:**

```json
{
  "status": "success"
}
```

## Error Handling

### Common Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - Invalid JSON format or parameter |
| 403 | Forbidden - Access denied |
| 404 | Not Found - Endpoint not available |
| 500 | Internal Server Error - Inverter error |

### Error Response Example

```json
{
  "status": "error",
  "message": "Invalid parameter value"
}
```

## Integration with Home Assistant

The SunEnergyXT 500 Series Home Assistant integration uses this API to:

1. **Read data** every 3 seconds using the `/read` endpoint
2. **Write data** when users adjust settings through the UI
3. **Control the inverter** through buttons, switches, and number entities

## Rate Limiting

- The inverter may have rate limiting on API requests
- The Home Assistant integration uses a 3-second polling interval
- Avoid making more frequent requests to prevent overloading the inverter

## Security Considerations

- The API uses HTTP (not HTTPS) - use it only on trusted local networks
- There is no authentication mechanism - restrict access to the inverter's IP
- Avoid exposing the inverter to the public internet

## Troubleshooting

### API Not Responding

1. Check if the inverter is powered on
2. Verify the IP address is correct
3. Ensure the inverter is connected to the network
4. Check if the inverter's web server is running

### Invalid Response

1. Verify the inverter firmware is up to date
2. Check if the API format has changed
3. Restart the inverter if necessary

## Firmware Compatibility

This API documentation is based on SunEnergyXT 500 Series firmware version 1.0.0. API formats may change in future firmware versions.

## Support

For API-related issues, please contact SunEnergyXT support or refer to the inverter's user manual.