<div align="center">

# 👁️ ALEN ENTERPRISE 👁️
**AI-Powered Information Systems & Cyber Security Audit Tool**

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![CLI Framework](https://img.shields.io/badge/CLI-Click%20%2B%20Rich-ff69b4.svg?style=for-the-badge)](https://click.palletsprojects.com/)
[![AI Integration](https://img.shields.io/badge/AI-Google%20Gemini%201.5-orange.svg?style=for-the-badge&logo=google)](https://aistudio.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg?style=for-the-badge)](#)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black.svg?style=for-the-badge&logo=github)](https://github.com/alen12344/alen.audit.git)
[![Security Audits](https://img.shields.io/badge/Sec%20Audits-Enabled-red.svg?style=for-the-badge)](#)

*Empowering InfoSec through Intelligent Automation and Deep Reasoning.*

---

</div>

## 🚀 Apa itu Alen Enterprise?

**Alen Enterprise** adalah alat _Command-Line Interface_ (CLI) bergaya Kali Linux yang dirancang khusus untuk para Auditor Sistem Informasi dan praktisi _Cyber Security_. Terintegrasi langsung dengan **Google Gemini API**, alat ini tidak hanya memindai kerentanan secara mekanis, tetapi juga **berpikir, menganalisis, dan memberikan konteks** atas setiap celah keamanan yang ditemukan.

Dengan desain UI terminal yang memukau (diperkuat oleh `Rich` library) dan laporan _auto-generated_ HTML bergaya _dark-mode glassmorphism_, auditing sistem informasi sekarang terasa seperti di masa depan.

---

## 🔥 Fitur Utama (Core Features)

- **🤖 Intelegensi Buatan Terintegrasi:** Analisis pintar terhadap hasil _scanning_ menggunakan engine Gemini 1.5 Pro. Alat ini dapat menjelaskan _impact_, mitigasi, dan membedakan kemungkinan _False Positive_.
- **🔍 Cyber Security Scanner:**
  - Pemindaian Port (Terintegrasi `nmap`).
  - Inspeksi _HTTP Security Headers_.
  - Pemetaan Permukaan API (_API Surface Discovery_).
  - Pengecekan sinyal awal untuk celah kerentanan kritis seperti XSS & SQLi.
- **📄 IS Audit Lifecycle Built-in:** Mendukung tahapan _Planning_, _Scope_, _Evidence Collection_, dan _Evaluation_ berstandar audit.
- **🛡️ Engine Anti False-Positive:** Heuristik kustom dan validasi silang oleh AI untuk menyaring *noise* yang tidak penting.
- **📊 Modern HTML Reporting:** Dapatkan laporan akhir seketika dalam wujud halaman HTML interaktif dan indah untuk dipresentasikan ke Manajemen.
- **🎭 Terminal UI Futuristik:** Berinteraksi di CLI Command Line tidak pernah sekeren ini. Dilengkapi dengan animasi ASCII Eye effect, progres pemuatan yang interaktif, dan layout warna-warni.

---

## 🛠️ Instalasi & Persiapan (Termasuk Kali Linux)

### 1. Kebutuhan Sistem
Pastikan Anda sudah menginstal **Python 3.11+** di sistem Windows/Linux/MacOS Anda, dan pastikan juga `nmap` telah terpasang di *environment* sistem Anda.
(Jika menggunakan **Kali Linux**, `nmap` dan `python3` sudah terinstal secara _default_).

### 2. Cara Install dari GitHub (Direkomendasikan untuk Kali Linux)
Buka terminal kesayangan Anda (misalnya QTerminal/GNOME Terminal di Kali) dan jalankan runtutan perintah berikut:

```bash
# 1. Clone repository dari GitHub
git clone https://github.com/alen12344/alen.audit.git

# 2. Masuk ke direktori
cd alen.audit/alen_enterprise

# 3. Buat Virtual Environment 
python3 -m venv .venv

# 4. Aktifkan Virtual Environment
source .venv/bin/activate

# 5. Pasang dependensi dan Install Alat
pip install -e .
```

### 3. Konfigurasi Kunci AI (API Key)
`Alen Enterprise` kini dirancang menjadi **sangat praktis**. Anda **TIDAK PERLU** lagi repot-repot membuat atau mengedit file `.env` secara manual!

Cukup dapatkan API Key dari alat ini melalui [Google AI Studio](https://aistudio.google.com/), lalu jalankan aplikasi untuk pertama kali:
```bash
alen-audit
```
Aplikasi akan secara **otomatis** meminta Anda memasukkan API Key dan menyimpannya ke sistem secara aman (ke dalam `~/.alen_env`).

---

## 💻 Cara Menggunakan (_Usage_)

Buka terminal kesayangan Anda lalu jalankan salah satu dari dua fitur utama:

### Bantuan & Panel Utama
Tampilkan animasi inisialisasi dan daftar menu yang tersedia:
```bash
alen-audit
```

### 🎯 1. Menjalankan Cyber Scan Target
Memulai pemindaian keamanan agresif terhadap target IP atau _Domain_.
Pilih opsi **1** pada menu interaktif, lalu masukkan URL:
```text
Masukkan URL Target (contoh: https://target.com): https://dharmawacana.ac.id
```

### 📋 2. Membuat Sesi IS Audit Baru
Menginisialisasi proyek audit baru untuk pengumpulan bukti-bukti logikal dan _compliance_.
Pilih opsi **2** pada menu interaktif, lalu ikuti instruksinya.

---

## 🤝 Hubungi Sang Kreator (Contact)

Dibuat dengan ❤️ oleh **Alen Kusuma**. Ingin berdiskusi tentang keamanan cyber, request fitur, layanan pentest, atau sekadar menyapa? Jangan ragu hubungi saluran di bawah ini:

| Platform | Username / Kontak | Link Langsung |
| :--- | :--- | :--- |
| **GitHub** | `alen12344` | [⭐ Star di GitHub](https://github.com/alen12344/alen.audit.git) |
| **Instagram** | `@alen.kusumaa` | [🔥 Follow di IG](https://instagram.com/alen.kusumaa) |
| **WhatsApp** | `0857-6495-2471` | [💬 Hubungi via WA](https://wa.me/6285764952471) |

---
**Disclaimer:** *Alat ini dibuat hanya untuk tujuan edukasi dan auditing sah pada sistem yang telah diberikan izin (Authorized Penetration Testing/Compliance Audit).* Segala bentuk tindakan ilegal berada di luar tanggung jawab *developer*.
