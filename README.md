# Junk Data Generator

This Python script generates junk data of a specified size and writes it to a file. You can choose between generating random bytes or alphanumeric strings.

## Features

* Generates cryptographically secure random bytes (default) or alphanumeric strings.
* Specifies the size of the junk data in kilobytes.
* Outputs the data to a file.

## Usage

```python
python junk_data_generator.py [options]
```

**Options:**

* `-s`, `--size`: Size of junk data in kilobytes (default: 124)
* `-f`, `--filename`: Output filename (default: junk_data.bin)
* `-a`, `--alphanumeric`: Generate alphanumeric data instead of random bytes


## Example Usage

**Generate 1 MB of random bytes and write to a file named "random_data.bin"**

```python
python junk_data_generator.py -s 1024 -f random_data.bin
```

**Generate 500 KB of alphanumeric data and write to a file named "test_data.txt"**

```python
python junk_data_generator.py -s 512 -f test_data.txt -a
```
