# 🚀 GitHub Pages + Django Backend Deployment Guide

## 📋 Overview

Your portfolio is now split into two parts:
1. **Frontend (Static HTML)** → GitHub Pages (FREE, Fast)
2. **Backend (Django API)** → Render/Railway (for contact form)

---

## PART 1: DEPLOY FRONTEND TO GITHUB PAGES

### Step 1: Create GitHub Repository for Frontend

1. Go to: https://github.com/new
2. Repository name: **`portfolio`** or **`CodesOfSanthosh.github.io`**
3. Description: "My Portfolio Website"
4. Public repository
5. Click **"Create repository"**

### Step 2: Prepare Frontend Files

Create a new folder for frontend:
```bash
mkdir portfolio-frontend
cd portfolio-frontend
```

Copy these files to the new folder:
- `index.html` (the static file I created)
- `media/` folder (your images)

### Step 3: Initialize Git and Push

```bash
git init
git add .
git commit -m "Initial commit - Static portfolio"
git branch -M main
git remote add origin https://github.com/CodesOfSanthosh/portfolio.git
git push -u origin main
```

### Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll to **Pages** section (left sidebar)
4. Under **Source**, select: **main** branch
5. Click **Save**
6. Wait 2-3 minutes
7. Your site will be live at: `https://codesofsanthosh.github.io/portfolio/`

**OR** if you named it `CodesOfSanthosh.github.io`:
- Live at: `https://codesofsanthosh.github.io/`

---

## PART 2: DEPLOY BACKEND TO RENDER

### Step 1: Push Django Backend to GitHub

Your current Django project (with API) needs to be in a separate repository:

```bash
cd c:\Users\gunap\OneDrive\Desktop\Portfolio
git add .
git commit -m "Add REST API for contact form"
git push origin main
```

### Step 2: Deploy to Render

1. Go to: https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `portfolio-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn portfolio.wsgi:application`

5. Add Environment Variables:
   ```
   SECRET_KEY = (generate a new one)
   DEBUG = False
   ALLOWED_HOSTS = .onrender.com
   DATABASE_URL = (Render will provide this)
   ```

6. Click **"Create Web Service"**
7. Wait for deployment (5-10 minutes)
8. Your backend will be at: `https://portfolio-backend.onrender.com`

### Step 3: Update Frontend with Backend URL

1. Open `index.html`
2. Find line with `const API_URL`
3. Update to your Render URL:
   ```javascript
   const API_URL = 'https://portfolio-backend.onrender.com/api/contact/';
   ```
4. Save and push to GitHub:
   ```bash
   git add index.html
   git commit -m "Update API URL"
   git push
   ```

### Step 4: Update CORS Settings

In your Django backend `settings.py`, update CORS to include your GitHub Pages URL:

```python
CORS_ALLOWED_ORIGINS = [
    "https://codesofsanthosh.github.io",  # Your actual GitHub Pages URL
]
```

Push changes:
```bash
git add portfolio/settings.py
git commit -m "Update CORS for GitHub Pages"
git push
```

Render will auto-redeploy.

---

## PART 3: TESTING

### Test Frontend
1. Visit: `https://codesofsanthosh.github.io/portfolio/`
2. Check all sections load correctly
3. Images should display (from media folder)

### Test Contact Form
1. Scroll to contact section
2. Fill out the form
3. Click "Send Message"
4. Should see success message
5. Check Django admin on Render to verify message was saved

---

## 📁 PROJECT STRUCTURE

```
portfolio-frontend/  (GitHub Pages)
├── index.html
└── media/
    ├── projects/
    │   ├── blog.jpg
    │   ├── ecommerce.jpg
    │   ├── job_portal.jpg
    │   ├── bootstrap.jpg
    │   ├── spotify.jpg
    │   └── markus-winkler-bBm9Icw-_5M-unsplash.jpg
    └── resumes/
        └── Santhosh_P_Resume.pdf

Portfolio/  (Django Backend on Render)
├── core/
│   ├── models.py
│   ├── views.py
│   ├── api_views.py
│   ├── serializers.py
│   └── urls.py
├── portfolio/
│   ├── settings.py
│   └── urls.py
├── requirements.txt
├── Procfile
└── runtime.txt
```

---

## 🔧 CONFIGURATION FILES

### Frontend (index.html)
- Embedded portfolio data (skills, projects, certifications)
- Contact form that POSTs to Django API
- Fully static - no server needed

### Backend (Django)
- REST API endpoint: `/api/contact/`
- CORS enabled for GitHub Pages
- Stores contact form submissions in database

---

## ✅ BENEFITS OF THIS SETUP

1. **Frontend on GitHub Pages:**
   - ✅ FREE forever
   - ✅ Fast CDN delivery
   - ✅ Custom domain support
   - ✅ Automatic HTTPS
   - ✅ No server costs

2. **Backend on Render:**
   - ✅ Only used for contact form
   - ✅ Free tier available
   - ✅ Auto-deploy from GitHub
   - ✅ Can add database easily

---

## 🎯 NEXT STEPS

1. ✅ Deploy frontend to GitHub Pages
2. ✅ Deploy backend to Render
3. ✅ Update API_URL in index.html
4. ✅ Update CORS in Django settings
5. ✅ Test contact form
6. ✅ Add custom domain (optional)

---

## 🌐 YOUR LIVE URLS

**Frontend (GitHub Pages):**
- `https://codesofsanthosh.github.io/portfolio/`

**Backend API (Render):**
- `https://portfolio-backend.onrender.com/api/contact/`

**Django Admin:**
- `https://portfolio-backend.onrender.com/admin/`

---

## 🐛 TROUBLESHOOTING

### Contact form not working?
1. Check browser console for errors
2. Verify API_URL is correct in index.html
3. Check CORS settings in Django
4. Verify Render backend is running

### Images not showing?
1. Make sure `media/` folder is in GitHub Pages repo
2. Check image paths in index.html
3. Verify images are committed to Git

### Backend not deploying?
1. Check Render build logs
2. Verify requirements.txt is correct
3. Check environment variables are set

---

**Your portfolio will be live on GitHub Pages with a Django backend API!** 🚀
