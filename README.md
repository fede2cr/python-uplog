# python-uplog
Uplog was an excelent tool to ping a host every second and log it. It's obsolete, so this is a rewrite in python.

## Install

You only need the Python3 module called ``scapy``.

```bash
sudo pip3 install scapy
```

Now, you can run (recommended under ``screen`` or similar application):

```bash
sudo python3 uplog.py www.greencore.co.cr 2>&1 >/dev/null
```

Now, you'll have a new file called ``uplog.txt`` which should look like this:

```
[18:30:00]|[......................................................]
[18:31:00]|[......................................................]
[18:32:00]|[......................................................]
[18:33:01]|[......................................................]
[18:34:00]|[......................................................]
[18:35:00]|[.....................-................................]
[18:36:00]|[.....-................................................]
```

In this case, we only lost two packets, one at minute 35 and another at minute 36.
