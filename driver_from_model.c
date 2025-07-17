#include <stdio.h>
#include <string.h>

#define DEVICE_NAME "simple_char_dev"
#define BUF_LEN 1024

static char device_buffer[BUF_LEN];
static int device_open = 0;

int dev_open() {
    if (device_open) return -1;
    device_open++;
    return 0;
}

int dev_release() {
    device_open--;
    return 0;
}

int dev_read(char *buffer, size_t length, size_t *offset) {
    if (*offset >= BUF_LEN) return 0;
    if (length > BUF_LEN - *offset)
        length = BUF_LEN - *offset;
    memcpy(buffer, device_buffer + *offset, length);
    *offset += length;
    return length;
}

int dev_write(const char *buffer, size_t length, size_t *offset) {
    if (*offset >= BUF_LEN) return -1;
    if (length > BUF_LEN - *offset)
        length = BUF_LEN - *offset;
    memcpy(device_buffer + *offset, buffer, length);
    *offset += length;
    return length;
}
