# ZIP-CEN-OP

ZIP-CEN-OP is a command-line tool for manipulating the encryption flags in ZIP file central directories. It allows you to add or remove encryption flags without actually encrypting or decrypting the contents, which can be useful for testing or working with systems that expect certain ZIP file characteristics.

## Features

- Add encryption flags to ZIP files (fake encryption)
- Remove encryption flags from ZIP files (fake decryption)
- Easy-to-use command-line interface

## Installation

You can install ZIP-CEN-OP using pip:

```
pip install zip-cen-op
```

## Usage

After installation, you can use the `zipcenop` command directly from your terminal:

```
zipcenop <option> <file>
```

Where:
- `<option>` is either `r` (recover/remove encryption flag) or `e` (encrypt/add encryption flag)
- `<file>` is the path to the ZIP file you want to manipulate

### Examples

To add an encryption flag to a ZIP file:

```
zipcenop e path/to/your/file.zip
```

To remove an encryption flag from a ZIP file:

```
zipcenop r path/to/your/file.zip
```

## Warning

This tool only manipulates the encryption flag in the ZIP file's central directory. It does not actually encrypt or decrypt the contents of the ZIP file. Use this tool responsibly and be aware of potential security implications.

## Contributing

Contributions to ZIP-CEN-OP are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is provided as-is, without any warranties. Always backup your files before using this or any other tool that modifies file structures.

## Contact

If you have any questions or feedback, please open an issue on the GitHub repository.

---

Remember to replace "path/to/your/file.zip" with actual examples if you prefer, and to update any details that might be specific to your implementation or preferences.