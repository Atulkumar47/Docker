🛠 Docker Volume Persistence: Bind Mounts on Linux Containers 🏗️

## 📌 Introduction
This guide explores how to use Docker **bind mounts** with a Linux container to ensure data persists beyond the container’s lifecycle. By mounting a local directory into a container, you can retain files even after the container is deleted.

---

## 🔧 Steps & Observations

### 🏗️ Step 1: Running a Container with a Bind Mount
Run the following command:

```bash
docker run -dit --name alpine_with_bind_mount -v C:\Users\asus\docker_data:/data alpine:latest sh
```

### 🔍 What Happens?
- If `alpine:latest` is not available locally, Docker pulls it from the official repository.
- A new container named `alpine_with_bind_mount` is created.
- The `-v` flag mounts the local directory `C:\Users\asus\docker_data` to `/data` inside the container.
- The container starts a shell (`sh`) in detached mode.

---

### 📄 Step 2: Creating a File Inside the Bind Mount
Inside the container, create a file:

```bash
docker exec -it alpine_with_bind_mount sh -c "echo 'Hello, Atul!' > /data/testfile.txt"
```

### 🔍 What Happens?
- A shell command is executed inside the running container.
- A file `testfile.txt` is created inside `/data` with the text **"Hello, Atul!"**.
- Since `/data` is a **bind-mounted** directory, the file is actually stored in `C:\Users\asus\docker_data` on the host machine.

---

### ✅ Step 3: Verifying the File Exists
Check the contents of the file:

```bash
docker exec -it alpine_with_bind_mount sh -c "cat /data/testfile.txt"
```

#### 📌 Output:
```
Hello, Atul!
```
✔️ This confirms that the file was successfully created and accessible inside the container.

---

### 🗑 Step 4: Removing the First Container
Remove the container using:

```bash
docker rm -f alpine_with_bind_mount
```

### 🔍 What Happens?
- The container is **forcefully stopped** and removed.
- However, since `testfile.txt` was stored in a **bind-mounted directory**, it remains available on the host system. 🏡

---

### 🔄 Step 5: Creating a New Container with the Same Bind Mount
Run a new container:

```bash
docker run -dit --name new_alpine -v C:\Users\asus\docker_data:/data alpine sh
```

### 🔍 What Happens?
- A new container named `new_alpine` is launched.
- The **same bind-mounted directory** (`C:\Users\asus\docker_data`) is mounted to `/data` inside the new container.

---

### 🔎 Step 6: Verifying File Persistence
Check if `testfile.txt` still exists inside the new container:

```bash
docker exec -it new_alpine sh -c "cat /data/testfile.txt"
```

#### 📌 Output:
```
Hello, Atul!
```
✔️ This confirms that **bind mounts ensure data persists** even when the container is removed and recreated. 🔥

---

## 🎯 Conclusion
✅ **Bind mounts allow data persistence** across multiple container instances.
✅ **Deleting a container does not remove data** stored in the bind-mounted directory.
✅ **New containers using the same bind mount** can access previous data.
✅ **Useful for sharing files** between containers and retaining data beyond the container’s lifecycle.

---

## 🚀 Next Steps
🔹 **Experiment with named volumes** (`docker volume create`) for better storage management.
🔹 **Try bind mounts with different container images** to understand their flexibility.
🔹 **Explore permission settings** and their impact on bind-mounted files between host and container.

🚀 Keep exploring Docker, and happy coding! 💡

