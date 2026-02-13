# 🚀 DEPLOYMENT INSTRUCTIONS - FOLLOW THESE STEPS

## ✅ FRONTEND IS READY!

Your frontend files are prepared in: `portfolio-frontend/`
- ✅ index.html
- ✅ media/ folder with all images

---

## STEP 1: CREATE GITHUB REPOSITORY FOR FRONTEND

### Option A: Create repository named "portfolio"
1. Go to: https://github.com/new
2. Repository name: **`portfolio`**
3. Description: "My Portfolio Website"
4. **Public** repository
5. **DO NOT** initialize with README
6. Click **"Create repository"**

### Option B: Create repository named "CodesOfSanthosh.github.io" (Recommended)
1. Go to: https://github.com/new
2. Repository name: **`CodesOfSanthosh.github.io`**
3. Description: "My Portfolio Website"
4. **Public** repository
5. **DO NOT** initialize with README
6. Click **"Create repository"**

**Why Option B?** Your site will be at: https://codesofsanthosh.github.io/ (cleaner URL!)

---

## STEP 2: PUSH FRONTEND TO GITHUB

After creating the repository, GitHub will show you commands. Use these instead:

```powershell
cd c:\Users\gunap\OneDrive\Desktop\Portfolio\portfolio-frontend

git branch -M main

# Replace with YOUR repository URL
git remote add origin https://github.com/CodesOfSanthosh/CodesOfSanthosh.github.io.git

git push -u origin main
```

**You'll be asked for GitHub credentials:**
- Username: CodesOfSanthosh
- Password: Use a **Personal Access Token** (not your password!)

**How to create Personal Access Token:**
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Name: "Portfolio Deployment"
4. Select scopes: **repo** (check all boxes under repo)
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)
7. Use this token as your password when pushing

---

## STEP 3: ENABLE GITHUB PAGES

1. Go to your repository: https://github.com/CodesOfSanthosh/CodesOfSanthosh.github.io
2. Click **Settings** tab
3. Scroll down to **Pages** section (left sidebar)
4. Under **Source**, select: **main** branch
5. Click **Save**
6. Wait 2-3 minutes
7. Refresh the page
8. You'll see: "Your site is live at https://codesofsanthosh.github.io/"

✅ **Frontend deployed!**

---

## STEP 4: DEPLOY BACKEND TO RENDER

### A. Push Django Backend to GitHub

First, let's commit the API changes:

```powershell
cd c:\Users\gunap\OneDrive\Desktop\Portfolio

git add .
git commit -m "Add REST API for contact form"
git push origin main
```

### B. Create Render Account

1. Go to: https://render.com/
2. Click **"Get Started for Free"**
3. Sign up with GitHub (easiest)
4. Authorize Render to access your repositories

### C. Create Web Service on Render

1. Go to: https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect a repository"**
4. Find and select your **Portfolio** repository
5. Click **"Connect"**

### D. Configure Web Service

Fill in these settings:

**Name:** `portfolio-backend`

**Environment:** `Python 3`

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn portfolio.wsgi:application
```

**Instance Type:** `Free`

### E. Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add these variables:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | (Generate new: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.onrender.com` |
| `PYTHON_VERSION` | `3.11.0` |

Click **"Create Web Service"**

### F. Wait for Deployment

- Render will start building (5-10 minutes)
- Watch the logs
- Wait for "Build successful" and "Deploy live"
- Copy your backend URL: `https://portfolio-backend-xxxx.onrender.com`

---

## STEP 5: CONNECT FRONTEND TO BACKEND

### A. Update API URL in Frontend

1. Open: `c:\Users\gunap\OneDrive\Desktop\Portfolio\portfolio-frontend\index.html`
2. Find line ~360: `const API_URL = 'https://your-backend.onrender.com/api/contact/';`
3. Replace with YOUR Render URL:
   ```javascript
   const API_URL = 'https://portfolio-backend-xxxx.onrender.com/api/contact/';
   ```
4. Save the file

### B. Push Updated Frontend

```powershell
cd c:\Users\gunap\OneDrive\Desktop\Portfolio\portfolio-frontend

git add index.html
git commit -m "Update API URL to Render backend"
git push
```

Wait 1-2 minutes for GitHub Pages to update.

### C. Update CORS in Backend

1. Open: `c:\Users\gunap\OneDrive\Desktop\Portfolio\portfolio\settings.py`
2. Find `CORS_ALLOWED_ORIGINS` (around line 145)
3. Update with your actual GitHub Pages URL:
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://codesofsanthosh.github.io",  # Your actual URL
   ]
   ```
4. Save the file

### D. Push Backend Changes

```powershell
cd c:\Users\gunap\OneDrive\Desktop\Portfolio

git add portfolio/settings.py
git commit -m "Update CORS for GitHub Pages"
git push
```

Render will auto-redeploy (2-3 minutes).

---

## STEP 6: CREATE SUPERUSER ON RENDER

1. Go to Render Dashboard
2. Click on your **portfolio-backend** service
3. Click **"Shell"** tab (top right)
4. Run these commands:
   ```bash
   python manage.py createsuperuser
   ```
5. Enter username, email, password
6. Superuser created!

---

## STEP 7: TEST EVERYTHING

### Test Frontend:
1. Visit: `https://codesofsanthosh.github.io/`
2. Check all sections load
3. Images should display
4. Design should look good

### Test Contact Form:
1. Scroll to contact section
2. Fill out the form:
   - Name: Test User
   - Email: test@example.com
   - Subject: Test Message
   - Message: Testing contact form
3. Click "Send Message"
4. Should see: "Your message has been sent successfully!"

### Verify in Django Admin:
1. Go to: `https://portfolio-backend-xxxx.onrender.com/admin/`
2. Login with superuser credentials
3. Click "Contacts"
4. You should see the test message!

---

## ✅ DEPLOYMENT COMPLETE!

Your portfolio is now live:

**Frontend:** https://codesofsanthosh.github.io/
**Backend:** https://portfolio-backend-xxxx.onrender.com/
**Admin:** https://portfolio-backend-xxxx.onrender.com/admin/

---

## 🎉 CONGRATULATIONS!

You now have:
- ✅ Professional portfolio on GitHub Pages (FREE)
- ✅ Working contact form with Django backend (FREE tier)
- ✅ Fast loading with CDN
- ✅ Automatic HTTPS
- ✅ Easy to update

---

## 📝 TO UPDATE YOUR PORTFOLIO:

### Update Content:
1. Edit `index.html` in `portfolio-frontend/`
2. Commit and push to GitHub
3. GitHub Pages auto-updates in 1-2 minutes

### Update Backend:
1. Make changes in `Portfolio/` folder
2. Commit and push to GitHub
3. Render auto-deploys in 2-3 minutes

---

**Need help? Let me know!** 🚀
