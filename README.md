# ТЗ

Необходимо реализовать веб приложение на flask, с помощью которого можно управлять дисками виртуальной машины:
1. Отмонтировать диск
2. Форматировать диск
3. Примонтировать диск

В интерфейсе веб приложения на vue необходимо отобразить диски виртуальной машины в виде таблицы, колонки которой будут имя диска | размер | mountpoint | кнопнки. Должна быть реализована форма авторизации. Без авторизации нельзя получить диски и выполнить функции над ними.

P.S. Проект отправить ссылкой на git репозиторий, для разработки приложения необходимо будет развернуть виртуальную машину с несколькими виртуальными дисками, которые можно будет посмотреть с помощью команды lsblk, отформатировать диск можно с помощью mkfs.

# Dependencies

Arch-based Linux distributions:
```bash
sudo pacman -S python python-pip python-virtualenv
```
Debian-based distributions:
```bash
sudo apt install python3 python3-pip python-virtualenv
```
Gentoo-based distributions:
```bash
sudo emerge --ask dev-lang/python dev-python/pip dev-python/virtualenv
```
RPM-based distributions:
```bash
sudo yum install -y python3 python-pip python-virtualenv
```

p.s: Подразумеваю, что машина с KVM настроена, зависимости kvm и libvirt не рассматриваю.

# Installation

```bash
git clone git://github.com/ozz.life/tempKVMFlaskVue
cd tempKVMFlaskVue/frontend/
npm install
npm run build
cd ../backend/
python3 -m venv venv
. venv/bin/activate
pip install Flask
pip install python-dotenv
pip install flask-restful
pip install black
```

# Starting

Запускать из под пользователя, имеющего необходимые права на kvm, mount/umount, директории с виртуальными машинами
```bash
cd backend/
```
```bash
chmod +x start.sh
./start.sh
```