# Questions

## What's `stdint.h`?

stdint.h is a library which defines integer types. We use the library in order to make sure that the integer we are using run in the same type on different machines, devices, platforms,...

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

They are names of integer types. We use them to declare that an integer is in which type.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

a `BYTE` has a width of 1 byte, a `DWORD` has a width of 4 bytes, a `LONG` has a width of 4 bytes, a `WORD` has a width of 2 bytes.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

The first two bytes of any BMP file  must be 0x424D in hexadecimal or 16973 in decimal.

## What's the difference between `bfSize` and `biSize`?

bfSize specifies the size of the whole bitmap file, meanwhile biSize specifies the size of the BITMAPINFOHEADER structure in the file.

## What does it mean if `biHeight` is negative?

the bitmap file is written in top-down order, the origin of which is top left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount specifies the BMP's color depth, it determines the number of bits are used in a pixel and the maximum number of colors in the bitmap.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

They might return `NULL` because for some reasons they cannot open the file.

## Why is the third argument to `fread` always `1` in our code?

The third argument defines how many elements we want to read, we only read one element, therefore it would be 1.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

padding = 3

## What does `fseek` do?

fseek moves the file cursor/indicator step by step, but jumps over padding.

## What is `SEEK_CUR`?

It sets the offset relative to the current pointer position

## Whodunit?

It was Professor Plum with candlesticks in the library.
