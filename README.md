# Waiting Lists SaaS Platform

A modern, multi-tenant waiting list management system built with **FastAPI** (Backend) and **Vue 3** (Frontend). Designed for both General and Exclusive waiting lists with a focus on premium aesthetics and user experience.

## 🚀 project Structure

- **`/backend`**: FastAPI service with Neon (PostgreSQL) integration.
- **`/frontend`**: Vue 3 + Pinia + Vite dashboard for monitoring registrations.

## ✨ Features

- **Real-time Monitoring**: Track registrations in General and Exclusive lists.
- **Interactive Dashboard**:
  - **Sorting**: Chronological order (Newest/Oldest).
  - **Filtering**: Segment by Plan Type (Basic, Standard, Pro).
  - **WhatsApp Integration**: Direct chat links for quick follow-ups.
  - **Email Tools**: One-click copy with toast notifications.
- **Responsive Design**: Fully optimized for mobile, tablet, and desktop viewports.
- **Premium Aesthetics**: Dark-mode glassmorphism design with smooth animations.

## 🛠️ Getting Started

### Backend
1. Navigate to `/backend`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Configure `.env` with your Neon database string.
4. Run: `fastapi dev main.py`.

### Frontend
1. Navigate to `/frontend`.
2. Install dependencies: `npm install`.
3. Run development server: `npm run dev`.
4. The frontend is configured with a Vite proxy to communicate with the production API by default.

## 📡 API Documentation
The API follows a vertical slice architecture and provides Swagger documentation at:
`https://waiting-lists-production.up.railway.app/docs`

---
*Built with ❤️ for waiting list management.*