# Docker build fails: DNS / network

If you see **`lookup production.cloudflare.docker.com: getaddrinfow`** or **"temporary error during hostname resolution"**, WSL cannot resolve Docker Hub's hostname.

---

## 1. Fix WSL DNS (often fixes it)

In WSL:

```bash
sudo nano /etc/resolv.conf
```

Set the contents to:

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

Save (Ctrl+O, Enter) and exit (Ctrl+X). Then prevent WSL from overwriting it:

```bash
sudo bash -c 'echo "[network]\ngenerateResolvConf = false" > /etc/wsl.conf'
```

**Restart WSL:** In PowerShell run `wsl --shutdown`, then open Ubuntu again.

---

## 2. Check internet and DNS

```bash
ping -c 2 8.8.8.8
ping -c 2 production.cloudflare.docker.com
```

- If the first works but the second fails → DNS was the issue (step 1 usually fixes it).
- If both fail → check your internet connection or firewall.

---

## 3. Retry the build

```bash
cd "/mnt/c/Users/dawit/Desktop/ai pre/question5/docker"
docker build -t traveling_ethiopia_robot:noetic .
```

---

## 4. Legacy builder warning

The message **"The legacy builder is deprecated"** is a warning only. The build still works. You can ignore it or later use:  
`DOCKER_BUILDKIT=1 docker build -t traveling_ethiopia_robot:noetic .`
