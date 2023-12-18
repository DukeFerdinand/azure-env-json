# azure-env-json

## Description

This script, named `azure-env-json`, is a Python utility designed to read an environment file (typically named `.env`) and convert its contents into a JSON format. The script excludes commented lines and empty lines, then formats the remaining key-value pairs into a structured JSON representation.

## Usage

### Prerequisites

Make sure you have Python installed on your system.

### Running the Script

To run the script, execute the following command:

```bash
python azure-env-json.py [FILENAME]
```

Replace `[FILENAME]` with the path to your environment file. If no filename is provided, the default is set to "./.env".

## Output

The script outputs a JSON array containing objects for each key-value pair found in the environment file. Each object includes the key, value, and a "slotSetting" field set to `false`.

### Example Output

This output is ready to be coppied into your app's advanced configuration

```json
[
    {
        "key": "API_HOST",
        "value": "https://api.yourcompany.com",
        "slotSetting": false
    },
    {
        "key": "SOME_IMPORTANT_KEY",
        "value": "sdfaosdfasdfjaklsdfj2109348uijwsda9083==",
        "slotSetting": false
    }
]
```

## Notes

- Commented lines (starting with `#`) and empty lines are excluded from the output.
- The script assumes a key-value format in the input file, with each line containing a single pair separated by an equals sign (`=`).
- Values are trimmed of leading and trailing whitespaces.
- Values have double quoutes removed instead of JSON escaped (raise an issue if you want a flag for this)
- The output JSON is indented for better readability.

Feel free to use and modify this script according to your project's needs. If you encounter any issues or have suggestions for improvements, please open an issue on the project's GitHub repository.

## License

This script is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
