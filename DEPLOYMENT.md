# Portfolio Deployment Guide

## Your project has been pushed to GitHub! 🎉
Repository: https://github.com/CodesOfSanthosh/portfolio

## Deploy to Render (Recommended - Free Tier Available)

### Step 1: Sign Up/Login to Render
1. Go to https://render.com
2. Sign up or login with your GitHub account

### Step 2: Create a New Web Service
1. Click "New +" button in the top right
2. Select "Web Service"
3. Connect your GitHub account if not already connected
4. Select the repository: `CodesOfSanthosh/portfolio`
5. Click "Connect"

### Step 3: Configure the Web Service
Fill in the following details:

**Name:** `santhosh-portfolio` (or any name you prefer)

**Region:** Choose the closest to your location

**Branch:** `main`

**Root Directory:** Leave blank

**Runtime:** `Python 3`

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn portfolio.wsgi:application
```

### Step 4: Add Environment Variables
Click "Advanced" and add these environment variables:

1. **SECRET_KEY**
   - Value: Generate a new secret key (use: https://djecrety.ir/)

2. **DEBUG**
   - Value: `False`

3. **ALLOWED_HOSTS**
   - Value: `.onrender.com`

4. **DATABASE_URL** (Render will auto-create this if you add a PostgreSQL database)
   - Leave blank for now, or use SQLite for testing

### Step 5: Create the Service
1. Select the **Free** plan
2. Click "Create Web Service"
3. Wait for the deployment to complete (5-10 minutes)

### Step 6: Your Site is Live! 🚀
Once deployed, Render will give you a URL like:
`https://santhosh-portfolio.onrender.com`

---

## Alternative: Deploy to Railway

### Step 1: Sign Up/Login to Railway
1. Go to https://railway.app
2. Sign up with GitHub

### Step 2: Deploy from GitHub
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `CodesOfSanthosh/portfolio`

### Step 3: Add Environment Variables
In the Variables tab, add:
- `SECRET_KEY`: (generate from https://djecrety.ir/)
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `.railway.app`

### Step 4: Deploy
Railway will automatically detect it's a Django project and deploy it!

---

## Alternative: Deploy to PythonAnywhere (Free Tier)

### Step 1: Sign Up
1. Go to https://www.pythonanywhere.com
2. Create a free account

### Step 2: Clone Your Repository
1. Open a Bash console
2. Run:
```bash
git clone https://github.com/CodesOfSanthosh/portfolio.git
cd portfolio
```

### Step 3: Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 portfolio-env
pip install -r requirements.txt
```

### Step 4: Configure Web App
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. Set the source code directory to: `/home/yourusername/portfolio`
6. Set the working directory to: `/home/yourusername/portfolio`
7. Edit the WSGI configuration file to point to your Django project

### Step 5: Set Environment Variables
In the web app settings, add your environment variables

### Step 6: Reload and Go Live!
Click "Reload" and your site will be live at:
`https://yourusername.pythonanywhere.com`

---

## Post-Deployment Checklist

After deployment, make sure to:

1. ✅ Run migrations (if using PostgreSQL):
   ```bash
   python manage.py migrate
   ```

2. ✅ Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

3. ✅ Collect static files:
   ```bash
   python manage.py collectstatic
   ```

4. ✅ Test all functionality:
   - Navigation works
   - Contact form submits
   - Admin panel accessible
   - Mobile menu works

5. ✅ Update your GitHub README with the live URL

---

## Recommended: Use Render (Easiest)

I recommend **Render** because:
- ✅ Free tier available
- ✅ Automatic deployments from GitHub
- ✅ Easy PostgreSQL database setup
- ✅ Custom domain support
- ✅ SSL certificates included
- ✅ Simple environment variable management

---

## Need Help?

If you encounter any issues during deployment, let me know and I'll help you troubleshoot!
