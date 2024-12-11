# SS Config Updater

This repository automatically fetches and updates Shadowsocks configurations from ProjectAinita servers every 1 hours.

```URL
https://raw.githubusercontent.com/4n0nymou3/ss-config-updater/refs/heads/main/configs.txt
```

## Overview

This project maintains an auto-updating list of Shadowsocks configurations sourced from ProjectAinita servers. The configurations are updated daily to ensure reliability and continuous access.

## Features

- Automatic updates every 1 hours
- Reliable configuration fetching
- GitHub Actions automated workflow
- Clean and formatted output
- Built-in error handling and logging

## How It Works

1. The GitHub Actions workflow runs automatically every 1 hours
2. Python script fetches configurations from ProjectAinita servers
3. Configurations are validated and formatted
4. Results are saved to `configs.txt`
5. Changes are automatically committed if new configurations are available

## Usage

The configurations are available in the `configs.txt` file in this repository. The file is automatically updated daily with the latest configurations.

## Acknowledgments

Special thanks to:
- [ProjectAinita](https://ainita.net/vpn) for providing the server infrastructure and original configurations
- This project wouldn't be possible without their excellent work and dedication

## Credits

This is a configuration aggregator for ProjectAinita servers. All server configurations and infrastructure are provided by ProjectAinita. We are merely providing an automated way to fetch and format these configurations.

## Important Notes

- All server infrastructure and configurations are provided by ProjectAinita
- Updates occur every 1 hours
- Check the Actions tab for update status

## Repository Status
![Update SS Configs](https://github.com/4n0nymou3/ss-config-updater/workflows/Update%20SS%20Configs/badge.svg)

## License

This project is open-source and available under the MIT License.