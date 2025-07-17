#include <linux/init.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/uaccess.h>

#define DEVICE_NAME "simple_char_dev"
#define BUF_LEN 1024

static int major_number;
static char device_buffer[BUF_LEN];
static int device_open = 0;

static int dev_open(struct inode *inode, struct file *file) {
    if (device_open) return -EBUSY;
    device_open++;
    try_module_get(THIS_MODULE);
    return 0;
}

static int dev_release(struct inode *inode, struct file *file) {
    device_open--;
    module_put(THIS_MODULE);
    return 0;
}

static ssize_t dev_read(struct file *filp, char __user *buffer, size_t length, loff_t *offset) {
    int bytes_read = 0;
    if (*offset >= BUF_LEN) return 0;

    if (length > BUF_LEN - *offset)
        length = BUF_LEN - *offset;

    if (copy_to_user(buffer, device_buffer + *offset, length) != 0)
        return -EFAULT;

    *offset += length;
    bytes_read = length;
    return bytes_read;
}

static ssize_t dev_write(struct file *filp, const char __user *buffer, size_t length, loff_t *offset) {
    if (*offset >= BUF_LEN) return -ENOSPC;

    if (length > BUF_LEN - *offset)
        length = BUF_LEN - *offset;

    if (copy_from_user(device_buffer + *offset, buffer, length) != 0)
        return -EFAULT;

    *offset += length;
    return length;
}

struct file_operations fops = {
    .owner = THIS_MODULE,
    .read = dev_read,
    .write = dev_write,
    .open = dev_open,
    .release = dev_release
};

static int __init simple_char_init(void) {
    major_number = register_chrdev(0, DEVICE_NAME, &fops);
    if (major_number < 0) {
        printk(KERN_ALERT "Registering char device failed with %d\n", major_number);
        return major_number;
    }
    printk(KERN_INFO "Simple char driver registered with major number %d\n", major_number);
    return 0;
}

static void __exit simple_char_exit(void) {
    unregister_chrdev(major_number, DEVICE_NAME);
    printk(KERN_INFO "Simple char driver unregistered\n");
}

module_init(simple_char_init);
module_exit(simple_char_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("ML Intern Task Generator");
MODULE_DESCRIPTION("A simple character device driver with 1KB buffer");
