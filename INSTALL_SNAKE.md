# Инструкция по установке игры "Змейка" на Windows

## 📦 Файл игры

Файл `snake.html` находится по пути:
```
/home/rim44/.openclaw/workspace/snake.html
```

Размер: ~16 КБ  
Строк кода: 446

---

## 🚀 Способ 1: Открыть прямо в браузере (быстро, без установки)

### Windows:
```
Проводник → snake.html → Дважды клик
```
Или:
```
Проводник → snake.html → ПКМ → Открыть с помощью → Edge/Chrome/Firefox
```

---

## 📥 Способ 2: Скопировать на Windows с Linux-сервера

### 2.1. Через `scp` (рекомендуется)

На Windows откройте PowerShell или CMD и выполните:

```powershell
# Скачать в папку Загрузки
scp rim44@mevm.art.it-dl.ru:/home/rim44/.openclaw/workspace/snake.html "$env:USERPROFILE\Downloads\snake.html"

# Или в конкретную папку
scp rim44@mevm.art.it-dl.ru:/home/rim44/.openclaw/workspace/snake.html "C:\Users\Имя\Games\snake.html"
```

### 2.2. Через `rsync` (если установлен)

```powershell
rsync -avz rim44@mevm.art.it-dl.ru:/home/rim44/.openclaw/workspace/snake.html ~/snake_with_ads.html
```

### 2.3. Через WinSCP (графический интерфейс)

1. Скачайте [WinSCP](https://winscp.net/)
2. Подключитесь к `mevm.art.it-dl.ru` (вход: `rim44`)
3. Найдите файл: `/home/rim44/.openclaw/workspace/snake.html`
4. Скопируйте его на компьютер

---

## 🌐 Способ 3: Открыть по ссылке (если опубликовать)

Если загрузить файл на веб-сервер, игра будет доступна по ссылке:

```bash
# На сервере скопировать в веб-директорию
sudo cp /home/rim44/.openclaw/workspace/snake.html /var/www/html/snake_new.html
```

**Ссылка будет:**
```
http://mevm.art.it-dl.ru/snake_new.html
```

---

## 🎮 Как играть на Windows

1. Откройте `snake.html` в любом браузере (Edge, Chrome, Firefox)
2. Управление:
   - **Стрелки** — движение
   - **WASD** — движение
   - **Русская раскладка** (ЦФЫВ) — тоже работает!
3. Цель: съедайте красные яблоки → змейка растёт
4. Проигрыш: врезаться в стену или в свой хвост

---

## 📋 Что внутри файла

✅ **Классическая механика змейки**  
✅ **Блок рекламы** (кликабельный)  
✅ **Модальное окно "Политика конфиденциальности"**  
✅ **Футер с ссылками**  
✅ **Адаптивная верстка**  

---

## 📝 Дополнительно: Инструкция для Linux/macOS

Смотрите файл `INSTALL_SNAKE_LINUX.md` (если нужен).

---

**Приятной игры! 🐍🎮**
