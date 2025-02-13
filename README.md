# TechDash

TechDash is a Python program designed to enhance your audio experiences on Windows by modifying system volume settings based on user activity patterns. The program intelligently adjusts the volume based on whether the user is active or inactive, providing a seamless audio experience tailored to your needs.

## Features

- **Automatic Volume Adjustment**: Increases volume when the user is active and decreases it when the user is inactive.
- **User Activity Detection**: Monitors user activity to determine the appropriate volume adjustments.

## Requirements

- Windows Operating System
- Python 3.x
- `psutil` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TechDash.git
   ```
2. Navigate to the directory:
   ```bash
   cd TechDash
   ```
3. Install the required library:
   ```bash
   pip install psutil
   ```

## Usage

Run the `techdash.py` script:

```bash
python techdash.py
```

The program will adjust the system volume based on user activity patterns, checking every minute to update the volume settings.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

TechDash is designed for Windows systems. Compatibility with other operating systems is not guaranteed.